import os
import json
import unittest
import finite.pflow
from finite.storage.factom import Storage


class OctoeTestCase(unittest.TestCase):

    def setUp(self):
        finite.pflow.set_provider(Storage)
        self.xmlfile = os.path.dirname(os.path.abspath(__file__)
            ) + "/../examples/octoe.pflow"

    def tearDown(self):
        pass

    def test_load_subnets(self):
        flow, err = finite.pflow.load_file(self.xmlfile)
        self.assertIsNone(err)
        m = flow.to_module()
        self.assertEqual(m.Machine.__class__, type)
        #print(flow)

if __name__ == '__main__':
    unittest.main()
