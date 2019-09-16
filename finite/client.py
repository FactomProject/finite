""" eventstore client """
from __future__ import print_function
import os
import sys
import logging

import grpc
# KLUDGE: alter path to import proto3 generated python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # noqa
import finite.event_pb2 as event_pb2
import finite.event_pb2_grpc as event_pb2_grpc


def TestClient():
    channel = grpc.insecure_channel('localhost:50051')
    stub = event_pb2_grpc.EventStoreStub(channel)
    return stub


def run():
    # FIXME: turn into unit tests
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = event_pb2_grpc.EventStoreStub(channel)

        response = stub.Status(event_pb2.Ping(nonce="foobar"))
        print("Status: \n  nonce:%s \n  code:%i" %
              (response.nonce, response.code))

        query = event_pb2.MachineQuery()
        response = stub.ListMachines(query)
        print("ListMachines: %s" % response.list)

        query = event_pb2.Query(schema="foo", id="bar", uuid="baz")
        response = stub.GetMachine(query)
        print("GetMachine: %s" % response.schema)

        cmd = event_pb2.Command(
            id="bar",
            schema="baz",
            action="",
            multiple=1,
            payload=None,
            state=[])
        response = stub.Dispatch(cmd)
        print("Dispatch: \n  message: %s \n  code: %s" %
              (response.message, response.code))

        query = event_pb2.Query(schema="foo", id="bar", uuid="baz")
        response = stub.GetEvent(query)
        print("GetEvent: %s" % response.list)

        query = event_pb2.Query(schema="foo", id="bar", uuid="baz")
        response = stub.GetState(query)
        print("GetState: %s" % response.list)


if __name__ == '__main__':
    logging.basicConfig()
    run()
