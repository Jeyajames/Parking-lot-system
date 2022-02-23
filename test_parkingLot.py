import unittest

from main import allocateParkingSlot

class TestParkingLot(unittest.TestCase):
    def test_something(self):

        allocateParkingSlot()
        self.assertEqual(True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
