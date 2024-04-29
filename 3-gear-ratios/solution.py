import re

from config import days
from util import get_day, pad_array, array_neighbors


def solution(input, part=1):
    acc = 0
    if part == 2:
        # part 2 here
        return 0
    # part 1 here
    arr = input.splitlines()
    M = len(arr)
    N = len(arr[0])
    p_arr = pad_array(arr, padding=".")
    for i in range(1, M + 1):
        row = "".join(p_arr[i])
        for match in re.finditer(r"\d+", row):
            num = match.group()
            pos = (i, match.span()[0])
            neighbors = array_neighbors(p_arr, pos, span=len(num))
            if not all(n == "." for n in neighbors):
                acc += int(num)
    return acc


if __name__ == "__main__":
    with open(f"{days[get_day(__file__)]}/input") as f:
        input = f.read()

    print(solution(input))
    print(solution(input, part=2))
