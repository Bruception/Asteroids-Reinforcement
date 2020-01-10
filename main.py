
import pygame as pg
import color
from neuralnetwork import NeuralNetwork

nn = NeuralNetwork([(1, 10), (10, 9), (9, 9), (9, 9), (9, 4)])
print(nn.feedforward([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]))

colors = color.colors

pg.init()
font = pg.font.Font(None, 30)
clock = pg.time.Clock()

screen = pg.display.set_mode([800, 600])
pg.display.set_caption("Asteroids!")

running = True

while (running) :
    for event in pg.event.get() :
        if (event.type == pg.QUIT) :
            running = False

    screen.fill(colors["black"])
    nn.draw(screen)
    fps = font.render(str(int(clock.get_fps())), True, pg.Color('white'))
    screen.blit(fps, (50, 50))
    clock.tick(30)

    pg.display.flip()

pg.quit()