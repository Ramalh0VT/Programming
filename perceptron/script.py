import pygame
from pygame import *

pygame.init()

screen_w = 864
screen_h = 936

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('AI Flappy Bird')

bg = pygame.image.load('img/bg.png')
ground = pygame.image.load('img/ground.png')

running = True

ground_scroll = 0
scroll_speed = 4

while running:
	screen.blit(ground, (ground_scroll,768))
	screen.blit(bg, (0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False	
	pygame.display.update()
pygame.quit()
