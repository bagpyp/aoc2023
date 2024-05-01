import numpy as np

from config import days
from model import Particle
from util import get_day


def solution(input, part=1, xymin=2e14, xymax=4e14):
    if part == 2:
        # part 2 here
        return 0
    # part 1 here
    acc = 0
    positions, velocities = parse_input(input)
    particles = [Particle(*p, *v) for p, v in zip(positions, velocities)]
    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            p1, p2 = particles[i], particles[j]
            t, s = p1.intersect_when(p2)
            if t > 0 and s > 0:
                p1_t = p1.evaluate(t)
                p2_s = p2.evaluate(s)
                if np.allclose(p1_t, p2_s):
                    if xymin <= p1_t[0] <= xymax:
                        if xymin <= p1_t[1] <= xymax:
                            acc += 1
    return acc


def parse_input(input):
    positions, velocities = [], []
    for line in input.splitlines():
        positions.append([int(num) for num in line.split(" @ ")[0].split(", ")])
        velocities.append([int(num) for num in line.split(" @ ")[1].split(", ")])
    return positions, velocities


if __name__ == "__main__":
    with open(f"{days[get_day(__file__)]}/input") as f:
        input = f.read()

    print(solution(input))
    print(solution(input, part=2))
