import unittest
from finite.server import TestServer
from finite.client import TestClient, event_pb2


class TestCase(unittest.TestCase):

    def setUp(self):
        self.server = TestServer()
        self.server.start()

    def tearDown(self):
        self.server.join()

    def test_grpc_api(self):
        stub = TestClient()
        response = stub.Status(event_pb2.Ping(nonce="foobar"))
        print("Status: \n  nonce:%s \n  code:%i" % (response.nonce, response.code))

        query = event_pb2.MachineQuery()
        response = stub.ListMachines(query)
        print("ListMachines: %s" % response.list)

        query = event_pb2.Query(schema="foo", id="bar", uuid="baz")
        response = stub.GetMachine(query)
        print("GetMachine: %s" % response.schema)

        cmd = event_pb2.Command(id="bar", schema="baz", action=["act0"], multiple=1, payload=None, state=[])
        response = stub.Dispatch(cmd)
        print("Dispatch: \n  message: %s \n  code: %s" % (response.message, response.code))

        query = event_pb2.Query(schema="foo", id="bar", uuid="baz")
        response = stub.GetEvent(query)
        print("GetEvent: %s" % response.list)

        query = event_pb2.Query(schema="foo", id="bar", uuid="baz")
        response = stub.GetState(query)
        print("GetState: %s" % response.list)

if __name__ == '__main__':
    unittest.main()
