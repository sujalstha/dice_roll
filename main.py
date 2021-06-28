#  random dice roll

import pygame, random, time

size = 256  # Size of window/dice
size_of_spots = size // 10

d = pygame.display.set_mode((size, size))
pygame.display.set_caption("Dice Simulator")