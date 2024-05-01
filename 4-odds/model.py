import numpy as np


class Particle:
    def __init__(self, x=0, y=0, z=0, vx=0, vy=0, vz=0, collapse=True):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        if collapse:
            self.z = 0
            self.vz = 0

    def pos(self):
        return np.array([self.x, self.y, self.z])

    def vel(self):
        return np.array([self.vx, self.vy, self.vz])

    def __repr__(self):
        return f"{self.x}, {self.y}, {self.z} @ {self.vx}, {self.vy}, {self.vz}"

    def intersect_when(self, other):
        a = np.vstack(
            [
                self.vel(),
                -1 * other.vel(),
            ]
        ).T

        b = other.pos() - self.pos()

        return np.linalg.lstsq(a, b, rcond=None)[0]

    def evaluate(self, t):
        return self.pos() + self.vel() * t


if __name__ == "__main__":

    A = Particle(19, 13, 30, -2, 1, -2)
    B = Particle(18, 19, 22, -1, -1, -2)
    t, s = A.intersect_when(B)
    ax, ay, az = A.evaluate(t)
