from config import days


def solution(input: str, part=1):

    if part == 2:
        acc = 0
        for line in input.splitlines():
            numbers = extract_numbers(line)
            numbers = [
                {
                    "one": "1",
                    "two": "2",
                    "three": "3",
                    "four": "4",
                    "five": "5",
                    "six": "6",
                    "seven": "7",
                    "eight": "8",
                    "nine": "9",
                    # "zero": "0",
                }.get(r, r)
                for r in numbers
            ]
            acc += int("".join(numbers))
        return acc

    acc = 0
    for line in input.split("\n"):
        digits = extract_digits(line)
        acc += int("".join(digits))
    return acc


def extract_digits(line: str) -> list[str]:
    res = []
    for char in line:
        if char in "1234567890":
            res.append(char)
            break
    for char in line[-1::-1]:
        if char in "1234567890":
            res.append(char)
            break
    return res


def extract_numbers(line: str) -> list[str]:
    res = ["", ""]
    tokens = list("1234567890") + [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        # "zero",
    ]
    first_position, second_position = 9999, 9999
    for token in tokens:
        position = line.find(token)
        if position != -1 and position <= first_position:
            first_position = position
            res[0] = line[position : position + len(token)]
    for token in tokens:
        position = line[-1::-1].find(token[-1::-1])
        if position != -1 and position <= second_position:
            second_position = position
            res[1] = line[-1::-1][position : position + len(token)][-1::-1]
    print(f"({res}, '{line}'),")
    return res


if __name__ == "__main__":

    with open(f"{days[0]}/input") as f:
        input = f.read()

    print(solution(input))
    print(solution(input, part=2))
