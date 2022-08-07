import pygame
import os

pygame.init()

class text(pygame.sprite.Sprite):
	def __init__(self,screen,x,y,text,color,size,font="slkscre-webfont.ttf"):
		self.screen = screen
		self.x = x
		self.y = y
		self.text = str(text)
		self.color = color
		self.size = size
		self.font = font

		self.true_font = pygame.font.Font(self.font, self.size)
		self.true_text = self.true_font.render(self.text,True,self.color)
		self.text_rect = self.true_text.get_rect()
		self.text_rect.topleft = (self.x,self.y)
		self.screen.blit(self.true_text,self.text_rect)






'''font = pygame.font.Font("freesansbold.ttf", 32)
				self.text = self.font.render("Zadanie:",True,self.font_color)
		self.text_rect = self.text.get_rect()
		self.text_rect.center = (self.width/2,self.height/2)
		self.screen.blit(self.text, self.text_rect)'''
