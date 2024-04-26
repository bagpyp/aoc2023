from config import days


def solution(input, part=1):
    if part == 2:
        # part 2 here
        return 0
    # part 1 here
    return 0


if __name__ == "__main__":
    with open(f"{days[0]}/input") as f:
        input = f.read()

    print(solution(input))
    print(solution(input, part=2))
