import pygame
from text import *
from button import *
from unit import *
from button_new import*
przycisk1 = pygame.Rect(200, 400, 300, 200)
przycisk2 = pygame.Rect(700, 400, 300, 200)
przycisk3 = pygame.Rect(1200,400,300,200)

class MENU4():
	def __init__(self,screen,screen_size,image,color,font_color,image2):
		self.x = 0
		self.y = 0
		self.screen = screen
		self.image = image
		self.width = screen_size[0]
		self.height = screen_size[1]
		self.font_color = (153, 0, 0)
		self.color = color
		self.image2 = image2
		self.lock_color = (30, 10, 10)
		self.lock_font_color = (100, 0, 0)
		self.levels = []
		self.lock_image = pygame.image.load("grafika/lock.png").convert_alpha()
		self.lock_color = (30, 10, 10)
		self.lock_font_color = (100, 0, 0)
	def draw(self):
		
		self.screen.blit(self.image,(self.x,self.y))
		self.screen.blit(self.image2, (400,100))
		
					
			
		
		pygame.draw.rect(self.screen,self.color,(200, 400, 300, 200))
		self.tekst1 = text(self.screen,200+65,490,"Obrona",self.font_color,32)
		if len(self.levels) >= 4:
			pygame.draw.rect(self.screen,self.color,(700, 400, 300, 200))
			self.tekst2 = text(self.screen,700+35,490,"Kontratak",self.font_color,32)
		else:
			pygame.draw.rect(self.screen,self.lock_color,(700, 400, 300, 200))
			self.tekst2 = text(self.screen,700+35,490,"Kontratak",self.lock_font_color,32)	
			self.screen.blit(self.lock_image,(700+150-30,400+100-40))	
			

		if len(self.levels) >= 7:
			pygame.draw.rect(self.screen,self.color,(1200,400,300,200))
			self.tekst3 = text(self.screen,1200+85,490,"Bonus",self.font_color,32)
		else:
			pygame.draw.rect(self.screen,self.lock_color,(1200,400,300,200))
			self.tekst3 = text(self.screen,1200+85,490,"Bonus",self.lock_font_color,32)
			self.screen.blit(self.lock_image,(1200+150-30,400+100-40))



	def update(self):
		self.draw()