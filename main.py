import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Platformer")

BG_COLOR = (255, 255, 255)
WIDHT, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDHT, HEIGHT))

# name is color of our bg


def get_background(name):
    image = pygame.image.load(join("assets", "background", name))
    _, _, widht, height = image.get_rect()
    tiles = []

    for i in range(WIDHT // widht + 1):
        for j in range(HEIGHT // height + 1):


def main(window):
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.typee == pygame.QUIT:
                run = False
                break

    pygame.quit()
    quit()


# Only call the main function if we run this file directly
if __name__ == "__main__":
    main(window)
