import pygame
from text import *
from button import *
przycisk1 = pygame.Rect(200, 400, 300, 200)
przycisk2 = pygame.Rect(700, 400, 300, 200)
przycisk3 = pygame.Rect(1200,400,300,200)
class MENU2():
	def __init__(self,screen,screen_size,image,color,font_color,image2,levels):
		self.x = 0
		self.y = 0
		self.screen = screen
		self.image = image
		self.width = screen_size[0]
		self.height = screen_size[1]
		self.font_color = (153, 0, 0)
		self.color = color
		self.image2 = image2
		self.przycisk = button(self.screen,self.x,self.y,self.width,self.height,self.color,przycisk1,'Graj',font="freesansbold.ttf")
		self.button2 = button(self.screen,self.x,self.y,self.width,self.height,self.color,przycisk2,'Opcje',font='freesansbold.tft')
		self.button3 = button(self.screen,self.x,self.y,self.width,self.height,self.color,przycisk3,'Wyjście',font='freesansbold.tft')
		self.button_text = text(self.screen,270,490,'Raszyn',self.font_color,32)
		self.button_text1 = text(self.screen,785,490,'Praga',self.font_color,32)
		self.button_text2 = text(self.screen,1210,490,'Na poludnie!',self.font_color,32)

		self.lock_image = pygame.image.load("grafika/lock.png").convert_alpha()
		self.levels = levels
		self.lock_color = (30, 10, 10)
		self.lock_font_color = (100, 0, 0)


	def draw(self):
		self.screen.blit(self.image,(self.x,self.y))
		self.screen.blit(self.image2, (400,100))
	def update(self):
		self.draw()
		self.przycisk = button(self.screen,self.x,self.y,self.width,self.height,self.color,przycisk1,'Graj',font="freesansbold.ttf")
		self.button_text = text(self.screen,260,490,'Tutorial',self.font_color,32)
		if len(self.levels) >= 3:
			print("3")
			self.button2 = button(self.screen,self.x,self.y,self.width,self.height,self.color,przycisk2,'Opcje',font='freesansbold.tft')
			self.button_text1 = text(self.screen,775,490,'Raszyn',self.font_color,32)

			self.button3 = button(self.screen,self.x,self.y,self.width,self.height,self.color,przycisk3,'Wyjście',font='freesansbold.tft')
			self.button_text2 = text(self.screen,1280+5,490,'Praga',self.font_color,32)


		elif len(self.levels) >= 2:
			print("2")
			self.button2 = button(self.screen,self.x,self.y,self.width,self.height,self.color,przycisk2,'Opcje',font='freesansbold.tft')
			self.button_text1 = text(self.screen,775,490,'Raszyn',self.font_color,32)

			self.button3 = button(self.screen,self.x,self.y,self.width,self.height,self.lock_color,przycisk3,'Wyjście',font='freesansbold.tft')
			self.button_text2 = text(self.screen,1280+5,490,'Praga',self.lock_font_color,32)
			self.screen.blit(self.lock_image,(1200+150-30,400+100-40))

		
		elif len(self.levels) >= 1:
			print("4")
			self.button2 = button(self.screen,self.x,self.y,self.width,self.height,self.lock_color,przycisk2,'Opcje',font='freesansbold.tft')
			self.button3 = button(self.screen,self.x,self.y,self.width,self.height,self.lock_color,przycisk3,'Wyjście',font='freesansbold.tft')

			self.button_text1 = text(self.screen,775,490,'Raszyn',self.lock_font_color,32)
			self.button_text2 = text(self.screen,1280+5,490,'Praga',self.lock_font_color,32)

			self.screen.blit(self.lock_image,(700+150-30,400+100-40))
			self.screen.blit(self.lock_image,(1200+150-30,400+100-40))



		
		
		