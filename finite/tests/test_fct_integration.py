
import unittest

from finite.storage import new_uuid, encode
from finite.storage.factom import keyval as kv


# TODO: precompute chainid rather than just creating every time
chain0 = "8ccb2446cfaa7915863cf5b3fad79653dfd92ce896f424c3bd635e0c88f20503"


# NOTE: currently this test is somewhat inconsistent
# Chainhead is created during first run & subsequent runs will pass
class FactomStorageTestCase(unittest.TestCase):

    def setUp(self):
        self.schema = 'testing_schema'
        self.stor = kv.initialize(chain0, self.schema)

    def tearDown(self):
        pass

    # TODO: test interacting w/ walletd & factomd using included lib

    def test_entry_creation(self):
        f = kv.factomd
        w = kv.walletd

        r = f.factoid_balance()
        print(r)

        r = f.entry_credit_balance()
        print(r)

        r = f.entry_credit_rate()
        print(r)
        rate = r['rate']

        r = f.entry_credit_balance()
        print(r)

        print(f.fct_address, f.ec_address)

        r = w.fct_to_ec(f, 50 * rate, fct_address=f.fct_address,
                        ec_address=f.ec_address)
        print(r)

        r = f.entry_credit_balance()
        print(r)

        # REVIEW: Perhaps we always leave the chain hardcoded?
        try:
            key = b'test'
            r = w.new_chain(f, [b'random', b'chain', b'id', key],
                            b'chain_content', ec_address=f.ec_address)

            self.assertEqual(chain0, r['chainid'])
            entry0 = r['entryhash']
            print({"chain": chain0, "entryhash": entry0})
            sleep(2)
        except Exception as x:
            r = f.chain_head(chain0)

        print(r)

        key = b'NTk0ZjBhZDctY2U0NS00NzhmLWIyN2ItODhhNDEzMGFjZGYy'
        r = w.new_entry(f, chain0, [b'random', b'entry', key],
                        b'entry_content', ec_address=f.ec_address)

        r = f.read_chain(chain0)
        print("\nCHAIN: %s\n" % chain0)
        for e in r:
            print(e)

        # print(r)
        #import IPython ; IPython.embed()


if __name__ == '__main__':
    unittest.main()
