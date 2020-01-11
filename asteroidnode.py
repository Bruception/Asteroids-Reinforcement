
import globals as g
import math

class AsteroidNode :

    def __init__(self, ship, asteroid) :
        self.dx = ship.x - asteroid.x
        self.dy = ship.y - asteroid.y

        angle = math.atan2(self.dy, self.dx)

        self.dx += asteroid.radius * math.cos(angle)
        self.dy += asteroid.radius * math.sin(angle)

        self.angle = asteroid.angle
        self.priority = g.distance(ship, asteroid)

    def __lt__(self, other) :
        return self.priority < other.priority