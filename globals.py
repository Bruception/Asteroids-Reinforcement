
import math

width = 800
height = 600

bullets = []
ships = []
asteroids = []

red = (255, 71, 87)
blue =  (30, 144, 255)
black = (47, 53, 66)
black_dark = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 127, 80)

def bound(entity) :
    if(entity.x - entity.radius >= width) :
        entity.x = -entity.radius
    elif(entity.x <= -entity.radius) :
        entity.x = width + entity.radius

    if(entity.y - entity.radius >= height) :
        entity.y = -entity.radius
    elif(entity.y <= -entity.radius) :
        entity.y = height + entity.radius

def areColliding(entity1, entity2) :
    dx = entity1.x - entity2.x
    dy = entity1.y - entity2.y
    dx *= dx
    dy *= dy

    radiusSquared = (entity1.radius + entity2.radius)
    radiusSquared *= radiusSquared

    return (dx + dy) <= radiusSquared


def distance(entity1, entity2) :
    dx = entity1.x - entity2.x
    dy = entity1.y - entity2.y

    theta = math.atan2(dy, dx)
    theta2 = theta + math.pi

    trueX = entity1.x - (entity1.radius * math.cos(theta))
    trueY = entity1.y - (entity1.radius * math.sin(theta))

    trueX2 = entity2.x - (entity2.radius * math.cos(theta2))
    trueY2 = entity2.y - (entity2.radius * math.sin(theta2))

    dx = trueX - trueX2
    dy = trueY - trueY2

    dx2 = dx * dx
    dy2 = dy * dy

    return math.sqrt(dx2 + dy2), dx, dy

def filterDelete(entities) :
    return list(filter(lambda e : not e.delete, entities))