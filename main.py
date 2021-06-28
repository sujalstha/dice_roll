#  random dice roll

import pygame, random, time

size = 256  # Size of window/dice
size_of_spots = size // 10
mid = int(size / 2)
left = t = int(size / 4)
right = b = size - left
rolling = 12
diecol = (255, 255, 127)
spotcol = (0, 127, 127)

d = pygame.display.set_mode((size, size))
pygame.display.set_caption("Dice Simulator")

for i in range(rolling):
    n = random.randint(1, 6)
    d.fill(diecol)