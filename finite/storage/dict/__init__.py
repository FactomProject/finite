import json
import uuid
from finite.storage.dict import keyval as kv


class Unimplemented(Exception):
    pass


class RoleFail(Exception):
    pass


SUPERUSER = '*'
""" role used to bypass all permission checks """

ROOT_UUID = '00000000-0000-0000-0000-000000000000'
""" parent UUID used to initialize a stream """

DEFAULT_SCHEMA = 'base'
""" event schema to use if not provided """


""" python dict use to emulate database storage """


class Storage(object):

    SOURCE_HEADER = "from finite.storage.dict import Storage"
    """ import line used to include this class in generated code """

    EVENT = "_EVENT"
    """ event table """

    STATE = "_STATE"
    """ state table """

    @staticmethod
    def reconnect(**kwargs):
        """ create connection pool """
        print(kwargs)

    @staticmethod
    def drop():
        """ drop evenstore tables """

    @staticmethod
    def migrate():
        """ create evenstore tables if missing """

    def __init__(self, **kwargs):
        """ set object uuid for storage instance """
        self.schema = kwargs['schema']
        self.oid = str(uuid.uuid4())
        self.chain = str(uuid.uuid4())  # FIXME should create a proper chain ID

    def __call__(self, action, **kwargs):
        """ append a new event """
        # REVIEW: should chainid be a kwarg?

        event_id = str(uuid.uuid4())
        payload = None
        new_state = None
        err = None

        try:
            if 'multiple' in kwargs:
                multiple = int(kwargs['multiple'])
            else:
                multiple = 1

            if 'payload' in kwargs:
                if isinstance(kwargs['payload'], dict):
                    payload = json.dumps(kwargs['payload'])
                else:
                    # already json encoded string
                    payload = kwargs['payload']
            else:
                # cannot be null
                payload = "{}"

            def _txn():

                previous = kv.get_state(self.chain, self.schema, self.oid)

                if not previous:
                    current_state = self.inital_vector()
                    parent = ROOT_UUID
                else:
                    # FIXME: update to map return values
                    current_state = previous[2]
                    parent = previous[3]

                new_state, role = self.transform(
                    current_state, action, multiple)

                if role not in kwargs['roles'] and SUPERUSER not in kwargs['roles']:
                    raise RoleFail("Missing Required Role: " + role)

                kv.set_state(
                    self.chain,
                    self.schema,
                    self.oid,
                    event_id,
                    new_state)

                # FIXME actually support multiple actions
                kv.append_event(
                    self.chain, self.schema, self.oid, parent, event_id, [
                        (action, multiple)], new_state, payload)

            _txn()

        except Exception as x:
            err = x

        return event_id, new_state, err

    def events(self):
        """ list all events """

    def event(self, uuid):
        """ get a single event """

    def state(self):
        """ get state """
