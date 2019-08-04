
# REVIEW:
# consider refactoring to support
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.memmap.html

__STOR = {'base': {"_EVENT": None, "_STATE": None}}


def get_state(chain, schema, oid):
    # TODO: return should match db columns
    # return None, None
    return None


def set_state(chain, schema, oid, head, new_state):
    # FIXME
    pass


def append_event(
        chain,
        schema,
        oid,
        parent,
        event_id,
        commands,
        new_state,
        payload):
    # FIXME
    pass
