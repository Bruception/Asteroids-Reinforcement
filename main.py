
import pygame as pg
import color
from neuralnetwork import NeuralNetwork

nn = NeuralNetwork([(1, 3), (4, 9), (9, 9), (9, 9), (9, 4)])

colors = color.colors

pg.init()

screen = pg.display.set_mode([800, 600])
pg.display.set_caption("Asteroids!")

running = True

while (running) :
    for event in pg.event.get() :
        if (event.type == pg.QUIT) :
            running = False

    screen.fill(colors["black"])
    nn.draw(screen)

    pg.display.update()

pg.quit()