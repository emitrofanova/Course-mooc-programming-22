# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()
n = 0 #iteration counter
num_robots = random.randint(10, 20) #amount of robots
x = [random.randint(0, 640 - robot.get_width()) for i in range(num_robots)] #width
time = [random.randint(0, 1000) for i in range(num_robots)] #random time of appearance
robots = [] #all robots that have already appeared
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    #the robot appears if the robot is supposed to appear in this iteration
    for i in range(num_robots):
        if n == time[i]:
            robots.append([x[i], -robot.get_height()]) #append a new robot with (x,y) coordinates
    n += 1
    #movement for each robot
    for rob in robots:
        if rob[1]+robot.get_height() < 480:
            rob[1] += 1
        if rob[1]+robot.get_height() == 480:
            if rob[0] <= (320 - robot.get_width()/2):
                rob[0] -= 1
            elif rob[0] > (320 - robot.get_width()/2):
                rob[0] += 1
        window.blit(robot, (rob[0], rob[1]))
        
    pygame.display.flip()
    clock.tick(60)
