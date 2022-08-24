# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

robot_x = random.randint(0, 640 - robot.get_width())
robot_y = random.randint(0, 480 - robot.get_height())
target_x = 0
target_y = 0
window.blit(robot, (robot_x, robot_y))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            target_x = event.pos[0]
            target_y = event.pos[1]

        if event.type == pygame.QUIT:
            exit(0)

    if robot_x <= target_x <= robot_x + robot.get_width() and robot_y <= target_y <= robot_y + robot.get_height():
        robot_x = random.randint(0, 640 - robot.get_width())
        robot_y = random.randint(0, 480 - robot.get_height())


    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)
