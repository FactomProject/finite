import time

_STATE = "_STATE"

_EVENT = "_EVENT"

__STOR = {'_SCHEMA': {_EVENT: None, _STATE: None}}
""" simple k/v storage """

# REVIEW:
# consider refactoring to support
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.memmap.html


def initialize(chain, schema):
    global __STOR
    __STOR[_chainid(chain, schema)] = {_EVENT: {}, _STATE: {}}


def _chainid(chain='', schema=''):
    return schema + "::" + chain


def get_state(chain, schema, oid):
    global __STOR
    d = None
    try:
        d = __STOR[_chainid(chain, schema)][_STATE][oid]
    except KeyError as x:
        pass
    return d


def set_state(chain, schema, oid, head, new_state):
    """ set new state """
    global __STOR
    stored = False
    try:
        __STOR[_chainid(chain, schema)][_STATE][oid] = (head, new_state)
        stored = True
    except KeyError as x:
        pass
    return stored


def append_event(
        chain,
        schema,
        oid,
        parent,
        event_id,
        commands,
        new_state,
        payload):
    """ store new event """

    global __STOR
    stored = False
    k = _chainid(chain, schema)

    if oid not in __STOR[k][_EVENT]:
        __STOR[k][_EVENT][oid] = {}

    try:
        __STOR[k][_EVENT][oid][event_id] = (
            parent, commands, new_state, payload, time.time())
        stored = True
    except KeyError as x:
        pass
    return stored


def get_event(chain, schema, oid, event_id):
    """ retrieve previous event """

    global __STOR
    d = None
    k = _chainid(chain, schema)

    try:
        d = __STOR[k][_EVENT][oid][event_id]
    except KeyError as x:
        pass
    return d
