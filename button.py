import pygame
from text import *
from menu import*
pygame.init()

class button(pygame.sprite.Sprite):
	def __init__(self,screen,x,y,width,height,color,rect,text,font="freesansbold.ttf"):
		self.screen = screen
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.font_color = (1,1,1)
		self.rect = rect
		self.text = str(text)

		pygame.draw.rect(self.screen,self.color,self.rect)
		#self.button_text = text(self.screen,100,100,"bruh",self.font_color,32)
	#def draw(self):
		#self.button_text = text(self.screen,350,500,'Graj',self.font_color,32)
		#self.button_text1 = text(self.screen,850,500,'Opcje',self.font_color,32)
	def buttonpress1(self, pos):
	   if pos[0] > 200 and pos [0] < 500:
	   	if pos[1] > 400 and pos [1] < 600:
	   		return True
	   
	def buttonpress2(self,pos):
	   if pos[0] > 1200 and pos[0] < 1500:
	   	if pos[1] > 400 and pos[1] < 600:
	   		return True
	def buttonpress3(self,pos):
	   if pos[0] > 700 and pos [0] < 1000:
	   	if pos[1] > 400 and pos [1] < 600:
	   		return True

	   #if pos[0] > 1200 and pos [0] < 1500:
	   	#if pos[1] > 400 and pos [1] < 600:
	   		#return True

