# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

to_right = False
to_left = False
points = 0

robot = pygame.image.load("robot.png")
rock_img = pygame.image.load("rock.png")

x_robot = 320 - robot.get_width()
y_robot = 480 - robot.get_height()

clock = pygame.time.Clock()
n = 0 #iteration counter
num_rocks = random.randint(10, 20) #amount of rocks
x_rock = [random.randint(0, 640 - rock_img.get_width()) for i in range(num_rocks)] #width for each rock
time = [random.randint(0, 2000) for i in range(num_rocks)] #random time of appearance
rocks = [] #all rocks that have already appeared

while True:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_left = True
                if event.key == pygame.K_RIGHT:
                    to_right = True
                
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    to_left = False
                if event.key == pygame.K_RIGHT:
                    to_right = False

    if to_right and x_robot < 640 - robot.get_width():
        x_robot += 2
    if to_left and x_robot > 0:
        x_robot -= 2

    #the rock appears if the rock is supposed to appear in this iteration
    for i in range(num_rocks):
        if n == time[i]:
            rocks.append([x_rock[i], -rock_img.get_height()]) #append a new rock with (x,y) coordinates
    n += 1
    #movement for each rock
    for rock in rocks:
        if rock[1]+rock_img.get_height() < 480:
            rock[1] += 1
        if (x_robot <= rock[0] <= x_robot + robot.get_width() or x_robot <= rock[0] + rock_img.get_width() <= x_robot + robot.get_width()) and y_robot <= rock[1] + rock_img.get_height() <= y_robot + robot.get_height():
            rock[0] = 650
            rock[1] = 490
            points += 1
        if rock[1] + rock_img.get_height() == 480:
            num_rocks = 0
            rocks = []
        window.blit(rock_img, (rock[0], rock[1]))
    
    score_font = pygame.font.SysFont("Arial", 24)
    text = score_font.render(f"Points: {points}", True, (255, 0, 0))
    window.blit(text, (520, 30))
    window.blit(robot, (x_robot, y_robot))
    pygame.display.flip()
    clock.tick(60)
