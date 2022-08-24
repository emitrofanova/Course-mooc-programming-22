# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
width = robot.get_width()
height = robot.get_height()
w = 1
h = 1 
n = 1
while h <= 10:
    while w <= 10:
        window.blit(robot, (40 * w + width/5 * n, 70 + 20 * h))
        w += 1
    pygame.display.flip()
    n += 1
    w = 1
    h += 1
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

