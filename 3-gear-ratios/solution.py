import re
from collections import defaultdict

from config import days
from util import get_day, pad_array, array_neighbors


def solution(input, part=1):
    acc = 0
    gears = defaultdict(list)
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
            if part == 1:
                neighbors = neighbors.values()
                if not all(n == "." for n in neighbors):
                    acc += int(num)
            else:
                for pos, val in neighbors.items():
                    if val == "*":
                        gears[pos].append(int(num))
    if part == 1:
        return acc
    else:
        for pos, nums in gears.items():
            if len(nums) == 2:
                acc += nums[0] * nums[1]
        return acc


if __name__ == "__main__":
    with open(f"{days[get_day(__file__)]}/input") as f:
        input = f.read()

    print(solution(input))
    print(solution(input, part=2))
