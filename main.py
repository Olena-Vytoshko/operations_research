from model import nqueens, utilities
from view.chessboard import draw_chessboard
from view.gui import draw_gui


def solve(count_of_queens: int, path_to_folder: str, filtering: bool):
    res = nqueens.search_queens(count_of_queens) if not filtering else \
        utilities.filter_result(nqueens.search_queens(count_of_queens))
    draw_chessboard.draw_chessboards(res, path_to_folder, f"result for N={count_of_queens}")


if __name__ == '__main__':
    draw_gui.draw_gui(solve)
