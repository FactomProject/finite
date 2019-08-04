""" """
import finite.event_pb2_grpc as event_pb2_grpc
import finite.event_pb2 as event_pb2
from concurrent import futures
import os
import sys
import time
import logging
import threading

import grpc

# KLUDGE: is there a way to avoid this when using proto3 generated python?
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


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
        return event_pb2.MachineList(list=[])

    def GetMachine(self, request, context):
        return event_pb2.Machine(
            schema=request.schema,
            initial=[],
            capacity=[],
            transitions={})

    def Dispatch(self, request, context):
        state = event_pb2.State(
            id="foo",
            schema="bar",
            state=[],
            head="head",
            created=None,
            updated=None)
        import IPython
        IPython.embed()
        return event_pb2.EventStatus(state=state, code=0, message="hello")

    def GetEvent(self, request, context):
        return event_pb2.EventList(list=[])

    def GetState(self, request, context):
        return event_pb2.StateList(list=[])


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
