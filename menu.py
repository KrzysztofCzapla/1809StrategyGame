import pygame
from text import *
from button import *
from menu2 import *
przycisk1 = pygame.Rect(200, 400, 300, 200)
przycisk2 = pygame.Rect(700, 400, 300, 200)
przycisk3 = pygame.Rect(1200,400,300,200)

class MENU ():
	def __init__(self,screen,screen_size,image,color,font_color,image2):
		self.x = 0
		self.y = 0
		self.screen = screen
		self.image = image
		self.width = screen_size[0]
		self.height = screen_size[1]
		self.font_color = (153, 0, 0)
		self.color = color
		self.which_menu = 1
		self.image2 = image2
		#muzykamenu.play(-1)
		#self.button_text = text(self.screen,self.x+400,self.y+500,'Graj',self.font_color,32)

		self.grid_size = 20
		self.screen_size = screen_size

		self.how_many_grids_x = int(screen_size[0]/self.grid_size)
		self.how_many_grids_y = int(screen_size[1]/self.grid_size)
	   	

				 
		
		#self.button_text

	###############przycisk#########
	def draw(self):
		self.screen.blit(self.image,(self.x,self.y))
		self.screen.blit(self.image2, (400,100))

	#def createbutton(self, screen, rect):
		#self.rect = rect
		#self.screen - screen
	def update(self):
		self.draw()


		self.przycisk = button(self.screen,self.x,self.y,self.width,self.height,self.color,przycisk1,'Graj',font="freesansbold.ttf")
		self.button2 = button(self.screen,self.x,self.y,self.width,self.height,self.color,przycisk2,'Opcje',font='freesansbold.tft')
		self.button3 = button(self.screen,self.x,self.y,self.width,self.height,self.color,przycisk3,'Wyjscie',font='freesansbold.tft')
		self.button_text = text(self.screen,295,490,'Graj',self.font_color,32)
		self.button_text1 = text(self.screen,800-15,490,'Opcje',self.font_color,32)
		self.button_text2 = text(self.screen,1230+30+5,490,'Wyjscie',self.font_color,32)
		'''for i in range(self.how_many_grids_x):
			pygame.draw.rect(self.screen,(1,1,1),((self.grid_size*i,0),(1,self.screen_size[1]))) #ekran,kolor,(x,y lewego gornego rogu, szerokość)
		for i in range(self.how_many_grids_y):
			pygame.draw.rect(self.screen,(1,1,1),((0,self.grid_size*i),(self.screen_size[0],1))) # tak samo'''
		#przycisk.draw()
		#self.which_menu = 1





	
		