import pygame
import math
from text import *
from unit import *
from hud import *

class loading_time(pygame.sprite.Sprite):
	def __init__(self,screen,image,x,y,w,h,color,units):
		self.screen = screen
		self.image = image
		self.x =  x
		self.y = y
		self.w = w
		self.h = h
		self.cur_w = 1
		self.color = color
		self.units = units

		self.screen.blit(self.screen,(0,0))
		pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.cur_w,self.h))
		#self.clock = pygame.time.Clock()

		

	def add(self):
		self.cur_w += self.w/(self.units+1)

		self.screen.blit(self.screen,(0,0))
		pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.cur_w,self.h))
		pygame.display.update()
		#self.clock.tick(30)




pygame.init()

class mission_class(pygame.sprite.Sprite):
	def __init__(self,screen,screen_size,mouse,units_images,units,fighting_icon,sounds,logo_pl_unit,logo_at_unit,logo_pl,mission):
		self.mission = mission
		self.loading_image = pygame.image.load("grafika/tlo_dwa_big.png").convert_alpha()

		self.end_screen_bg = pygame.image.load('grafika/tlo_dwa_big.png').convert_alpha()
		self.screen = screen
		if self.mission == "leipzig":
			logo_fr = pygame.image.load("grafika/logo_fr_160.png").convert_alpha()
			logo_fr_unit = pygame.image.load("grafika/logo_fr_64.png").convert_alpha()

			logo_ru_unit = pygame.image.load("grafika/logo_ru_64.png").convert_alpha()
			logo_sw_unit = pygame.image.load("grafika/logo_sw_64.png").convert_alpha()
			logo_de_unit = pygame.image.load("grafika/logo_de_64.png").convert_alpha()

			self.unit_spacing = 100
			self.loading = loading_time(self.screen,self.loading_image,200,700,1200,100,(81, 10, 10),18)
			self.unit1 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",770,450,logo_fr_unit,"pl","infantry","1 Pulk Piechoty",100)
			self.loading.add()
			self.unit2 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1000,460,logo_fr_unit,"pl","cavalry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit3 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1000,350,logo_fr_unit,"pl","infantry","Druga Brygada",100)
			self.loading.add()
			self.unit4 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",630,300,logo_fr_unit,"pl","artillery","Artyleria",100)
			self.loading.add()
			self.unit5 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",650,400,logo_fr_unit,"pl","infantry","Pierwsza Brygada",100)
			self.loading.add()
			self.unit6 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",820,360,logo_fr_unit,"pl","cavalry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit15 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",570,380,logo_pl_unit,"pl","infantry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit16 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",900,560,logo_pl_unit,"pl","infantry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit19 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1000,560,logo_pl_unit,"pl","infantry","Dywizja Kawalerii",100)
			self.loading.add()



			self.unit7 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",300,300,logo_sw_unit,"at","infantry","P1",100)
			self.loading.add()
			self.unit8 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",360,550,logo_ru_unit,"at","infantry","P2",100)
			self.loading.add()
			self.unit9 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",770,770,logo_ru_unit,"at","cavalry","K1",100)
			self.loading.add()
			self.unit10 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",450,680,logo_ru_unit,"at","cavalry","K2",100)
			self.loading.add()
			self.unit11 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1000,690,logo_de_unit,"at","artillery","A1",100)
			self.loading.add()
			self.unit12 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1200,300,logo_ru_unit,"at","artillery","A2",100)
			self.loading.add()
			self.unit13 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",580,520,logo_de_unit,"at","infantry","P3",100)
			self.loading.add()
			self.unit14 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1200,550,logo_ru_unit,"at","cavalry","K3",100)
			self.loading.add()
			self.unit17 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1100,500,logo_sw_unit,"at","infantry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit18 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1300,600,logo_sw_unit,"at","infantry","Dywizja Kawalerii2",100)
			self.loading.add()
		


			self.raszyn_tlo = pygame.image.load("grafika/leipzig_tlo.png").convert_alpha()
			#self.raszyn_tlo = 
			self.raszyn_river = pygame.image.load("grafika/raszyn_river.png").convert_alpha()

			
			self.units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6,self.unit7,self.unit8,self.unit9,self.unit10,self.unit11,self.unit12,self.unit13,self.unit14,self.unit15,self.unit16,self.unit17,self.unit18,self.unit19]

			self.ally_units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6,self.unit15,self.unit16,self.unit19]
			self.enemy_units =[self.unit7,self.unit8,self.unit9,self.unit10,self.unit11,self.unit12,self.unit13,self.unit14,self.unit17,self.unit18]

			self.hud = HUD(screen, screen_size, logo_fr,self.units,self.unit1,"przetrwaj bitwe narodow")
			self.hud.quest2 = ""



			self.screen = screen
			self.screen_size = screen_size

			self.is_over = False
			self.is_win = False

			self.loading.add()
		if self.mission == "borodino":
			logo_fr = pygame.image.load("grafika/logo_fr_160.png").convert_alpha()
			logo_fr_unit = pygame.image.load("grafika/logo_fr_64.png").convert_alpha()

			logo_ru_unit = pygame.image.load("grafika/logo_ru_64.png").convert_alpha()

			self.unit_spacing = 100
			self.loading = loading_time(self.screen,self.loading_image,200,700,1200,100,(81, 10, 10),18)
			self.unit1 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",100,800,logo_fr_unit,"pl","infantry","1 Pulk Piechoty",100)
			self.loading.add()
			self.unit2 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1200,700,logo_fr_unit,"pl","cavalry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit3 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",500,790,logo_fr_unit,"pl","infantry","Druga Brygada",100)
			self.loading.add()
			self.unit4 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",400,700,logo_fr_unit,"pl","artillery","Artyleria",100)
			self.loading.add()
			self.unit5 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",650,800,logo_fr_unit,"pl","infantry","Pierwsza Brygada",100)
			self.loading.add()
			self.unit6 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1000,810,logo_fr_unit,"pl","cavalry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit15 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1500,810,logo_pl_unit,"pl","infantry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit16 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",800,810,logo_pl_unit,"pl","infantry","Dywizja Kawalerii",100)
			self.loading.add()



			self.unit7 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",760,500,logo_ru_unit,"at","infantry","P1",100)
			self.loading.add()
			self.unit8 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",630,450,logo_ru_unit,"at","infantry","P2",100)
			self.loading.add()
			self.unit9 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",950,500,logo_ru_unit,"at","cavalry","K1",100)
			self.loading.add()
			self.unit10 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1080,400,logo_ru_unit,"at","cavalry","K2",100)
			self.loading.add()
			self.unit11 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",450,400,logo_ru_unit,"at","artillery","A1",100)
			self.loading.add()
			self.unit12 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1200,400,logo_ru_unit,"at","artillery","A2",100)
			self.loading.add()
			self.unit13 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",580,520,logo_ru_unit,"at","infantry","P3",100)
			self.loading.add()
			self.unit17 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1100,500,logo_ru_unit,"at","infantry","Dywizja Kawalerii",100)



			self.raszyn_tlo = pygame.image.load("grafika/borodino_tlo.png").convert_alpha()
			#self.raszyn_tlo = 
			self.raszyn_river = pygame.image.load("grafika/raszyn_river.png").convert_alpha()

			
			self.units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6,self.unit7,self.unit8,self.unit9,self.unit10,self.unit11,self.unit12,self.unit13,self.unit15,self.unit16]

			self.ally_units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6,self.unit15,self.unit16]
			self.enemy_units =[self.unit7,self.unit8,self.unit9,self.unit10,self.unit11,self.unit12,self.unit13]

			self.hud = HUD(screen, screen_size, logo_fr,self.units,self.unit1,"zajmij rodute rosjan")
			self.hud.quest2 = ""



			self.screen = screen
			self.screen_size = screen_size

			self.is_over = False
			self.is_win = False

			self.loading.add()
		if self.mission == "waterloo":
			logo_fr = pygame.image.load("grafika/logo_fr_160.png").convert_alpha()
			logo_fr_unit = pygame.image.load("grafika/logo_fr_64.png").convert_alpha()

			logo_uk_unit = pygame.image.load("grafika/logo_uk_64.png").convert_alpha()

			logo_de_unit = pygame.image.load("grafika/logo_de_64.png").convert_alpha()
			self.unit_spacing = 100
			self.loading = loading_time(self.screen,self.loading_image,200,700,1200,100,(81, 10, 10),18)
			self.unit1 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",100,800,logo_fr_unit,"pl","infantry","1 Pulk Piechoty",100)
			self.loading.add()
			self.unit2 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",120,700,logo_fr_unit,"pl","cavalry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit3 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",200,790,logo_fr_unit,"pl","infantry","Druga Brygada",100)
			self.loading.add()
			self.unit4 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",230,700,logo_fr_unit,"pl","artillery","Artyleria Polska",100)
			self.loading.add()
			self.unit5 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",350,800,logo_fr_unit,"pl","infantry","Pierwsza Brygada",100)
			self.loading.add()
			self.unit6 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",270,810,logo_fr_unit,"pl","cavalry","Dywizja Kawalerii",100)
			self.loading.add()


			self.unit7 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",50,300,logo_uk_unit,"at","infantry","P1",100)
			self.loading.add()
			self.unit8 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",130,320,logo_uk_unit,"at","infantry","P2",100)
			self.loading.add()
			self.unit9 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",200,400,logo_uk_unit,"at","cavalry","K1",100)
			self.loading.add()
			self.unit10 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",210,260,logo_uk_unit,"at","cavalry","K2",100)
			self.loading.add()
			self.unit11 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",300,300,logo_uk_unit,"at","artillery","A1",100)
			self.loading.add()
			self.unit12 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1300,400,logo_de_unit,"at","artillery","A2",100)
			self.loading.add()
			self.unit13 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1400,520,logo_de_unit,"at","infantry","P3",100)
			self.loading.add()
			self.unit14 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1500,700,logo_de_unit,"at","cavalry","K3",100)
			self.loading.add()



			self.raszyn_tlo = pygame.image.load("grafika/waterloo_tlo.png").convert_alpha()
			#self.raszyn_tlo = 
			self.raszyn_river = pygame.image.load("grafika/raszyn_river.png").convert_alpha()

			
			self.units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6,self.unit7,self.unit8,self.unit9,self.unit10,self.unit11,self.unit12,self.unit13,self.unit14]

			self.ally_units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6]
			self.enemy_units =[self.unit7,self.unit8,self.unit9,self.unit10,self.unit11,self.unit12,self.unit13,self.unit14]

			self.hud = HUD(screen, screen_size, logo_fr,self.units,self.unit1,"sprobuj wygrac bitwe")
			self.hud.quest2 = "pod Waterloo"



			self.screen = screen
			self.screen_size = screen_size

			self.is_over = False
			self.is_win = False

			self.loading.add()
		if self.mission == "torun":
			self.end_screen_bg = pygame.image.load('grafika/end_torun.png').convert_alpha()


			self.loading = loading_time(self.screen,self.loading_image,200,700,1200,100,(81, 10, 10),15)
			



			self.unit_spacing = 100
			self.loading.add()
			self.unit1 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",200,300,logo_pl_unit,"pl","infantry","1 Pulk Piechoty",100)
			self.loading.add()
			self.unit2 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",200,560,logo_pl_unit,"pl","cavalry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit3 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",150,800,logo_pl_unit,"pl","infantry","Trzecia Brygada",100)
			self.loading.add()
			self.unit4 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",300,300,logo_pl_unit,"pl","artillery","Artyleria Polska",100)
			self.loading.add()
			self.unit5 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",170,700,logo_pl_unit,"pl","infantry","Pierwsza Brygada",100)
			self.loading.add()
			self.unit6 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",250,750,logo_pl_unit,"pl","infantry","Pierwsza Brygada",100)
			self.loading.add()
			self.unit18 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",430,560,logo_pl_unit,"pl","cavalry","Dywizja Kawalerii",100)
			self.loading.add()
			print("ally unit zaladowane")

			
			self.unit9 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1250,200,logo_at_unit,"at","cavalry","kirasjerzy",100)
			self.loading.add()
			#self.unit10 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+5/11*self.unit_spacing,200+60,logo_at_unit,"at","cavalry","Dywizja Kawalerii",100)
			self.unit11 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1000,500,logo_at_unit,"at","infantry","Druga Brygada",100)
			self.loading.add()
			self.unit12 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1500,600,logo_at_unit,"at","artillery","Arty1",100)
			self.loading.add()
			self.unit13 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1300,700,logo_at_unit,"at","infantry","Pierwsza Brygadat3",100)
			self.loading.add()
			self.unit14 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1100,700,logo_at_unit,"at","infantry","Piechota1",100)
			self.loading.add()
			self.unit15 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1400,500,logo_at_unit,"at","infantry","Pierwsza Brygadat",100)
			self.unit16 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1100,800,logo_at_unit,"at","infantry","Pierwsza Brygadat2",100)
			#self.unit17 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1500,500,logo_at_unit,"at","infantry","Pierwsza Brygadat4",100)
			#self.loading.add()
			self.units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6,self.unit9,self.unit11,self.unit12,self.unit13,self.unit14,self.unit15,self.unit16,self.unit18]

			self.ally_units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6,self.unit18]
			self.enemy_units =[self.unit9,self.unit11,self.unit12,self.unit13,self.unit14,self.unit15,self.unit16]

			self.hud = HUD(screen, screen_size, logo_pl,self.units,self.unit1,"Obron Torun")

			self.screen = screen
			self.screen_size = screen_size

			self.is_over = False
			self.is_win = False
			self.raszyn_tlo = pygame.image.load("grafika/torun_tlo.png").convert_alpha()
			print("wszystko zaladowane")
			self.loading.add()
		if self.mission == "ostrowek":
			self.end_screen_bg = pygame.image.load('grafika/end_ostrowek.png').convert_alpha()


			self.loading = loading_time(self.screen,self.loading_image,200,700,1200,100,(81, 10, 10),15)
			



			self.unit_spacing = 100
			self.loading.add()
			self.unit1 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",500+200,230,logo_pl_unit,"pl","infantry","1 Pulk Piechoty",100)
			self.loading.add()
			self.unit2 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",700+200,260,logo_pl_unit,"pl","cavalry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit3 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",750+200,400,logo_pl_unit,"pl","infantry","Trzecia Brygada",100)
			self.loading.add()
			self.unit4 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",800+200,300,logo_pl_unit,"pl","artillery","Artyleria Polska",100)
			self.loading.add()
			self.unit5 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",775+200,700,logo_pl_unit,"pl","infantry","Pierwsza Brygada",100)
			self.loading.add()
			self.unit6 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",900+200,750,logo_pl_unit,"pl","infantry","Pierwsza Brygada",100)
			self.loading.add()

			print("ally unit zaladowane")

			
			self.unit9 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",450,300,logo_at_unit,"at","cavalry","kirasjerzy",100)
			self.loading.add()
			#self.unit10 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+5/11*self.unit_spacing,200+60,logo_at_unit,"at","cavalry","Dywizja Kawalerii",100)
			self.unit11 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",500,500,logo_at_unit,"at","infantry","Druga Brygada",100)
			self.loading.add()
			self.unit12 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",475,600,logo_at_unit,"at","artillery","Arty1",100)
			self.loading.add()
			self.unit13 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",480,700,logo_at_unit,"at","infantry","Pierwsza Brygadat",100)
			self.loading.add()
			self.unit14 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",775,700,logo_at_unit,"at","infantry","Piechota1",100)
			self.loading.add()
			self.unit15 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",600,500,logo_at_unit,"at","infantry","Pierwsza Brygadat",100)
			self.loading.add()			

			print("enemy unit zaladowane")
			self.bridge_timer = 1
			self.bridge_timer2 = 1
			self.bridge_timer_max = 60
			self.bridge_progress = 0
			self.bridge_progress_max = 24
			self.destroying_bridge = False
			self.raszyn_tlo = pygame.image.load("grafika/ostrowek_tlo.png").convert_alpha()
			self.bridge_part = pygame.image.load("grafika/bridge_part.png").convert_alpha()
			#self.raszyn_river = pygame.image.load("grafika/raszyn_river.png").convert_alpha()



			
			self.units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6,self.unit9,self.unit11,self.unit12,self.unit13,self.unit14,self.unit15]

			self.ally_units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6]
			self.enemy_units =[self.unit9,self.unit11,self.unit12,self.unit13,self.unit14,self.unit15]

			self.hud = HUD(screen, screen_size, logo_pl,self.units,self.unit1,"Pokonaj jednostki")
			self.hud.quest2 = "broniace mostu"

			self.screen = screen
			self.screen_size = screen_size

			self.is_over = False
			self.is_win = False

			print("wszystko zaladowane")
			self.loading.add()


		if self.mission == "tutorial":
			self.target = None
			self.what_now = 1
			self.select_timer = 10
			self.loading = loading_time(self.screen,self.loading_image,200,700,1200,100,(81, 10, 10),10)
			



			self.unit_spacing = 100
			self.loading.add()
			self.unit1 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"tutorial",230,800,logo_pl_unit,"pl","infantry","1 Pulk Piechoty",100)
			self.loading.add()
			self.unit2 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"tutorial",400,800,logo_pl_unit,"pl","cavalry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit3 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"tutorial",500,800,logo_pl_unit,"pl","infantry","Trzecia Brygada",100)
			self.loading.add()
			self.unit4 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"tutorial",600,800,logo_pl_unit,"pl","artillery","Artyleria Polska",100)
			self.loading.add()
			self.unit5 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"tutorial",700,800,logo_pl_unit,"pl","infantry","Pierwsza Brygada",100)
			self.loading.add()
			self.unit6 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"tutorial",800,800,logo_pl_unit,"pl","cavalry","Dywizja Kawalerii",100)
			self.loading.add()

			print("ally unit zaladowane")

			
			self.unit9 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"tutorial",200,300,logo_at_unit,"at","infantry","kirasjerzy",100)
			self.loading.add()
			#self.unit10 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"tutorial",180+5/11*self.unit_spacing,200+60,logo_at_unit,"at","cavalry","Dywizja Kawalerii",100)
			self.unit11 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"tutorial",500,300,logo_at_unit,"at","cavalry","Druga Brygada",80)
			self.loading.add()
			self.unit12 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"tutorial",1200,400,logo_at_unit,"at","artillery","Artyleria Polska5",75)
			self.loading.add()
			self.unit13 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"tutorial",400,600,logo_at_unit,"at","infantry","Pierwsza Brygadat",30)
			self.loading.add()

			

			print("enemy unit zaladowane")
			self.raszyn_tlo = pygame.image.load("grafika/raszyn_tlo.png").convert_alpha()
			self.raszyn_river = pygame.image.load("grafika/raszyn_river.png").convert_alpha()

			
			self.units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6,self.unit9,self.unit11,self.unit12,self.unit13]

			self.ally_units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6]
			self.enemy_units =[self.unit9,self.unit11,self.unit12,self.unit13]

			self.hud = HUD(screen, screen_size, logo_pl,self.units,self.unit1,"Obron raszyn")



			self.screen = screen
			self.screen_size = screen_size

			self.is_over = False
			self.is_win = False
			print("wszystko zaladowane")
			self.loading.add()
		


		if self.mission == "poludnie":
			self.end_screen_bg = pygame.image.load('grafika/end_poludnie.png').convert_alpha()
			self.unit_spacing = 100
			self.loading = loading_time(self.screen,self.loading_image,200,700,1200,100,(81, 10, 10),18)
			self.unit1 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1200,800,logo_pl_unit,"pl","infantry","1 Pulk Piechoty",100)
			self.loading.add()
			self.unit2 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1300,800,logo_pl_unit,"pl","cavalry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit3 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1400,790,logo_pl_unit,"pl","infantry","Druga Brygada",100)
			self.loading.add()
			self.unit4 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1500,750,logo_pl_unit,"pl","artillery","Artyleria Polska",100)
			self.loading.add()
			self.unit5 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1450,600,logo_pl_unit,"pl","infantry","Pierwsza Brygada",100)
			self.loading.add()
			self.unit6 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1400,500,logo_pl_unit,"pl","cavalry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit7 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1350,400,logo_pl_unit,"pl","infantry","Druga Brygada",100)
			#self.unit8 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1300,300,logo_pl_unit,"pl","artillery","Artyleria Polska2",100)
			self.loading.add()


			self.unit9 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1300,540,logo_at_unit,"at","cavalry","K1",100)
			#self.unit10 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+5/11*self.unit_spacing,200+60,logo_at_unit,"at","cavalry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit11 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1000,300,logo_at_unit,"at","infantry","P1",100)
			self.loading.add()
			self.unit12 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",300,400,logo_at_unit,"at","artillery","A1",100)
			self.loading.add()
			self.unit13 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",950,520,logo_at_unit,"at","infantry","P2",100)
			self.loading.add()
			self.unit14 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",1100,700,logo_at_unit,"at","cavalry","K2",100)
			self.loading.add()
			self.unit15 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",800,800,logo_at_unit,"at","infantry","P3",100)
			self.loading.add()
			self.unit16 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",100,500,logo_at_unit,"at","artillery","A2",100)



			self.raszyn_tlo = pygame.image.load("grafika/poludnie_tlo.png").convert_alpha()
			self.raszyn_river = pygame.image.load("grafika/raszyn_river.png").convert_alpha()

			
			self.units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6,self.unit7,self.unit9,self.unit11,self.unit12,self.unit13,self.unit14,self.unit15,self.unit16]

			self.ally_units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6,self.unit7]
			self.enemy_units =[self.unit9,self.unit11,self.unit12,self.unit13,self.unit14,self.unit15,self.unit16]

			self.hud = HUD(screen, screen_size, logo_pl,self.units,self.unit1,"Zniszcz jednostki wroga")



			self.screen = screen
			self.screen_size = screen_size

			self.is_over = False
			self.is_win = False

			self.loading.add()




		if self.mission == "praga":
			self.end_screen_bg = pygame.image.load('grafika/end_praga.png').convert_alpha()
			self.unit_spacing = 100
			self.loading = loading_time(self.screen,self.loading_image,200,700,1200,100,(81, 10, 10),18)
			self.unit1 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",1300,800,logo_pl_unit,"pl","infantry","1 Pulk Piechoty",100)
			self.loading.add()			
			self.unit3 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",1280,720,logo_pl_unit,"pl","infantry","Trzecia Brygada",100)
			self.loading.add()
			self.unit4 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",1350,600,logo_pl_unit,"pl","artillery","Artyleria Polska",100)
			self.loading.add()
			self.unit5 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",1250,230,logo_pl_unit,"pl","infantry","Pierwsza Brygada",100)
			self.loading.add()
			self.unit6 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",1300,430,logo_pl_unit,"pl","cavalry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit7 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",640,430,logo_pl_unit,"pl","infantry","Druga Brygada",100)
			self.loading.add()
			self.unit8 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",750,490,logo_pl_unit,"pl","artillery","2 Artyleria Polska",100)
			self.loading.add()
			self.unit19 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",1400,280,logo_pl_unit,"pl","infantry","Piechota Polska",100)
			self.loading.add()
			self.unit20 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",1230,400,logo_pl_unit,"pl","infantry","Piechota Polska",100)
			self.loading.add()
			self.unit21 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",1200,500,logo_pl_unit,"pl","cavalry","Kawaleria Polska",100)
			self.loading.add()
			self.unit22 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",1300,680,logo_pl_unit,"pl","infantry","Piechota Polska",100)




			
			self.unit9 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",50,350,logo_at_unit,"at","cavalry","kirasjerzy",100)
			self.loading.add()
			self.unit10 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",190,800,logo_at_unit,"at","cavalry","Dywizja Kawaleriii",100)
			self.loading.add()
			self.unit11 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",250,730,logo_at_unit,"at","infantry","Druga Brygad11",100)
			self.loading.add()
			self.unit12 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",170,300,logo_at_unit,"at","artillery","Artyleria Polska5",100)
			self.loading.add()
			self.unit13 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",400,370,logo_at_unit,"at","infantry","Pierwsza Brygadat",100)
			self.loading.add()
			self.unit14 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",300,500,logo_at_unit,"at","cavalry","Dywizja Kawalerii2",100)
			self.loading.add()
			self.unit15 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",410,300,logo_at_unit,"at","infantry","Druga Brygada8",100)
			self.loading.add()
			self.unit16 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",390,550,logo_at_unit,"at","infantry","Druga Brygada7",100)
			self.loading.add()
			self.unit17 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",250,600,logo_at_unit,"at","infantry","Druga Brygada5",100)
			self.loading.add()
			self.unit18 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"praga",350,700,logo_at_unit,"at","infantry","Druga Brygada4",100)

			


			self.raszyn_tlo = pygame.image.load("grafika/praga_tlo.png").convert_alpha()
			self.raszyn_river = pygame.image.load("grafika/raszyn_river.png").convert_alpha()

			
			self.units = [self.unit1,self.unit3,self.unit4,self.unit5,self.unit6,self.unit7,self.unit8,self.unit9,self.unit10,self.unit11,self.unit12,self.unit13,self.unit14,self.unit15,self.unit16,self.unit18,self.unit17,self.unit19,self.unit20,self.unit21,self.unit22]

			self.ally_units = [self.unit1,self.unit3,self.unit4,self.unit5,self.unit6,self.unit7,self.unit8,self.unit19,self.unit20,self.unit21,self.unit22]
			self.enemy_units =[self.unit9,self.unit10,self.unit11,self.unit12,self.unit13,self.unit14,self.unit15,self.unit16,self.unit17,self.unit18,]

			self.hud = HUD(screen, screen_size, logo_pl,self.units,self.unit1,"Odeprzj wrogie jednostki")



			self.screen = screen
			self.screen_size = screen_size

			self.is_over = False
			self.is_win = False
			self.loading.add()

		if self.mission == "raszyn":
			self.end_screen_bg = pygame.image.load('grafika/end_raszyn.png').convert_alpha()
			self.loading = loading_time(self.screen,self.loading_image,200,700,1200,100,(81, 10, 10),15)
			



			self.unit_spacing = 100
			self.loading.add()
			self.unit1 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+self.unit_spacing*5,screen_size[1]-320,logo_pl_unit,"pl","infantry","1 Pulk Piechoty",100)
			self.loading.add()
			self.unit2 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+self.unit_spacing*9/2,screen_size[1]-300,logo_pl_unit,"pl","cavalry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit3 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180,screen_size[1]-140,logo_pl_unit,"pl","infantry","Trzecia Brygada",100)
			self.loading.add()
			self.unit4 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+self.unit_spacing,screen_size[1]-90,logo_pl_unit,"pl","artillery","Artyleria Polska",100)
			self.loading.add()
			self.unit5 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+2*self.unit_spacing,screen_size[1]-90,logo_pl_unit,"pl","infantry","Pierwsza Brygada",100)
			self.loading.add()
			self.unit6 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+3*self.unit_spacing,screen_size[1]-90,logo_pl_unit,"pl","cavalry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit7 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+4*self.unit_spacing,screen_size[1]-90,logo_pl_unit,"pl","infantry","Druga Brygada",100)
			self.loading.add()
			self.unit8 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+8*self.unit_spacing,screen_size[1]-90,logo_pl_unit,"pl","artillery","2 Artyleria Polska",100)
			self.loading.add()
			print("ally unit zaladowane")

			
			self.unit9 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+5*self.unit_spacing,200+30,logo_at_unit,"at","cavalry","kirasjerzy",100)
			self.loading.add()
			#self.unit10 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+5/11*self.unit_spacing,200+60,logo_at_unit,"at","cavalry","Dywizja Kawalerii",100)
			self.unit11 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180,200+70,logo_at_unit,"at","infantry","Druga Brygada",100)
			self.loading.add()
			self.unit12 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+self.unit_spacing,200+100,logo_at_unit,"at","artillery","Artyleria Polska5",100)
			self.loading.add()
			self.unit13 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+2*self.unit_spacing,200+70,logo_at_unit,"at","infantry","Pierwsza Brygadat",100)
			self.loading.add()
			self.unit14 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+3*self.unit_spacing,200+40,logo_at_unit,"at","cavalry","Dywizja Kawalerii",100)
			self.loading.add()
			self.unit15 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+4*self.unit_spacing,200+50,logo_at_unit,"at","infantry","Druga Brygada2",100)
			self.loading.add()
			self.unit16 = unit(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,"raszyn",180+8*self.unit_spacing,200+120,logo_at_unit,"at","artillery","Artyleria Polska6",100)
			

			print("enemy unit zaladowane")
			self.raszyn_tlo = pygame.image.load("grafika/raszyn_tlo.png").convert_alpha()
			self.raszyn_river = pygame.image.load("grafika/raszyn_river.png").convert_alpha()

			
			self.units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6,self.unit7,self.unit8,self.unit9,self.unit11,self.unit12,self.unit13,self.unit14,self.unit15,self.unit16]

			self.ally_units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6,self.unit7,self.unit8]
			self.enemy_units =[self.unit9,self.unit11,self.unit12,self.unit13,self.unit14,self.unit15,self.unit16]

			self.hud = HUD(screen, screen_size, logo_pl,self.units,self.unit1,"Obron raszyn")



			self.screen = screen
			self.screen_size = screen_size

			self.is_over = False
			self.is_win = False
			print("wszystko zaladowane")
			self.loading.add()

	def init_units(self,mission):
		if mission == "ostrowek":
			self.units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6,self.unit9,self.unit11,self.unit12,self.unit13,self.unit14,self.unit15]

			self.ally_units = [self.unit1,self.unit2,self.unit3,self.unit4,self.unit5,self.unit6]
			self.enemy_units =[self.unit9,self.unit11,self.unit12,self.unit13,self.unit14,self.unit15]

	def if_ended(self):
		if len(self.enemy_units) == 0:
			if self.mission != "ostrowek":
				print("###################")
				self.is_over = True
				#self.end_screen_bg = pygame.image.load('grafika/tlo_dwa_big.png').convert_alpha()
				self.is_win = True
				self.time_text = self.hud.time_text
			else:
				self.hud.quest = "ostrzelaj most"
				self.hud.quest2 = ""
				if self.bridge_timer2 <= 0:
					print("###################")
					self.is_over = True
					#self.end_screen_bg = pygame.image.load('grafika/tlo_dwa_big.png').convert_alpha()
					self.is_win = True
					self.time_text = self.hud.time_text					
		elif len(self.ally_units) == 0:
			self.is_over = True
			#self.end_screen_bg = pygame.image.load('grafika/tlo_dwa_big.png').convert_alpha()
			self.is_win = False
			self.time_text = self.hud.time_text

	def end_screen(self):
		
		print(self.hud.time_text)

		self.screen.blit(self.raszyn_tlo,(0,0))

		self.screen.blit(self.end_screen_bg,(0,0))

		if self.is_win == True:
			self.end_title = text(self.screen,50+50-10,250,"WYGRANA",(0,0,0),70)
			if self.mission == "raszyn":
				self.end_time = text(self.screen,50+50-10,400+6*50,"Odblokowano kolejny poziom",(30,0,0),30)	
		else:
			self.end_title = text(self.screen,50+50-10,250,"PRZEGRANA",(0,0,0),70)

		self.end_time_title = text(self.screen,50+50-10,400,"Czas:",(30,0,0),50)
		self.end_time_title = text(self.screen,50+50+800,120,"Ciekawostka:",(255,255,255),50)
		self.end_time = text(self.screen,250+50,400,self.time_text,(30,0,0),50)






		self.end_skip = text(self.screen,50+50,400+7*50,"Kliknij SPACJE, aby kontynuowac",(0,0,0),40-10)



	def tut_target(self,unit):
		if self.select_timer > 5:	
			unit.letter_color = (100,10,10)
			#self.hud.quest_title_color = (100,10,10)

		if self.select_timer <= 5:
			unit.letter_color = (0,0,0)
			#self.hud.quest_title_color = (0,0,0)


	def bridge_rect_progress(self):
		pygame.draw.rect(self.screen,(80,20,30),(310-3,615-3,4*self.bridge_progress_max+6,10+6))
		pygame.draw.rect(self.screen,(20,100,30),(310,615,4*self.bridge_timer2/self.bridge_timer_max,10))


	def update(self):

		#for unit in self.enemy_units:
		#	print("unit " + str(unit.name) + " :" + str(unit.logo_x))
		#print(self.hudd.unit)
		self.screen.blit(self.raszyn_tlo,(0,0))

		
 
		#self.screen.blit(self.raszyn_river,(0,self.screen_size[1]-350))


		self.if_ended()

		if self.mission == "tutorial":

			if self.select_timer > 10:
				self.select_timer = 0
			self.select_timer += 1




			#print(self.what_now)
			if self.what_now == 1:
				self.hud.quest = "Kliknij Lewym Przyciskiem"
				self.hud.quest2 = "na Piechote po Lewej"
				self.tut_target(self.unit1)
				if self.unit1.is_selected == True:
					self.what_now = 2
					self.unit1.letter_color = (0,0,0)
			if self.what_now == 2:
				self.hud.quest = "Kliknij Prawym Przyciskiem"
				self.hud.quest2 = "na Piechote wroga"
				self.tut_target(self.unit13)
				if self.unit1.is_moving_to_fight:
					self.what_now = 3
					self.unit13.letter_color = (0,0,0)	
			if self.what_now == 3:
				self.hud.quest = "Poczekaj az ja zniszczysz"
				self.hud.quest2 = ""
				#self.tut_target(self.unit13)
				if self.unit13.hp < 5:
					self.what_now = 4
					#self.unit13.letter_color = (0,0,0)
			if self.what_now == 4:
				self.hud.quest = "Zaznacz Artylerie"
				self.hud.quest2 = ""
				self.tut_target(self.unit4)
				if self.unit4.is_selected:
					self.what_now = 5
					self.unit4.letter_color = (0,0,0)
			if self.what_now == 5:
				self.hud.quest = "Przybliz Artylerie do"
				self.hud.quest2 = "kawalerii wroga"
				#self.tut_target(self.unit4)
				pygame.draw.circle(self.screen, (100,10,10), (int(self.unit11.x_center+50),int(self.unit11.y_center+200)), self.unit9.width,3)
				self.where_to_go_rect = pygame.Rect(int(self.unit11.x_center+50-self.unit9.width),int(self.unit11.y_center+150-self.unit9.width),self.unit9.width*2,self.unit9.width*2)
				#pygame.draw.rect(self.screen,(200,0,0),self.where_to_go_rect)
				if self.unit4.rect.colliderect(self.where_to_go_rect):
					self.what_now = 6
					#self.unit4.letter_color = (0,0,0)
			if self.what_now == 6:
				self.hud.quest = "Przytrzymaj R i Kliknij"
				self.hud.quest2 = "Prawym na Kawalerie "
				self.tut_target(self.unit11)
				if self.unit4.range_attack:
					self.what_now = 7
					self.unit11.letter_color = (0,0,0)
			if self.what_now == 7:
				self.hud.quest = "Poczekaj az ja znisczysz"
				self.hud.quest2 = ""
				#self.tut_target(self.unit11)
				if self.unit11.hp < 5:
					self.what_now = 8
					self.unit11.letter_color = (0,0,0)
			if self.what_now == 8:
				self.hud.quest = "Przeciagnij kursorem nad"
				self.hud.quest2 = "pozostalymi jednostkami"
				self.tut_target(self.unit2)
				self.tut_target(self.unit3)
				self.tut_target(self.unit5)
				self.tut_target(self.unit6)
				if self.unit2.is_selected and self.unit3.is_selected and self.unit5.is_selected and self.unit6.is_selected:
					self.what_now = 9
					self.unit2.letter_color = (0,0,0)
					self.unit3.letter_color = (0,0,0)
					self.unit5.letter_color = (0,0,0)
					self.unit6.letter_color = (0,0,0)
			if self.what_now == 9:
				self.hud.quest = "Kliknij na artylerie"
				self.hud.quest2 = "wroga"
				self.tut_target(self.unit12)
				if self.unit12.hp < 5:
					self.what_now = 10
					self.unit12.letter_color = (0,0,0)
			if self.what_now == 10:
				self.hud.quest = "Poczekaj az ja znisczysz"
				self.hud.quest2 = ""
				#self.tut_target(self.unit11)
				if self.unit12.hp < 5:
					self.what_now = 11
					self.unit11.letter_color = (0,0,0)	
			if self.what_now == 11:
				self.hud.quest = "Zniszcz ostatnia"
				self.hud.quest2 = "jednostke wroga"
				self.tut_target(self.unit9)
				if self.unit9.hp < 5:
					self.what_now = 12
					self.unit9.letter_color = (0,0,0)				
		if self.mission == "torun":
			self.house_rect = pygame.Rect(37,372,77,92)
			#pygame.draw.rect(self.screen,(200,0,0),self.house_rect,1)
			#self.wall1_rect = pygame.Rect(425,60,150,327)
			#pygame.draw.rect(self.screen,(200,0,0),self.wall1_rect,1)
			for unit in self.enemy_units:
				if unit.rect.colliderect(self.house_rect):
					print('parbadum')
					self.ally_units = []
				#if unit.rect.colliderect(self.wall1_rect):
					#unit.move = False	
					#unit.mouse_point_moving(unit.x_center-1,unit.y_center-1)
		#if self.mission == "borodino":
		#	self.borodino_rect = pygame.Rect(775,333,100,100)	
		#	for unit in self.ally_units:
		#		if unit.rect.colliderect(self.borodino_rect):
		#			print('skrrrr')
					
		if self.mission == "ostrowek":
			
			self.bridge_timer += 1
			self.bridge_timer2 += 1
			if self.bridge_timer >= self.bridge_timer_max:
				if self.destroying_bridge == False:
					self.bridge_progress += 1
				self.bridge_timer = 0
			if self.bridge_progress > 24:
				self.bridge_progress = 24
			if self.bridge_timer2 < 0:
				self.bridge_timer2 = 0
			self.river_rect = pygame.Rect(290,150,140,900)
			self.bridge_rect = pygame.Rect(250,500,200,100)
			#pygame.draw.rect(self.screen,(200,0,0),self.bridge_rect,1)
			#pygame.draw.rect(self.screen,(200,0,0),self.river_rect,1)
			self.bridge_rect_progress()
			for unit in self.units:
				if unit.rect.colliderect(self.river_rect) and unit.is_selected:
					unit.x_center += 5
					#mouse_point_moving = unit.x_center
					unit.mouse_point_moving = (int(unit.x_center),int(unit.y_center))
					unit.is_moving = False

			bridge_spacing = 0
			
			for i in range(self.bridge_progress):
				#print(bridge_spacing)
				self.screen.blit(self.bridge_part,(250+bridge_spacing,500))
				bridge_spacing += 10
			if self.bridge_progress >= self.bridge_progress_max:
				self.ally_units = []


			if len(self.enemy_units) == 0:
				print(self.bridge_timer2)
				print(self.destroying_bridge)
				for unit in self.ally_units:
					if self.bridge_rect.colliderect(unit.mouse_rect):
						unit.is_moving = False
						#print(unit.mouse_pos)

						
						if unit.r_pressed  == True and unit.is_fighting == False and unit.mouse_down and unit.x_center <= 450 + unit.range:
							if unit.y_center + unit.range >= 500 or unit.y_center - unit.range <= 600:
								unit.destroying_bridge = True
									
								self.destroying_bridge = True
								if self.bridge_timer2 <= 5:
									unit.is_selected = False
									for unit in self.units:
										unit.is_selected = False
										unit.any_selected = False
								#if unit.is_moving or unit.is_moving_to_fight or unit.is_fighting:
									#destroying_bridge = False
													
									
				if self.destroying_bridge:
					self.bridge_timer2 -= 5

					#self.bridge_progress -= 1
				#print(self.destroying_bridge)








		#self.hud.update()

