import time
from factom import Factomd, FactomWalletd

VERSION = "v1"

PROTO = "https://project.factom.com/ptnet-eventstore/event.proto"
""" protobuf defs """

_STATE = "_STATE"

_EVENT = "_EVENT"

def initialize(chain, schema):
    global __DB
    __DB = Blockchain(chain, schema)


def _chainid(chain='', schema=''):
    # TODO return proper chainId generated using these w/ ExtIDs
    # EXTIDS = VERSION + PROTO
    return schema + "::" + chain

__DB = None
""" Singleton Blockchain object """

class Blockchain(object):
    """
    wrapper for peristing writes to Factom
    """

    walletd = FactomWalletd()

    factomd = Factomd(
        host='http://factomd:8088',
        fct_address='FA2jK2HcLnRdS94dEcU27rF3meoJfpUcZPSinpb7AwQvPRY6RL1Q',
        ec_address='EC2jhmCtabeTXGtuLi3AaPzvwSuqksdVsjfxXMXV5gPmipXc4GjC'
        # username='rpc_username',
        # password='rpc_password'
    )

    STOR = {}

    def __init__(self, chain, schema):
        self.STOR[_chainid(chain, schema)] = {_EVENT: {}, _STATE: {}}

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

    def append_event(self, chain, schema, oid, parent, event_id, commands, new_state, payload):
        """ store new event """
        k = _chainid(chain, schema)

        try:
            if oid not in self[k][_EVENT]:
                self[k][_EVENT][oid] = {}

            self[k][_EVENT][oid][event_id] = (
                parent, commands, new_state, payload, time.time())
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
        except KeyError as x:
            pass

        return d


def get_state(chain, schema, oid):
    return __DB.get_state(chain, schema, oid)


def set_state(chain, schema, oid, head, new_state):
    return __DB.set_state(chain, schema, oid, head, new_state)


def append_event(chain, schema, oid, parent, event_id, commands, new_state, payload):
    return __DB.append_event(chain, schema, oid, parent, event_id, commands, new_state, payload)


def get_event(chain, schema, oid, event_id):
    return __DB.get_event(chain, schema, oid, event_id)
