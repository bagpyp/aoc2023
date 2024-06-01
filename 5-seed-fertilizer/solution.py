from config import days
from util import get_day


def solution(input, part=1):
    data = parse_input(input)

    if part == 2:
        # part 2 here
        return 0
    # part 1 here
    return 0


def parse_input(input):
    pieces = input.split("\n\n")

    seeds = pieces[0].split(": ")[1]
    seeds = [int(seed) for seed in seeds.split(" ")]
    data = dict(seeds=seeds)

    for piece in pieces[1:]:
        lines = piece.splitlines()
        map_type = lines[0].split(" map:")[0]
        data[map_type] = []  # should this be list()?
        map_data = lines[1:]
        for line in map_data:
            nums = [int(i) for i in line.split(" ")]
            data.get(map_type).append(
                {
                    "source-start": nums[1],
                    "destination-start": nums[0],
                    "range-length": nums[2],
                }
            )
    return data


if __name__ == "__main__":
    with open(f"{days[get_day(__file__)]}/input") as f:
        input = f.read()

    print(solution(input))
    print(solution(input, part=2))
