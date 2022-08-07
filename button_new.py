import pygame
from text import *
from menu import*
from unit import *
przycisk1 = pygame.Rect(200, 400, 300, 200)
pygame.init()
class button2(pygame.sprite.Sprite):
	def __init__(self,screen,x,y,width,height,color,rect,font="freesansbold.ttf"):
		self.screen = screen
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.font_color = (1,1,1)
		self.rect = rect
		pygame.draw.rect(self.screen,self.color,przycisk1)
	def pressbutton1(self, pos):
		if mouse.rect.colliderect(przycisk1):
			return True