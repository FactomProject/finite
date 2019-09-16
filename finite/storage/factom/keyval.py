import time
import json
from factom import Factomd, FactomWalletd
from finite.storage import encode as _b

VERSION = "v1"

PROTO = "https://project.factom.com/ptnet-eventstore/event.proto"
""" protobuf defs """

_STATE = "_STATE"

_EVENT = "_EVENT"

_CHAINID = '8aea9badb6ba2da807ed1dffff61f36db836e2cbb467558dd8b214ce6088e8e9'


def initialize(chain, schema):
    global __DB
    __DB = Blockchain(chain, schema)
    return __DB


def _chainid(chain='', schema=''):
    # TODO return proper chainId generated using these w/ ExtIDs
    # EXTIDS = VERSION + PROTO
    # return schema + "::" + chain
    return _CHAINID


__DB = None
""" Singleton Blockchain object """

walletd = FactomWalletd()

factomd = Factomd(
    # host='http://factomd:8088',
    host='http://127.0.0.1:8088',
    fct_address='FA2jK2HcLnRdS94dEcU27rF3meoJfpUcZPSinpb7AwQvPRY6RL1Q',
    ec_address='EC3Hu1W7uMHf7CtSva1cMyr5rXKsu7rVqQtkJCDHqEV9dgh5FjAj'
    # username='rpc_username',
    # password='rpc_password'
)


class Blockchain(object):
    """
    wrapper for peristing writes to Factom
    """
    STOR = {}

    def __init__(self, chain, schema):
        self.STOR[_chainid(chain, schema)] = {_EVENT: {}, _STATE: {}}
        try:
            # TODO: use hash of state machine as chain_content
            r = walletd.new_chain(factomd, [b'finite', _b(
                schema)], b'chain_content', ec_address=factomd.ec_address)
            print(r)
        except Exception as x:
            pass

        # assert our chain exists
        r = factomd.chain_head(_CHAINID)
        assert 'chainhead' in r

    def __getitem__(self, key):
        return self.STOR[key]

    def get_state(self, chain, schema, oid):
        d = None
        try:
            d = self[_chainid(chain, schema)][_STATE][oid]
        except KeyError as x:
            # TODO lookup in Factom
            pass
        return d

    def set_state(self, chain, schema, oid, head, new_state):
        """ set new state """
        try:
            self[_chainid(chain, schema)][_STATE][oid] = (head, new_state)
            return True
        except KeyError as x:
            # TODO should this exception bubble up?
            pass

        return False

    def append_event(self, chain, schema, oid, parent,
                     event_id, commands, new_state, payload):
        """ store new event """
        k = _chainid(chain, schema)

        try:
            if oid not in self[k][_EVENT]:
                self[k][_EVENT][oid] = {}

            self[k][_EVENT][oid][event_id] = (
                parent, commands, new_state, payload, time.time())

            # TODO: specify parent commit & add actual body
            r = walletd.new_entry(factomd, k, [b'finite', _b(schema)], _b(
                json.dumps(payload)), ec_address=factomd.ec_address)
            print(r)

            return True
        except KeyError as x:
            pass

        return False

    def get_event(self, chain, schema, oid, event_id):
        """ retrieve previous event """

        d = None
        k = _chainid(chain, schema)

        try:
            d = self[k][_EVENT][oid][event_id]
            # FIXME: lookup from factomd
        except KeyError as x:
            pass

        return d

    def find_event(self, chain, schema, oid, event_id):
        r = factomd.read_chain(_chainid(chain, schema))
        #import IPython ; IPython.embed()
        print("\nFIND:", chain, schema, oid, event_id)
        print(r)
        return[0]  # KLUDGE: just return the last one


def get_state(chain, schema, oid):
    return __DB.get_state(chain, schema, oid)


def set_state(chain, schema, oid, head, new_state):
    return __DB.set_state(chain, schema, oid, head, new_state)


def append_event(chain, schema, oid, parent, event_id,
                 commands, new_state, payload):
    return __DB.append_event(chain, schema, oid, parent,
                             event_id, commands, new_state, payload)


def get_event(chain, schema, oid, event_id):
    return __DB.get_event(chain, schema, oid, event_id)


def find_event(chain, schema, oid, event_id):
    return __DB.find_event(chain, schema, oid, event_id)
    return __DB.get_event(chain, schema, oid, event_id)
