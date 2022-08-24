# WRITE YOUR SOLUTION HERE:
import pygame
import datetime
import math

pygame.init()
display = pygame.display.set_mode((640, 480))
display.fill((0, 0, 0))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.draw.circle(display, (255, 0, 0), (320, 240), 200)
    pygame.draw.circle(display, (0, 0, 0), (320, 240), 195)
    pygame.draw.circle(display, (255, 0, 0), (320, 240), 10)

    time = datetime.datetime.now()
    hours = int(time.strftime("%H"))
    minutes = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))

    pygame.display.set_caption(' '*80 + time.strftime("%H:%M:%S"))

    s_angle = 3*math.pi/2 + (2*math.pi/60)*sec
    s_x = 320+math.cos(s_angle)*180
    s_y = 240+math.sin(s_angle)*180
    pygame.draw.line(display, (0, 0, 255), (320, 240), (s_x, s_y), 1) #sec

    m_angle = 3*math.pi/2 + (2*math.pi/3600) * (60 * minutes + sec)
    m_x = 320+math.cos(m_angle)*170
    m_y = 240+math.sin(m_angle)*170
    pygame.draw.line(display, (0, 0, 255), (320, 240), (m_x, m_y), 3) #min
    
    h_angle = 3*math.pi/2 + (2*math.pi/43200) * ((60 * hours + minutes)* 60 + sec)
    h_x = 320+math.cos(h_angle)*140
    h_y = 240+math.sin(h_angle)*140
    pygame.draw.line(display, (0, 0, 255), (320, 240), (h_x, h_y), 5) #hours
    
    pygame.display.flip()
    
    clock.tick(30)
