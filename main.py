#  random infinite dice roll

from sys import exit
import pygame
import random
import time

size = 256  # Size of window/dice
size_of_spots = size // 10
mid = int(size / 2)
left = t = int(size / 4)
right = b = size - left
rolling_time = random.randrange(4, 12)
print(rolling_time)
dice_color = (255, 255, 127)
spot_color = (0, 127, 127)

d = pygame.display.set_mode((size, size))
pygame.display.set_caption("Dice Simulator")

for i in range(rolling_time):
    n = random.randint(1, 6)
    d.fill(dice_color)
    if n % 2 == 1:
        pygame.draw.circle(d, spotcolor, (mid, mid), size_of_spots)
    if n == 2 or n == 3 or n == 4 or n == 5 or n == 6:
        pygame.draw.circle(d, spotcolor, (left, b), size_of_spots)  # left bottom
        pygame.draw.circle(d, spotcol, (right, t), size_of_spots)  # right top
    if n == 4 or n == 5 or n == 6:
        pygame.draw.circle(d, spotcol, (left, t), size_of_spots)  # left top
        pygame.draw.circle(d, spotcol, (right, b), size_of_spots)  # right bottom
    if n == 6:
        pygame.draw.circle(d, spotcol, (mid, b), size_of_spots)  # middle bottom
        pygame.draw.circle(d, spotcol, (mid, t), size_of_spots)  # middle top

    pygame.display.flip()
    time.sleep(.3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
