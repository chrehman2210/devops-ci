import unittest
from Dec2Hex import dec_to_hex

class TestDecToHex(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(dec_to_hex(15), "F")

    def test_zero(self):
        self.assertEqual(dec_to_hex(0), "0")

    def test_large_number(self):
        self.assertEqual(dec_to_hex(255), "FF")

    def test_negative_integer(self):
        with self.assertRaises(ValueError):
            dec_to_hex(-5)

if __name__ == "__main__":
    unittest.main()
