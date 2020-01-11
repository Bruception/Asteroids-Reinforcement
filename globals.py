
bullets = []
ships = []

red = (255, 71, 87)
blue =  (30, 144, 255)
black = (47, 53, 66)
black_dark = (0, 0, 0)
white = (255, 255, 255)


def bound(entity) :
    if(entity.x - entity.radius >= 800) :
        entity.x = -entity.radius
    elif(entity.x <= -entity.radius) :
        entity.x = 800 + entity.radius

    if(entity.y - entity.radius >= 600) :
        entity.y = -entity.radius
    elif(entity.y <= -entity.radius) :
        entity.y = 600 + entity.radius
        