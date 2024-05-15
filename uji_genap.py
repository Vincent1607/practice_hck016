import unittest
from genap_app import CheckGenap

class TestCheckGenap(unittest.TestCase)Check Genap
    def test_CheckGenap_succes1(self):
        num = 10
        result = CheckGenap(num)
        self.assertEqual(result, True)
    def testCheckGenap_success2(self):
        self.assertEqual(CheckGenap(1), False)

if __name__ == '__main__':
    unittest.main(verbosity=2)