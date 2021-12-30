from typing import List


def is_safe(col: int, queens: List[int]) -> bool:
    """
    Checks possibility to add a queen in the column
    :param col: column that is needed to check
    :param queens: list with contains all queens in the board
    :return: Bool value represents the result of the checking
    """
    row = len(queens)
    queens_with_row = zip(range(row - 1, -1, -1), queens)
    return all((col != c and abs(col - c) != row - r) for (r, c) in queens_with_row)


def search_queens(n: int) -> List[List[int]]:
    """
    The main function for searching all possible options of queens placing in the board of custom size.
    The way to solve this problem is to place a queen to each row.
    :param n: size of board
    :return: list of list which contains the column's index for each row that are possible for queen staying.
    """

    def placeQueens(k: int):
        """
        Inner function for resolve the tasks with using recursive approach.
        :param k: current number of places for queen that were founded
        """
        if k == 0:
            return [[]]
        res = []
        for col, queens in (
                (col, queens)
                for queens in placeQueens(k - 1)
                for col in range(n)
                if is_safe(col, queens)
        ):
            res.append([col, *queens])
        return res

    return placeQueens(n)
