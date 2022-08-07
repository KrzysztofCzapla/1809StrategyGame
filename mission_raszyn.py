import pygame
import math
from text import *
from unit import *
from hud import *

end_screen_bg = pygame.image.load('grafika/tut_background.png').convert_alpha()

pygame.init()

class mission_class(pygame.sprite.Sprite):
	def __init__(self,screen,screen_size,mouse,units_images,units,fighting_icon,sounds,logo_pl_unit,logo_at_unit,logo_pl,mission):
		self.mission = mission

		if self.mission == "raszyn":
			self.unit_spacing = 100
			self.unit1 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+self.unit_spacing*5,screen_size[1]-320,logo_pl_unit,"pl","infantry","1 Pulk Piechoty",100)
			self.unit2 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+self.unit_spacing*9/2,screen_size[1]-300,logo_pl_unit,"pl","cavalry","Dywizja Kawalerii",100)
			self.unit3 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180,screen_size[1]-140,logo_pl_unit,"pl","infantry","Druga Brygada3",100)
			self.unit4 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+self.unit_spacing,screen_size[1]-90,logo_pl_unit,"pl","artillery","Artyleria Polska",100)

			self.unit5 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+2*self.unit_spacing,screen_size[1]-90,logo_pl_unit,"pl","infantry","Pierwsza Brygada",100)
			self.unit6 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+3*self.unit_spacing,screen_size[1]-90,logo_pl_unit,"pl","cavalry","Dywizja Kawalerii",100)
			self.unit7 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+4*self.unit_spacing,screen_size[1]-90,logo_pl_unit,"pl","infantry","Druga Brygada",100)
			self.unit8 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+8*self.unit_spacing,screen_size[1]-90,logo_pl_unit,"pl","artillery","Artyleria Polska2",100)



			self.unit9 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+5*self.unit_spacing,200+30,logo_at_unit,"at","cavalry","kirasjerzy",100)
			self.unit10 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180*5/11*self.unit_spacing,200+60,logo_at_unit,"at","cavalry","Dywizja Kawalerii",100)
			self.unit11 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180,200+70,logo_at_unit,"at","infantry","Druga Brygada",100)
			self.unit12 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+self.unit_spacing,200+100,logo_at_unit,"at","artillery","Artyleria Polska5",100)

			self.unit13 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+2*self.unit_spacing,200+70,logo_at_unit,"at","infantry","Pierwsza Brygadat",100)
			self.unit14 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+3*self.unit_spacing,200+40,logo_at_unit,"at","cavalry","Dywizja Kawalerii",100)
			self.unit15 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+4*self.unit_spacing,200+50,logo_at_unit,"at","infantry","Druga Brygada2",100)
			self.unit16 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+8*self.unit_spacing,200+120,logo_at_unit,"at","artillery","Artyleria Polska6",100)


			self.raszyn_tlo = pygame.image.load("grafika/raszyn_tlo.png").convert_alpha()
			self.raszyn_river = pygame.image.load("grafika/raszyn_river.png").convert_alpha()

			
			self.units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6,self.unit7,self.unit8,self.unit9,self.unit10,self.unit11,self.unit12,self.unit13,self.unit14,self.unit15,self.unit16]

			self.enemy_units =[]#self.unit9,self.unit10,self.unit11,self.unit12,self.unit13,self.unit14,self.unit15,self.unit16]

			self.hud = HUD(screen, screen_size, logo_pl,self.units,self.unit1,"Obron raszyn")



			self.screen = screen
			self.screen_size = screen_size

			self.is_over = False


	def if_ended(self):
		if len(self.enemy_units) == 0:
			print("###################")
			self.is_over = True

	def end_screen(self):
		print("koniec")
		keys = pygame.key.get_pressed()
		while not keys[pygame.K_SPACE]:
			self.screen.blit(end_screen_bg,(0,0))


			end_skip = text(screen,tut_x,tut_y+5*tut_y_spacing,"Kliknij SPACJE, aby kontynuowac",(0,0,0),tut_size-10)









	def update(self):
		#print(self.hudd.unit)
		self.screen.blit(self.raszyn_tlo,(0,0))
		

		#self.screen.blit(self.raszyn_river,(0,self.screen_size[1]-350))


		self.if_ended()
		self.hud.update()

