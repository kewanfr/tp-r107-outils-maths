import unittest
import exo1


class TestSum(unittest.TestCase):

    def test_division(self):

        self.assertEqual(exo1.division(1, 2), (0, 1), "Should be 0 and 1")
        self.assertEqual(exo1.division(10, 10), (1, 0), "Should be 1 and 0")
        self.assertEqual(exo1.division(10, 5), (2, 0), "Should be 2 and 0")
        self.assertEqual(exo1.division(11, 5), (2, 1), "Should be 2 and 1")
        self.assertEqual(exo1.division(23, 5), (4, 3), "Should be 4 and 3")



if __name__ == '__main__':
    unittest.main()