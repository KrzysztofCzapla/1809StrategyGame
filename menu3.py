import pygame
from text import *
from button import *
przycisk1 = pygame.Rect(200, 400, 300, 200)
przycisk2 = pygame.Rect(700, 400, 300, 200)
przycisk3 = pygame.Rect(1200,400,300,200)
class MENU3:
	def __init__(self,screen,screen_size,image,color,font_color,image2):
		self.x = 0
		self.y = 0
		self.screen = screen
		self.image = image
		self.width = screen_size[0]
		self.height = screen_size[1]
		self.font_color = (153, 0, 0)
		self.color = color
		self.music = 1
		self.image2 = image2
		self.rozdzielczosc = 1
		self.przycisk = button(self.screen,self.x,self.y,self.width,self.height,self.color,przycisk2,'Graj',font="freesansbold.ttf")
		self.volume = 0.5

		self.suwak_volume = pygame.Rect(703+294*self.volume,375-3-5,10,15+6+10)

		self.volume_x = 294/2+703

		self.przycisk2 = button(self.screen,self.x,self.y,self.width,self.height,self.color,przycisk1,'Graj',font="freesansbold.ttf")
		self.button_text2 = text(self.screen,295,490,'Wstecz',self.font_color,32)
	def draw(self):
		self.screen.blit(self.image,(self.x,self.y))
		self.screen.blit(self.image2, (400,100))
	def update(self):
		self.draw()
		self.przycisk = button(self.screen,self.x,self.y,self.width,self.height,self.color,przycisk2,'Graj',font="freesansbold.ttf")
		if self.music == 1:
			self.button_text1 = text(self.screen,780,490,'Dzwiek',(20,100,30),32)
		if self.music == 2:
			self.button_text1 = text(self.screen,780,490,'Dzwiek',self.font_color,32)


		pygame.draw.rect(self.screen,(81, 10, 10),(700,375-3,300,15+6)) #80,20,30
		pygame.draw.rect(self.screen,(20,100,30),(700+3,375,self.volume_x-703,15))
		self.suwak_volume = pygame.Rect(700,375-3,300,15+6)

		pygame.draw.rect(self.screen,(114,114,114),(self.volume_x,375-3-5,10,15+6+10))

		self.volume = round((self.volume_x-703)/294,2)
		#print(self.volume)
		pygame.mixer.music.set_volume(self.volume)



		self.przycisk2 = button(self.screen,self.x,self.y,self.width,self.height,self.color,przycisk1,'Graj',font="freesansbold.ttf")
		self.button_text2 = text(self.screen,280,490,'Wstecz',self.font_color,32)
		pygame.draw.rect(self.screen,self.color,(1200,400,300,200))
		if self.rozdzielczosc == 1:
			self.button_text3 = text(self.screen,1200+27,490,'Fullscreen',self.font_color,32)
		if self.rozdzielczosc == 2:
			self.button_text3 = text(self.screen,1200+27,490,'Fullscreen',(20,100,30),32)




