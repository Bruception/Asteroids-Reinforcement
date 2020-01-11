
width = 800
height = 600

bullets = []
ships = []

red = (255, 71, 87)
blue =  (30, 144, 255)
black = (47, 53, 66)
black_dark = (0, 0, 0)
white = (255, 255, 255)


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
