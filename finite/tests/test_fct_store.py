import unittest
from finite.storage import new_uuid
from finite.storage.factom import keyval as kv


class FactomStorageTestCase(unittest.TestCase):

    def setUp(self):
        self.chain = new_uuid()
        self.oid = new_uuid()
        self.schema = 'testing_schema'
        kv.initialize(self.chain, self.schema)

    def tearDown(self):
        pass

    def test_events(self):
        """ test get/set event """
        parent = "__PARENT__"
        event_id = new_uuid()
        new_state = [0, 0, 0]

        commands = (('foo', 1), ('bar', 2))
        r = kv.append_event(self.chain,
                            self.schema,
                            self.oid,
                            parent,
                            event_id,
                            commands,
                            new_state,
                            {"hello": "world"})
        self.assertIsNotNone(r)

        e = kv.get_event(self.chain, self.schema, self.oid, event_id)
        self.assertIsNotNone(e)

        self.assertEqual(e[2], new_state)

    def test_state(self):
        """ test get/set state """

        r = kv.get_state(self.chain, self.schema, self.oid)
        self.assertIsNone(kv.get_state(self.chain, self.schema, self.oid))
        event_id = new_uuid()

        new_state = [1, 1, 1]
        r = kv.set_state(
            self.chain,
            self.schema,
            self.oid,
            event_id,
            new_state)
        self.assertTrue(r)

        r = kv.get_state(self.chain, self.schema, self.oid)
        self.assertIsNotNone(r)
        self.assertEqual(r[0], event_id)
        self.assertEqual(r[1], new_state)


if __name__ == '__main__':
    unittest.main()
