import time
import unittest
from finite.storage import new_uuid
from finite.storage.factom import keyval as kv
from factom_sim import Factomd, FactomWalletd

CHAIN = 'foo'  # fiendly name for chain
SCHEMA = 'bar'
OID = b'NTk0ZjBhZDctY2U0NS00NzhmLWIyN2ItODhhNDEzMGFjZGYy'
BLKTIME=15 #sec
# toggle to run tests against external services

def wait_blocks(i):
    time.sleep(i*BLKTIME)

class TestFactomStorage(unittest.TestCase):
    fnode = Factomd()
    wallet = FactomWalletd()
    stor = None # datastore
    EXTERNAL=False # test using an external factomd/factom-walletd

    @classmethod
    def setUpClass(cls):
        if not cls.EXTERNAL:
            cls.fnode.start()
            cls.wallet.start()
            wait_blocks(1)

        cls.stor = kv.initialize(CHAIN, SCHEMA)

        if cls.stor.chainhead is None:
            time.sleep(2)
            cls.stor.create_chain()

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        if not cls.EXTERNAL:
            cls.fnode.join()
            cls.wallet.join()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_chain(self):
        #self.assertIsNotNone(self.stor.chainid)
        self.assertIsNotNone(None)

    def test_events(self):
        """ test get/set event """
        parent = "__PARENT__"
        event_id = b'eTk0ZjBhZDctY2U0NS00NzhmLWIyN2ItODhhNDEzMGFjZGYy'

        new_state = [0, 0, 0]

        commands = (('foo', 1), ('bar', 2))
        r = kv.append_event(CHAIN,
                            SCHEMA,
                            OID,
                            parent,
                            event_id,
                            commands,
                            new_state,
                            {"hello": "world"})
        self.assertIsNotNone(r)

        wait_blocks(1)

        e = kv.get_event(CHAIN, SCHEMA, OID, event_id)
        self.assertIsNotNone(e)
        self.assertEqual(e[2], new_state)

        r = kv.find_event(CHAIN, SCHEMA, OID, event_id)
        self.assertIsNotNone(r)

    def test_state(self):
        """ test get/set state """

        r = kv.get_state(CHAIN, SCHEMA, OID)
        self.assertIsNone(kv.get_state(CHAIN, SCHEMA, OID))
        event_id = new_uuid()

        new_state = [1, 1, 1]
        r = kv.set_state(
            CHAIN,
            SCHEMA,
            OID,
            event_id,
            new_state)
        self.assertTrue(r)

        r = kv.get_state(CHAIN, SCHEMA, OID)
        self.assertIsNotNone(r)
        self.assertEqual(r[0], event_id)
        self.assertEqual(r[1], new_state)


if __name__ == '__main__':
    unittest.main()
