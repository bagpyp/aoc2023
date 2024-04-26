import re

from config import days


def solution(input, part=1):
    games = [Game.parse(line) for line in input.splitlines()]

    if part == 2:
        return sum([game.power() for game in games])

    possible_games = [game for game in games if game.is_possible()]
    return sum([pg.id for pg in possible_games])


class Round:
    red: int
    blue: int
    green: int

    def __init__(self, red: int = 0, blue: int = 0, green: int = 0):
        self.red = red
        self.blue = blue
        self.green = green

    @staticmethod
    def parse(round_line: str):
        round_data = {
            match.group(2): int(match.group(1))
            for match in re.finditer(r"(\d+) (red|blue|green)", round_line)
        }
        return Round(**round_data)

    def is_possible(self):
        return self.red <= 12 and self.green <= 13 and self.blue <= 14


class Game:
    id: int
    rounds: [Round]

    def __init__(self, id: int, rounds: [Round]):
        self.id = id
        self.rounds = rounds

    @staticmethod
    def parse(game_line: str):
        id = int(re.search("Game ([0-9]+)", game_line).group(1))
        rounds = [
            Round.parse(round_line)
            for round_line in game_line.split(": ")[1].split("; ")
        ]
        return Game(id, rounds)

    def is_possible(self):
        return all([r.is_possible() for r in self.rounds])

    def min_set(self):
        res = []
        for color in ["red", "green", "blue"]:
            res.append(max([getattr(r, color) for r in self.rounds]))

        return res

    def power(self):
        min_sets = self.min_set()
        return product(min_sets)


def product(nums):
    result = 1
    for number in nums:
        result *= number
    return result


if __name__ == "__main__":
    with open(f"{days[1]}/input") as f:
        input = f.read()

    print(solution(input))
    print(solution(input, part=2))
