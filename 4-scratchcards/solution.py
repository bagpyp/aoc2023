from config import days
from util import get_day


def solution(input, part=1):
    if part == 2:
        # part 2 here
        return 0

    acc = 0
    for line in input.splitlines():
        points = 0
        want, have = [
            [int(j) for j in line.split(" | ")[i].strip().split()] for i in (0, 1)
        ]
        for h in have:
            for w in want:
                if h == w:
                    points = 1 if points == 0 else points * 2
        acc += points
    return acc


if __name__ == "__main__":
    with open(f"{days[get_day(__file__)]}/input") as f:
        input = f.read()

    print(solution(input))
    print(solution(input, part=2))
