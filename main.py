#  random dice roll

import pygame, random, time

size = 256  # Size of window/dice
size_of_spots = size // 10
mid = int(size / 2)
left = t = int(size / 4)
right = b = size - left
diecol = (255, 255, 127)
spotcol = (0, 127, 127)

d = pygame.display.set_mode((size, size))
pygame.display.set_caption("Dice Simulator")

while True:
    n = random.randint(1, 6)
    d.fill(diecol)
    if n % 2 == 1:
        pygame.draw.circle(d, spotcol, (mid, mid), size_of_spots)
    if n == 2 or n == 3 or n == 4 or n == 5 or n == 6:
        pygame.draw.circle(d, spotcol, (left, b), size_of_spots)  # left bottom
        pygame.draw.circle(d, spotcol, (right, t), size_of_spots)  # right top

    pygame.display.flip()
    time.sleep(0.2)