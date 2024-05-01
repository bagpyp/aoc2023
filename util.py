import os

from typing import Iterable, TypeVar

T = TypeVar("T")


def get_day(file):
    parent_dir = os.path.basename(os.path.dirname(os.path.abspath(file)))
    return int(parent_dir.split("-")[0])


def pad_array(arr: Iterable[Iterable[T]], padding: T) -> list[list[T]]:
    arr = list(list(row) for row in arr)
    if not arr or not arr[0]:
        return [[padding]]
    M = len(arr)
    N = max(len(row) for row in arr)
    padded_arr = [[padding for _ in range(M + 2)] for _ in range(N + 2)]

    for s_row, d_row in zip(arr, padded_arr[1:-1]):
        d_row[1 : int(len(s_row) + 1)] = s_row

    return padded_arr


def array_neighbors(
    arr: list[list[T]], pos_start: tuple[int, int], span: int = 1
) -> dict[tuple[int, int], T]:
    if not arr or not arr[0]:
        return dict()
    M = len(arr)
    N = max(len(row) for row in arr)
    a, b = pos_start
    if (1 <= a <= M - 2) and (1 <= b <= N - 2) and (1 <= b + span <= N - 1):
        indices = [(a - 1, b - 1 + i) for i in range(span + 2)]
        indices.append((a, b - 1))
        indices.append((a, b + span))
        indices.extend((a + 1, b - 1 + i) for i in range(span + 2))
        neighbors = {idx: arr[idx[0]][idx[1]] for idx in indices}
        return neighbors
    else:
        raise IndexError
