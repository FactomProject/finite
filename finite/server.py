""" """
import os
import sys
import time
import logging
import threading
import grpc
import finite
# KLUDGE: alter path to import proto3 generated python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # noqa
import finite.event_pb2_grpc as event_pb2_grpc
import finite.event_pb2 as event_pb2
from concurrent import futures


class TestServer(threading.Thread):

    def __init__(self, *args, **kwargs):
        self.s = server()
        super(TestServer, self).__init__(*args, **kwargs)

    def run(self):
        self.s.start()

    def join(self, *args, **kwargs):
        self.s.stop(0)
        super(TestServer, self).join(*args, **kwargs)


class EventStore(event_pb2_grpc.EventStoreServicer):

    def Status(self, request, context):
        return event_pb2.Pong(nonce=request.nonce, code=0)

    def ListMachines(self, request, context):
        return event_pb2.MachineList(list=finite.schemata())

    def GetMachine(self, request, context):
        sm = finite.eventstore(
            schema=request.schema,
            chain=request.chain,
            oid=request.id)

        txn_defs = {}
        for label, txn in sm.transitions.items():

            guard_defs = {}
            for condition, guard in txn['guards'].items():
                guard_defs[condition] = event_pb2.Guard(delta=guard)

            txn_defs[label] = event_pb2.Transition(
                delta=txn['delta'], role=txn['role'], guards=guard_defs)

        return event_pb2.Machine(
            schema=request.schema,
            initial=sm.initial_vector(),
            capacity=sm.capacity_vector(),
            transitions=txn_defs)

    def GetPlaceMap(self, request, context):
        sm = finite.eventstore(
            schema=request.schema,
            chain=request.chain,
            oid=request.id)

        place_defs = {}
        for label, place in sm.places.items():
            place_defs[label] = event_pb2.Place(
                offset=place['offset'],
                initial=place['initial'],
                capacity=place['capacity'])

        return event_pb2.PlaceMap(schema=request.schema, map=place_defs)

    def Dispatch(self, request, context):
        sm = finite.eventstore(
            schema=request.schema,
            chain=request.chain,
            oid=request.id)

        # FIXME: convert command.actions to multiple format

        # KLUDGE just dispatch first action without setting multiple

        # FIXME: this seems to initalize the storage with a new oid every time
        # TODO: make this a param
        res = sm(request.action[0].action, roles=['*'], payload={})

        # res = ('94c6a5f7-2828-4038-bf7b-c2adfa8e6dfe', [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1], None)

        # TODO make assertion that state matches expected state
        print(res)

        state = event_pb2.State(
            id=request.id,
            schema=request.schema,
            state=res[1],
            head=res[0],
            created=None,  # FIXME add time
            updated=None)  # FIXME get state

        return event_pb2.EventStatus(state=state, code=0, message="hello")

    def GetEvent(self, request, context):
        sm = finite.eventstore(
            schema=request.schema,
            chain=request.chain,
            oid=request.id)

        # FIXME retrieve the event or list of events if uuid is not passed

        events = []
        if request.uuid is None:
            # get all events
            # FIXME:  add query
            pass
        else:
            # get single event
            e = sm.event(request.uuid)
            if e is None:
                raise Exception("Missing Event uuid: %s" % request.uuid)

            # TODO: add remaining fields
            event = event_pb2.Event(
                id=request.id,
                schema=request.schema,
                chain=request.chain,
                action=None,  # FIXME: add actions
                payload=None,
                state=e[2],
                ts=None,
                uuid=request.uuid,
                parent=e[0])

            events.append(event)

        return event_pb2.EventList(list=events)

    def GetState(self, request, context):
        sm = finite.eventstore(
            schema=request.schema,
            chain=request.chain,
            oid=request.id)

        s = sm.state()

        state = event_pb2.State(
            id=request.id,
            schema=request.schema,
            chain=request.chain,
            state=s[1],
            head=s[0],
            created=None,
            updated=None)

        # FIXME
        # get current state
        if request.uuid is None:
            pass
        # get state at given event uuid
        else:
            pass

        return event_pb2.StateList(list=[state])


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    event_pb2_grpc.add_EventStoreServicer_to_server(EventStore(), server)
    server.add_insecure_port('[::]:50051')
    return server


def serve():
    _server = server()
    _server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        _server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
