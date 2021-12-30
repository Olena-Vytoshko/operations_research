from typing import List


def filter_result(queens: List[List[int]]) -> List[List[int]]:
    def filter_rotations(indx: int, result: List[List[int]]) -> None:
        rot_queen = rotate_board(result[indx])
        for i in range(2):
            if rot_queen in result and len(result) > 1:
                result.remove(rot_queen)
            rot_queen = rotate_board(rot_queen)
        return None

    def rotate_board(queen: List[int]) -> List[int]:
        res = []
        for i in range(len(queen)):
            res.append(len(queen) - 1 - queen[i])
        return res

    def filter_reflection(indx: int, result: List[List[int]]) -> None:
        temp = result[indx][::-1]
        if temp in result:
            result.remove(temp)
        return None

    def filter_result_inner(indx: int, result: List[List[int]]) -> List[List[int]]:
        if indx >= len(result):
            return result
        filter_rotations(indx, result)
        if indx >= len(result):
            return result
        filter_reflection(indx, result)
        return filter_result_inner(indx + 1, result)

    return filter_result_inner(0, queens.copy())
