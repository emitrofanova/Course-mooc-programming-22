# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
width = robot.get_width()
height = robot.get_height()
n = 1
while n <= 1000:
    w = random.randint(0, 640 - width)
    h = random.randint(0, 480 - height)
    window.blit(robot, (w, h))
    n += 1
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

