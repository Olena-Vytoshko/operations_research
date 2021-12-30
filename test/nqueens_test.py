import unittest
from model import nqueens


class NQueensTest(unittest.TestCase):

    def test_is_safe(self):
        """
        Tests the `is_safe` function.
        The are some comments for each test. The comments represent the board with the marks:
            Q - the queen
            * - empty field
            ! - The field that is checked for the possibility of placing the queen
        """

        # Q
        # !
        # The vertical intersection case. Must be False
        self.assertFalse(nqueens.is_safe(0, [0]))

        # Q *
        # * !
        # The diagonal intersection case. Must be False
        self.assertFalse(nqueens.is_safe(1, [0]))

        # Q * *
        # * * !
        # The non-intersection case. Must be True
        self.assertTrue(nqueens.is_safe(2, [0]))

        # * * * Q
        # Q * * *
        # * * * !
        # Must be False
        self.assertFalse(nqueens.is_safe(3, [0, 3]))

        # * Q * *
        # * * * Q
        # Q * * *
        # ! ! ! !
        # Test all possible columns in the 4th row
        self.assertTrue(nqueens.is_safe(2, [0, 3, 1]))
        self.assertFalse(nqueens.is_safe(0, [0, 3, 1]))
        self.assertFalse(nqueens.is_safe(1, [0, 3, 1]))
        self.assertFalse(nqueens.is_safe(3, [0, 3, 1]))


if __name__ == '__main__':
    unittest.main()
