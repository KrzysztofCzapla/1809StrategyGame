import pygame
import math
import time
from text import *

pygame.init()
pygame.mixer.init()

class mouse(pygame.sprite.Sprite):
	def __init__(self):
		self.pos = pygame.mouse.get_pos()
		self.rect = pygame.Rect(self.pos[0],self.pos[1],1,1)

	def update(self):
		self.pos = pygame.mouse.get_pos()
		self.rect = pygame.Rect(self.pos[0],self.pos[1],1,1)		



class unit(pygame.sprite.Sprite):
	def __init__(self,screen,screen_size,mouse,units_images,units,fighting_icon,sounds,mission,logo_x,logo_y,logo,faction,unit_type,name,hp):

		############ BASIC VARIABLES

		self.screen = screen
		self.logo_x = logo_x
		self.logo_y = logo_y
		self.logo = logo
		self.units_images = units_images
		self.fighting_icon = fighting_icon
		self.width = 64
		self.height = 64
		self.units = units

		self.ally_units = []
		self.enemy_units = []

		self.enemy = None
		self.sounds = sounds

		self.mission = mission

		self.waterloo_counter = 0
		self.waterloo_counter2 = 0

		############# STATS BASICS AND SZYBKSOC
		self.melee_attack = 3
		self.distant_attack = 3
		self.defense = 3
		self.range = 0
		self.v = 2
		self.moving_precision = self.v

		self.x_v = self.v
		self.y_v = self.v

		self.x_distance = 0
		self.y_distance = 0

		self.faction = faction

		if self.faction != "pl" and self.faction != "at":
			self.faction = "pl"

		self.x_vec = 0
		self.y_vec = 0	


		self.x_center = self.logo_x+self.width/2
		self.y_center = self.logo_y+self.height/2
		self.logo_x = self.x_center-32
		self.logo_y = self.y_center-32

		self.AI_point_y = 400
		self.AI_point_x = self.x_center
		############# HP
		self.hp = hp
		if self.hp > 100:
			self.hp = 100
		
		####################


		############################### HP RECT
		self.hp_background_width = self.width
		self.hp_background_height = 12
		self.hp_background_color_original = (80,20,30)
		self.hp_background_color = self.hp_background_color_original

		self.hp_background_y = 3



		self.hp_range_from_background = 2
		self.hp_width = self.width - self.hp_range_from_background
		self.hp_height = self.hp_background_height + self.hp_range_from_background
		self.hp_color = (20,100,30)
		self.hp_y = self.hp_background_y + self.hp_range_from_background
		self.hp_width = self.hp_width*self.hp/100
		##################################### 

		self.destroying_bridge = False



		self.full_width = 64
		self.full_height = self.height + self.hp_background_y + self.hp_background_height


		########### STAN JEDNOSTKI
		self.is_moving = False
		self.is_selected = False
		self.any_selected = False
		self.is_AI = False
		self.is_moving_to_fight = False
		self.is_fighting = False
		self.is_idle = True
		self.not_in_enemy = True
		####################

		######## KOLOREK SELECTU

		self.selected_color = (255, 51, 0)
		#self.rect = pygame.Rect(self.logo_x,self.logo_y,self.full_width,self.full_height)

		################



		self.no_colliding = True

		############ LETTER
		self.letter = ""
		self.letter_x = self.logo_x
		self.letter_y = self.logo_y+self.height-11
		self.letter_color = (0,0,0)
		self.letter_size = 15


		self.line_color = (0,150,0)
		self.circle_color = (0,50,0)
		self.line_attack_color = (100,0,0)
		self.circle_attack_color = (50,0,0)




		###############

		############## wysokosc hudu  

		self.hud_height = 2*10 + 160+10 #logo_pos_y*2 + logo_height + frame_width

		###############

		################# MOUSE

		self.mouse_point_moving = (int(self.x_center),int(self.y_center))
		self.mouse_pos = pygame.mouse.get_pos()
		self.mouse_rect = pygame.Rect(self.mouse_pos[0],self.mouse_pos[1],1,1)




		self.mouse_down = False
		self.lmouse_down = False
		self.rmouse_down = False



		self.mouse_x_min = 0
		self.mouse_x_max = screen_size[0]
		self.mouse_y_min = self.hud_height
		self.mouse_y_max = screen_size[1]


		###################### STATY #####################

		self.name = name

		self.unit_types = ["infantry","cavalry","artillery"]

		self.unit_type = unit_type
				
		self.hp = hp
		if self.hp > 100:
			self.hp = 100

		if unit_type == "infantry":

			self.melee_attack = 3
			self.distant_attack = 3
			self.defense = 3

			self.v = 2

			self.letter = "P"
			self.range = 200

		if unit_type == "cavalry":

			self.melee_attack = 4
			self.distant_attack = 1
			self.defense = 2

			self.v = 3

			self.letter = "K"
			self.range = 130

		if unit_type == "artillery":

			self.melee_attack = 1
			self.distant_attack = 5
			self.defense = 1

			self.v = 1

			self.letter = "A"
			self.range = 350
		#################################################
		self.x_v = self.v
		self.y_v = self.v
		#############range attack####
		self.range_attack = False
		self.distance_between = 0
		self.r_pressed = False
		self.in_range = False
		self.rpressing1 = False

		self.range_icon = pygame.image.load("grafika/range_icon.png").convert_alpha()
		self.AI_firing = False
		self.AI_firing_icon_on = False
		self.rect = pygame.Rect(self.logo_x,self.logo_y,self.full_width,self.full_height)



		self.is_fired_at = False


		############# sounds ######################


		self.play_sound = False	
		self.volume = 0.2

		#pygame.mixer.music.load('grafika/artillery.mp3')

		#self.inf_sound = pygame.mixer.Sound('grafika/infantry.wav')
		#self.art_sound = pygame.mixer.Sound('grafika/artillery.wav')
		#self.cav_sound = pygame.mixer.Sound('grafika/horse.wav')
		#self.move_sound = pygame.mixer.Sound('grafika/normal_movement.wav')
		#self.inf_sound.set_volume(self.volume)
		#self.art_sound.set_volume(self.volume-0.1)
		#self.cav_sound.set_volume(self.volume)



		self.select_rect = pygame.Rect(0,0,0,0)
		self.select_rect_pos_start_x = 0
		self.select_rect_pos_start_y = 0
		self.select_rect_pos_end_x = 0
		self.select_rect_pos_end_y = 0
		self.is_select_rect = False
		self.select_rect_timer = 0
		self.select_rect_timer_max = 4



	def draw(self):
		self.hp_width = self.width - self.hp_range_from_background
		self.hp_width = self.hp_width*self.hp/100
		if self.is_moving_to_fight == False and self.is_moving and self.is_AI == False:
			pygame.draw.line(self.screen,self.line_color,(self.x_center,self.y_center),(self.mouse_point_moving))
			pygame.draw.circle(self.screen, self.circle_color, (self.mouse_point_moving), 5)
		if self.is_moving_to_fight and self.is_idle == False and self.is_moving == False and self.is_AI == False:
			#print("bruh")
			pygame.draw.line(self.screen,self.line_attack_color,(self.x_center,self.y_center),(self.mouse_point_moving))
			pygame.draw.circle(self.screen, self.circle_attack_color, (self.mouse_point_moving), 5)
		if self.is_fighting:
			self.screen.blit(self.fighting_icon,(self.logo_x,self.logo_y-65))
		if self.range_attack or self.AI_firing:
			self.screen.blit(self.range_icon,(self.logo_x,self.logo_y-65))

		

		self.screen.blit(self.logo,(self.logo_x,self.logo_y)) #### WAZNE TUTAJ




		self.hp_background_rect = (self.logo_x,self.logo_y+self.height+self.hp_background_y,self.hp_background_width,self.hp_background_height)
		pygame.draw.rect(self.screen,self.hp_background_color,self.hp_background_rect)

		self.hp_rect = (self.logo_x + self.hp_range_from_background,self.logo_y+self.height+self.hp_y,int(self.hp_width - self.hp_range_from_background),self.hp_height - 3*self.hp_range_from_background)
		pygame.draw.rect(self.screen,self.hp_color,self.hp_rect)

		#### OZNACZENIE LITERA
		self.letter_x = self.logo_x
		self.letter_y = self.logo_y+self.height-11
		self.letter_show = text(self.screen,self.letter_x,self.letter_y,self.letter,self.letter_color,self.letter_size)



		#  DO ZAZNACZANIA, NIEWIDZIALNY RECT COLLIDE
		self.rect = pygame.Rect(self.logo_x,self.logo_y,self.full_width,self.full_height)
		pygame.draw.rect(self.screen,(0,0,0),self.rect,-1)


	def select(self):
		self.keys = pygame.key.get_pressed()
		self.mouse_pos = pygame.mouse.get_pos()
		self.mouse_rect = pygame.Rect(self.mouse_pos[0],self.mouse_pos[1],1,1)
		rect = pygame.Rect(self.logo_x,self.logo_y,self.full_width,self.full_height)

		self.collide = self.rect.colliderect(self.mouse_rect)

		for unit in self.ally_units:

			if self.mouse_rect.colliderect(unit.rect) and self.is_selected and self.lmouse_down and self.keys[pygame.K_LSHIFT] == False:
				self.is_selected = False
				unit.is_selected = True
				break


		

				



		if self.lmouse_down == False:
			#print("B)")
			self.select_rect_timer = 0
			self.is_select_rect = False
			self.select_rect_pos_start_x = self.mouse_pos[0]
			self.select_rect_pos_start_y = self.mouse_pos[1]
			self.select_rect_pos_end_x = self.mouse_pos[0]-self.select_rect_pos_start_x
			self.select_rect_pos_end_y = self.mouse_pos[1]-self.select_rect_pos_start_y
		






		self.escape_pressed = False


		#print("any "+str(self.any_selected))
		#print("sel "+str(self.is_selected))
		if self.select_rect_timer <= 0:
			if self.lmouse_down == True and self.is_AI == False: 
				
				if self.collide == True:
					

					if self.is_selected == False:
						print("CIELITO LINDO")
						self.is_selected = True


					if self.keys[pygame.K_LSHIFT]:
						self.is_selected = True





			
			if self.keys[pygame.K_ESCAPE] and self.is_selected == True:

				self.escape_pressed = True
				self.is_selected = False


			if self.keys[pygame.K_r] and self.is_selected == True:
				self.r_pressed = True
				pygame.draw.circle(self.screen, (100,0,0), (int(self.x_center),int(self.y_center)), self.range, 2)
			else:
				self.r_pressed = False


		
		if self.lmouse_down == True:
			


			if self.select_rect_timer < self.select_rect_timer_max:
				if self.mouse_rect.colliderect(self.rect) == False and self.lmouse_down == True and self.is_AI == False and self.is_selected and self.keys[pygame.K_LSHIFT] == False:
					self.is_selected = False
				self.select_rect_timer += 1
			
			if self.select_rect_timer >= self.select_rect_timer_max:
				if self.is_select_rect == False:
					self.select_rect_pos_start_x = self.mouse_pos[0]
					self.select_rect_pos_start_y = self.mouse_pos[1]

					self.select_rect_pos_end_x = 0
					self.select_rect_pos_end_y = 0

					self.is_select_rect = True
				else:
					self.select_rect_pos_end_x = self.mouse_pos[0]-self.select_rect_pos_start_x
					self.select_rect_pos_end_y = self.mouse_pos[1]-self.select_rect_pos_start_y



				self.select_rect = pygame.Rect(self.select_rect_pos_start_x,self.select_rect_pos_start_y,self.select_rect_pos_end_x,self.select_rect_pos_end_y)
				pygame.draw.rect(self.screen,(5,20,3),self.select_rect,1)
		else:
			self.is_select_rect = False

		if self.mouse_down == False:
			self.is_select_rect = False


		if self.lmouse_down == False:
			self.select_rect_timer = 0
			self.is_select_rect = False
			self.select_rect_pos_start_x = self.mouse_pos[0]
			self.select_rect_pos_start_y = self.mouse_pos[1]
			self.select_rect_pos_end_x = self.mouse_pos[0]-self.select_rect_pos_start_x
			self.select_rect_pos_end_y = self.mouse_pos[1]-self.select_rect_pos_start_y



			# DAC ZE LEWYM ZAZNACZANIE A PRAWYM CHODZENIE I ATAK
		
		def select_rect_collide():
			x1 = self.select_rect_pos_start_x
			y1 = self.select_rect_pos_start_y

			x2 = self.select_rect_pos_end_x
			y2 = self.select_rect_pos_end_y



			if x2 < 0:
				x1 = x1 + x2
				x2 = x2*(-1)
			

			if y2 < 0:
				y1 = y1 + y2
				y2 = y2*(-1)

			self.select_rect_check = pygame.Rect(x1,y1,x2,y2)
			
			#print(self.select_rect_check)
	


		select_rect_collide()








		if rect.colliderect(self.select_rect_check) and self.is_AI == False and self.is_select_rect:
			#print("abba")
			self.is_selected = True
			self.any_selected = True # NIE DZIALA BO RECT WIDTH/HEIGHT JEST NA MINUSIE
		elif self.is_select_rect and rect.colliderect(self.select_rect_check) == False and self.is_AI == False and self.is_selected:
			print("smiley face")
			self.is_selected = False 

		

		'''if self.mouse_down == True: 
			if self.collide == True:
				self.can_go = False
				if self.is_selected == False:
					self.is_selected = True







			#else:
			#	self.is_selected = False
		self.keys = pygame.key.get_pressed()

		if self.keys[pygame.K_ESCAPE] and self.is_selected == True:


			self.is_selected = False'''


		#print(self.any_selected)

		if self.is_selected == True:
			#print((self.x_center,self.y_center))
			self.hp_background_color = self.selected_color
		else:
			self.hp_background_color = self.hp_background_color_original

	def move(self):
		'''if self.is_moving == True:
			self.is_fighting = False
			self.is_moving_to_fight = False
		if self.is_moving_to_fight:
			self.is_moving = False
			self.is_fighting = False
		if self.is_fighting:
			self.is_moving = False
			self.is_moving_to_fight = False'''

		def is_mouse_in_view(self):
			self.mouse_pos = pygame.mouse.get_pos()
			if self.mouse_pos[0] >= self.mouse_x_min and self.mouse_pos[0] <= self.mouse_x_max and self.mouse_pos[1] >= self.mouse_y_min and self.mouse_pos[1] <= self.mouse_y_max:
				return True
			else:
				return False

		self.collide = self.rect.colliderect(self.mouse_rect)


		if self.is_selected == True and self.collide == False and self.rmouse_down == True and self.is_moving == False and is_mouse_in_view(self) and self.keys[pygame.K_LSHIFT] == False:

			self.mouse_point_moving = pygame.mouse.get_pos()
			self.is_moving = True
			self.is_moving_to_fight = False


			self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
			self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



			self.distance = self.x_distance + self.y_distance

			if self.distance != 0:
				self.x_vec = round(self.x_distance/self.distance,2)
				self.y_vec = round(self.y_distance/self.distance,2)	

		if self.is_moving == False or self.is_fighting == False or self.is_moving_to_fight == False:
			self.is_idle = True
		if self.is_moving == True or self.is_fighting == True or self.is_moving_to_fight == True:
			self.is_idle = False


		#print(self.full_width)
		#print(self.full_height)


		self.x_center = self.logo_x+self.width/2
		self.y_center = self.logo_y+self.height/2


		if self.is_AI == False and self.range_attack == False:#self.is_moving == True and self.is_moving_to_fight == False:
			if self.is_selected == True and self.collide == False and self.rmouse_down == True and is_mouse_in_view(self) and self.keys[pygame.K_LSHIFT] == False:

				self.mouse_point_moving = pygame.mouse.get_pos()

				self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
				self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



				self.distance = self.x_distance + self.y_distance

				if self.distance != 0:
					self.x_vec = round(self.x_distance/self.distance,3)
					self.y_vec = round(self.y_distance/self.distance,3)	


			#print(self.x_vec)
			#print("####")
			#print(self.y_vec)	

			self.moving_precision = self.v

			'''if self.logo_x+32 < self.mouse_point_moving[0]:
				#print("1")
				self.logo_x += round(self.x_v*self.x_vec,1)
			if self.logo_x+32 > self.mouse_point_moving[0]:
				#print("2")
				self.logo_x -= round(self.x_v*self.x_vec,1)
			if self.logo_y+32 > self.mouse_point_moving[1]:
				#print("3")
				self.logo_y -= round(self.y_v*self.y_vec,1)
			if self.logo_y+32 < self.mouse_point_moving[1]:
				#print("4")
				self.logo_y += round(self.y_v*self.y_vec,1)
			if self.logo_x >= self.mouse_point_moving[0]-self.moving_precision and self.logo_x <= self.mouse_point_moving[0]+self.moving_precision and self.logo_y >= self.mouse_point_moving[1]-self.moving_precision and self.logo_y <= self.mouse_point_moving[1]+self.moving_precision:
				self.is_moving = False'''


			'''if self.x_center < self.mouse_point_moving[0]:
				#print("1")
				self.logo_x += round(self.x_v*self.x_vec,2)
			if self.x_center > self.mouse_point_moving[0]:
				#print("2")
				self.logo_x -= round(self.x_v*self.x_vec,2)
			if self.y_center > self.mouse_point_moving[1]:
				#print("3")
				self.logo_y -= round(self.y_v*self.y_vec,2)
			if self.y_center < self.mouse_point_moving[1]:
				#print("4")
				self.logo_y += round(self.y_v*self.y_vec,2)
			if self.x_center >= self.mouse_point_moving[0]-self.moving_precision and self.x_center <= self.mouse_point_moving[0]+self.moving_precision and self.y_center >= self.mouse_point_moving[1]-self.moving_precision and self.y_center <= self.mouse_point_moving[1]+self.moving_precision:
				self.is_moving = False'''

			if self.x_center < self.mouse_point_moving[0]:
				#print("1")
				self.x_center += round(self.x_v*self.x_vec,1)
			if self.x_center > self.mouse_point_moving[0]:
				#print("2")
				self.x_center -= round(self.x_v*self.x_vec,1)
			if self.y_center > self.mouse_point_moving[1]:
				#print("3")
				self.y_center -= round(self.y_v*self.y_vec,1)
			if self.y_center < self.mouse_point_moving[1]:
				#print("4")
				self.y_center += round(self.y_v*self.y_vec,1)
			if self.x_center >= self.mouse_point_moving[0]-self.moving_precision and self.x_center <= self.mouse_point_moving[0]+self.moving_precision and self.y_center >= self.mouse_point_moving[1]-self.moving_precision and self.y_center <= self.mouse_point_moving[1]+self.moving_precision:
				self.is_moving = False


			self.logo_x = self.x_center-32
			self.logo_y = self.y_center-32





	def ai_moving(self):
		self.is_AI_moving = True


		self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
		self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



		self.distance = self.x_distance + self.y_distance

		if self.distance != 0:
			self.x_vec = round(self.x_distance/self.distance,3)
			self.y_vec = round(self.y_distance/self.distance,3)

	def move_to_arty(self):
		if self.unit_type == "infantry" or self.unit_type == "cavalry":
			for unit in self.units:
				if unit.faction == "pl" and unit.range_attack:
					self.distance_between = math.sqrt((unit.x_center - self.x_center)**2 + (unit.y_center - self.y_center)**2)
					if self.distance_between <= unit.range and self.is_fighting == False and self.is_fired_at:
						
						self.mouse_point_moving = (unit.x_center,unit.y_center)
						self.ai_moving()
						#self.ai_moving = True
	def mission_torun(self):
		if self.name == "Pierwsza Brygadat" or self.name == "Pierwsza Brygadat2" or self.name == "Pierwsza Brygadat3" or self.name == "Pierwsza Brygadat4" or self.name == "kirasjerzy" or self.name == "Druga Brygada" or self.name == "Piechota1":
			self.mouse_point_moving = (80,409)
			self.is_AI_moving = True


			self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
			self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



			self.distance = self.x_distance + self.y_distance

			if self.distance != 0:
				self.x_vec = round(self.x_distance/self.distance,3)
				self.y_vec = round(self.y_distance/self.distance,3)
		if self.is_fighting:
			self.AI_firing = False

		if self.AI_firing == True and self.is_fighting == False and self.is_fighting == False:
			self.AI_firing_icon_on = True
			self.distance_between = math.sqrt((self.unit_in_range.x_center - self.x_center)**2 + (self.unit_in_range.y_center - self.y_center)**2)
			if self.distance_between <= self.range and self.is_fighting == False:

				self.unit_in_range.hp = self.unit_in_range.hp - (self.distant_attack/unit.defense)*self.hp*1/1000*2
			if self.distance_between  > self.range:
				#self.mouse_point_moving = (0,900)
				self.AI_firing = False
				self.AI_firing_icon_on = False
		if self.name == "Arty1":
			self.mouse_point_moving = (500,400)
			self.is_AI_moving = True


			self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
			self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



			self.distance = self.x_distance + self.y_distance

			if self.distance != 0:
				self.x_vec = round(self.x_distance/self.distance,3)
				self.y_vec = round(self.y_distance/self.distance,3)
		
	def mission_praga(self):
		if self.name == "Druga Brygada8" or self.name == 'Druga Brygada7' or self.name == 'Druga Brygada5' or self.name == 'kirasjerzy':
			for unit in self.units:
				if unit.name == "2 Artyleria Polska":
					if unit.hp >= 10:
						self.mouse_point_moving = (unit.x_center,unit.y_center)
					if unit.hp < 10:
						if self.name == 'Druga Brygada8' or self.name == 'Druga Brygada7':
							for unit in self.units:
								if unit.name == 'Pierwsza Brygada':
									self.mouse_point_moving = (unit.x_center,unit.y_center)
						if self.name == 'Druga Brygada5' or self.name == 'kirasjerzy':
							for unit in self.units:
								if unit.name == 'Artyleria Polska':
									self.mouse_point_moving = (unit.x_center,unit.y_center)



			self.is_AI_moving = True


			self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
			self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



			self.distance = self.x_distance + self.y_distance

			if self.distance != 0:
				self.x_vec = round(self.x_distance/self.distance,3)
				self.y_vec = round(self.y_distance/self.distance,3)
		if self.name == 'Druga Brygada4' or self.name == 'Pierwsza Brygadat':
			self.mouse_point_moving = (1400,710)
			self.is_AI_moving = True


			self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
			self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



			self.distance = self.x_distance + self.y_distance

			if self.distance != 0:
				self.x_vec = round(self.x_distance/self.distance,3)
				self.y_vec = round(self.y_distance/self.distance,3)
		if self.name == 'Dywizja Kawaleriii' or self.name == 'Dywizja Kawalerii2':
			for unit in self.units:
				if unit.name == 'Trzecia Brygada':
					print('kondominium')
					self.mouse_point_moving = (unit.x_center,unit.y_center)
			self.is_AI_moving = True


			self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
			self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



			self.distance = self.x_distance + self.y_distance
			if self.distance != 0:
				self.x_vec = round(self.x_distance/self.distance,3)
				self.y_vec = round(self.y_distance/self.distance,3)
		if self.name == 'Artyleria Polska5':
			self.mouse_point_moving = (1000, 500)
			self.is_AI_moving = True


			self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
			self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



			self.distance = self.x_distance + self.y_distance
			if self.distance != 0:
				self.x_vec = round(self.x_distance/self.distance,3)
				self.y_vec = round(self.y_distance/self.distance,3)
		if self.name == 'Druga Brygad11':
			self.mouse_point_moving = (1370, 700)
			self.is_AI_moving = True


			self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
			self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



			self.distance = self.x_distance + self.y_distance
			if self.distance != 0:
				self.x_vec = round(self.x_distance/self.distance,3)
				self.y_vec = round(self.y_distance/self.distance,3)

		if self.unit_type == "artillery" and self.is_moving == False:
			for unit in self.units:
				if unit.faction == "pl":
					self.distance_between = math.sqrt((unit.x_center - self.x_center)**2 + (unit.y_center - self.y_center)**2)
					if self.distance_between <= self.range and self.is_fighting == False:
						self.unit_in_range = unit
						self.AI_firing = True
						self.AI_firing_icon_on = True
					else:
						self.AI_firing_icon_on = False
					
		if self.is_fighting:
			self.AI_firing = False

		if self.AI_firing == True and self.is_fighting == False and self.is_fighting == False:
			self.AI_firing_icon_on = True
			self.distance_between = math.sqrt((self.unit_in_range.x_center - self.x_center)**2 + (self.unit_in_range.y_center - self.y_center)**2)
			if self.distance_between <= self.range and self.is_fighting == False:

				self.unit_in_range.hp = self.unit_in_range.hp - (self.distant_attack/unit.defense)*self.hp*1/1000*2
			if self.distance_between  > self.range:
				#self.mouse_point_moving = (0,900)
				self.AI_firing = False
				self.AI_firing_icon_on = False
			if self.unit_in_range.hp <= 0:
				self.AI_firing = False
				self.AI_firing_icon_on = False


	def mission_raszynm(self):
		#print("bruh")
		if self.name == "kirasjerzy" or self.name == "Dywizja Kawalerii" or self.name == "Druga Brygada2":
			'''self.AI_point_y = self.AI_point_y + 10
			self.AI_point_x = self.AI_point_x + -1'''

			#if int(self.x_center) < 380:
			for unit in self.units:
				if unit.name == "1 Pulk Piechoty":
					self.mouse_point_moving = (unit.x_center,unit.y_center)
					#print(self.mouse_point_moving)
					#print(unit.hp)
				elif unit.hp < 10:
					if self.name == "kirasjerzy":
						self.mouse_point_moving = (650, 800)
					elif self.name == "Dywizja Kawalerii":
						self.mouse_point_moving = (600, 790)
					elif self.name == "Druga Brygada2":
						self.mouse_point_moving = (630, 850)

					#print(self.mouse_point_moving)						

			self.is_AI_moving = True


			self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
			self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



			self.distance = self.x_distance + self.y_distance

			if self.distance != 0:
				self.x_vec = round(self.x_distance/self.distance,3)
				self.y_vec = round(self.y_distance/self.distance,3)
		elif self.name == 'Druga Brygada':
			'''self.AI_point_y = self.AI_point_y + 10
			self.AI_point_x = self.AI_point_x + -1'''

			for unit in self.units:
				if unit.name == "Artyleria Polska":
					self.mouse_point_moving = (unit.x_center,unit.y_center)
				elif unit.hp < 10:
					self.mouse_point_moving = (400,800)
			self.is_AI_moving = True


			self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
			self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



			self.distance = self.x_distance + self.y_distance

			if self.distance != 0:
				self.x_vec = round(self.x_distance/self.distance,3)
				self.y_vec = round(self.y_distance/self.distance,3)
		elif self.name == 'Pierwsza Brygadat':
			#print('ez')
			for unit in self.units:
				if unit.name == "Pierwsza Brygada":
					self.mouse_point_moving = (unit.x_center,unit.y_center)
					#print(self.mouse_point_moving)
				elif unit.hp < 10:
					self.mouse_point_moving = (500,800)
			self.is_AI_moving = True

			self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
			self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



			self.distance = self.x_distance + self.y_distance
			if self.distance != 0:
				self.x_vec = round(self.x_distance/self.distance,3)
				self.y_vec = round(self.y_distance/self.distance,3)

		if self.unit_type == "artillery" and self.is_moving == False:
			for unit in self.units:
				if unit.faction == "pl":
					self.distance_between = math.sqrt((unit.x_center - self.x_center)**2 + (unit.y_center - self.y_center)**2)
					if self.distance_between <= self.range and self.is_fighting == False:
						self.unit_in_range = unit
						self.AI_firing = True
						self.AI_firing_icon_on = True
					else:
						self.AI_firing_icon_on = False
					
		if self.is_fighting:
			self.AI_firing = False

		if self.AI_firing == True and self.is_fighting == False and self.is_fighting == False:
			self.AI_firing_icon_on = True
			self.distance_between = math.sqrt((self.unit_in_range.x_center - self.x_center)**2 + (self.unit_in_range.y_center - self.y_center)**2)
			if self.distance_between <= self.range and self.is_fighting == False:

				self.unit_in_range.hp = self.unit_in_range.hp - (self.distant_attack/unit.defense)*self.hp*1/1000*2
			if self.distance_between  > self.range:
				#self.mouse_point_moving = (0,900)
				self.AI_firing = False
				self.AI_firing_icon_on = False
			#self.enemy_selected.hp = self.enemy_selected.hp - (self.distant_attack/unit.defense)*self.hp*1/1000
		#print("firing "+str(self.AI_firing))
		#print("fighting "+str(self.is_fighting))


	def mission_poludnie(self):
		if self.unit_type == "artillery" and self.is_moving == False:
			for unit in self.units:
				if unit.faction == "pl":
					self.distance_between = math.sqrt((unit.x_center - self.x_center)**2 + (unit.y_center - self.y_center)**2)
					if self.distance_between <= self.range and self.is_fighting == False:
						self.unit_in_range = unit
						self.AI_firing = True
						self.AI_firing_icon_on = True
					else:
						self.AI_firing_icon_on = False
					
		if self.is_fighting:
			self.AI_firing = False

		if self.AI_firing == True and self.is_fighting == False and self.is_fighting == False:
			self.AI_firing_icon_on = True
			self.distance_between = math.sqrt((self.unit_in_range.x_center - self.x_center)**2 + (self.unit_in_range.y_center - self.y_center)**2)
			if self.distance_between <= self.range and self.is_fighting == False:

				self.unit_in_range.hp = self.unit_in_range.hp - (self.distant_attack/unit.defense)*self.hp*1/1000*2
			if self.distance_between  > self.range:
				#self.mouse_point_moving = (0,900)
				self.AI_firing = False
				self.AI_firing_icon_on = False


		if self.name == "K1":
			self.mouse_point_moving = (1000,430)
			self.ai_moving()
			#print(self.is_moving)
		if self.name == "K2":
			self.mouse_point_moving = (1000,700)
			self.ai_moving()
		if self.name == "P1":

			#self.mouse_point_moving = (300,400)
			self.ai_moving()
		if self.name == "P2":
			#self.mouse_point_moving = (300,400)
			self.ai_moving()
		if self.name == "P3":
			#self.mouse_point_moving = (300,400)
			self.ai_moving()
		if self.name == "A1":
			self.mouse_point_moving = (900,400)
			self.ai_moving()
		if self.name == "A2":
			self.mouse_point_moving = (800,500)
			self.ai_moving()


	def mission_tutorial(self):
		if self.unit_type == "artillery" and self.is_moving == False:
			for unit in self.units:
				if unit.faction == "pl":
					self.distance_between = math.sqrt((unit.x_center - self.x_center)**2 + (unit.y_center - self.y_center)**2)
					if self.distance_between <= self.range and self.is_fighting == False:
						self.unit_in_range = unit
						self.AI_firing = True
						self.AI_firing_icon_on = True
					else:
						self.AI_firing_icon_on = False
					
		if self.is_fighting:
			self.AI_firing = False

		if self.AI_firing == True and self.is_fighting == False and self.is_fighting == False:
			self.AI_firing_icon_on = True
			self.distance_between = math.sqrt((self.unit_in_range.x_center - self.x_center)**2 + (self.unit_in_range.y_center - self.y_center)**2)
			if self.distance_between <= self.range and self.is_fighting == False:

				self.unit_in_range.hp = self.unit_in_range.hp - (self.distant_attack/unit.defense)*self.hp*1/1000*2
			if self.distance_between  > self.range:
				#self.mouse_point_moving = (0,900)
				self.AI_firing = False
				self.AI_firing_icon_on = False

	def mission_ostrowek(self):
		if self.unit_type == "artillery" and self.is_moving == False:
			for unit in self.units:
				if unit.faction == "pl":
					self.distance_between = math.sqrt((unit.x_center - self.x_center)**2 + (unit.y_center - self.y_center)**2)
					if self.distance_between <= self.range and self.is_fighting == False:
						self.unit_in_range = unit
						self.AI_firing = True
						self.AI_firing_icon_on = True
					else:
						self.AI_firing_icon_on = False
					
		if self.is_fighting:
			self.AI_firing = False

		if self.AI_firing == True and self.is_fighting == False and self.is_fighting == False:
			self.AI_firing_icon_on = True
			self.distance_between = math.sqrt((self.unit_in_range.x_center - self.x_center)**2 + (self.unit_in_range.y_center - self.y_center)**2)
			if self.distance_between <= self.range and self.is_fighting == False:

				self.unit_in_range.hp = self.unit_in_range.hp - (self.distant_attack/unit.defense)*self.hp*1/1000*2
			if self.distance_between  > self.range:
				#self.mouse_point_moving = (0,900)
				self.AI_firing = False
				self.AI_firing_icon_on = False

		if self.name == "Piechota1":
			self.mouse_point_moving = (1100,self.y_center)
			self.ai_moving()
		if self.name == "Arty1":
			self.mouse_point_moving = (800,650)
			self.ai_moving()
	def mission_leipzig(self):
		if self.name == "P1" or self.name == "P2" or self.name == "K1":
			for unit in self.units:
				if unit.name == "1 Pulk Piechoty":
					if unit.hp >= 10:
						self.mouse_point_moving = (unit.x_center,unit.y_center)
					if unit.hp < 10:
						for unit in self.units:
							if unit.name == "Artyleria Polska":
								self.mouse_point_moving = (unit.x_center,unit.y_center)
			self.is_AI_moving = True


			self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
			self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



			self.distance = self.x_distance + self.y_distance

			if self.distance != 0:
				self.x_vec = round(self.x_distance/self.distance,3)
				self.y_vec = round(self.y_distance/self.distance,3)
		if self.name == "K2" or self.name == "P3" or self.name == "K3":
			for unit in self.units:
				if unit.name == "Dywizja Kawalerii4":
					self.mouse_point_moving = (unit.x_center,unit.y_center)
			self.is_AI_moving = True


			self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
			self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



			self.distance = self.x_distance + self.y_distance

			if self.distance != 0:
				self.x_vec = round(self.x_distance/self.distance,3)
				self.y_vec = round(self.y_distance/self.distance,3)
		if self.name == "Dywizja Kawalerii" or self.name == "Dywizja Kawalerii2":
			for unit in self.units:
				if unit.name == "Druga Brygada":
					self.mouse_point_moving = (unit.x_center,unit.y_center)
			self.is_AI_moving = True


			self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
			self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



			self.distance = self.x_distance + self.y_distance

			if self.distance != 0:
				self.x_vec = round(self.x_distance/self.distance,3)
				self.y_vec = round(self.y_distance/self.distance,3)



		if self.unit_type == "artillery" and self.is_moving == False:
			for unit in self.units:
				if unit.faction == "pl":
					self.distance_between = math.sqrt((unit.x_center - self.x_center)**2 + (unit.y_center - self.y_center)**2)
					if self.distance_between <= self.range and self.is_fighting == False:
						self.unit_in_range = unit
						self.AI_firing = True
						self.AI_firing_icon_on = True
					else:
						self.AI_firing_icon_on = False
					
		if self.is_fighting:
			self.AI_firing = False

		if self.AI_firing == True and self.is_fighting == False and self.is_fighting == False:
			self.AI_firing_icon_on = True
			self.distance_between = math.sqrt((self.unit_in_range.x_center - self.x_center)**2 + (self.unit_in_range.y_center - self.y_center)**2)
			if self.distance_between <= self.range and self.is_fighting == False:

				self.unit_in_range.hp = self.unit_in_range.hp - (self.distant_attack/unit.defense)*self.hp*1/1000*2
			if self.distance_between  > self.range:
				#self.mouse_point_moving = (0,900)
				self.AI_firing = False
				self.AI_firing_icon_on = False
			if self.unit_in_range.hp <= 0:
				self.AI_firing = False
				self.AI_firing_icon_on = False


	def mission_borodinon(self):
		if self.name == "P3" or self.name == "P1" or self.name == "K3":
			for unit in self.units:
				if unit.name == "Dywizja Kawalerii":
					print('ok')
					self.mouse_point_moving = (unit.x_center,unit.y_center)
			self.is_AI_moving = True


			self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
			self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



			self.distance = self.x_distance + self.y_distance

			if self.distance != 0:
				self.x_vec = round(self.x_distance/self.distance,3)
				self.y_vec = round(self.y_distance/self.distance,3)

		if self.is_fighting:
			self.AI_firing = False
		if self.unit_type == "artillery" and self.is_moving == False:
			for unit in self.units:
				if unit.faction == "pl":
					self.distance_between = math.sqrt((unit.x_center - self.x_center)**2 + (unit.y_center - self.y_center)**2)
					if self.distance_between <= self.range and self.is_fighting == False:
						self.unit_in_range = unit
						self.AI_firing = True
						self.AI_firing_icon_on = True
					else:
						self.AI_firing_icon_on = False

		if self.AI_firing == True and self.is_fighting == False and self.is_fighting == False:
			self.AI_firing_icon_on = True
			self.distance_between = math.sqrt((self.unit_in_range.x_center - self.x_center)**2 + (self.unit_in_range.y_center - self.y_center)**2)
			if self.distance_between <= self.range and self.is_fighting == False:

				self.unit_in_range.hp = self.unit_in_range.hp - (self.distant_attack/unit.defense)*self.hp*1/1000*2
			if self.distance_between  > self.range:
				#self.mouse_point_moving = (0,900)
				self.AI_firing = False
				self.AI_firing_icon_on = False

	def mission_waterloo(self):
		if self.unit_type == "artillery" and self.is_moving == False:
			for unit in self.units:
				if unit.faction == "pl":
					self.distance_between = math.sqrt((unit.x_center - self.x_center)**2 + (unit.y_center - self.y_center)**2)
					if self.distance_between <= self.range and self.is_fighting == False:
						self.unit_in_range = unit
						self.AI_firing = True
						self.AI_firing_icon_on = True
					else:
						self.AI_firing_icon_on = False
					
		if self.is_fighting:
			self.AI_firing = False

		if self.AI_firing == True and self.is_fighting == False and self.is_fighting == False:
			self.AI_firing_icon_on = True
			self.distance_between = math.sqrt((self.unit_in_range.x_center - self.x_center)**2 + (self.unit_in_range.y_center - self.y_center)**2)
			if self.distance_between <= self.range and self.is_fighting == False:

				self.unit_in_range.hp = self.unit_in_range.hp - (self.distant_attack/unit.defense)*self.hp*1/1000*2
			if self.distance_between  > self.range:
				#self.mouse_point_moving = (0,900)
				self.AI_firing = False
				self.AI_firing_icon_on = False

		if self.name == "P1" or self.name == "P2" or self.name == "A1" or self.name == "K1" or self.name == "K2":
			self.waterloo_counter2 = 4001
			self.waterloo_counter += 1
			if self.waterloo_counter < 200 and self.is_fighting != True:
				self.mouse_point_moving = [self.x_center+5,self.y_center+2]
			self.ai_moving()
			print(self.waterloo_counter)

		if self.name == "P3" or self.name == "A2" or self.name == "K3":
			print(self.waterloo_counter)
			self.waterloo_counter += 1
			if self.waterloo_counter >= 400 and self.waterloo_counter <= 720 and self.is_fighting == False:
				print("larry")
				self.mouse_point_moving = [self.x_center-2,self.y_center+0.5]
				#self.waterloo_counter += 1
				


			self.ai_moving()


			
		



	def AI(self):

		if self.faction == "at" or self.faction == "uk" or self.faction == "de":
			for unit in self.units:
				if self.rect.colliderect(unit.rect) and unit.is_AI == False and self.is_AI == True:
					self.is_fighting = True

			#print(self.mouse_point_moving)
			#self.mouse_point_moving = (400,400)
			#self.mouse_point_moving = (self.x_center,10)
			self.is_AI = True
			self.is_AI_moving = False
			#self.mouse_point_moving = [self.x_center,self.y_center]




			if self.mission == "raszyn":
				self.mission_raszynm()
			if self.mission == "poludnie":
				self.mission_poludnie()
				self.move_to_arty()
			if self.mission == "praga":
				self.mission_praga()
			if self.mission == "tutorial":
				self.mission_tutorial()
			if self.mission == "ostrowek":
				self.mission_ostrowek()
				self.move_to_arty()
			if self.mission == "torun":
				self.mission_torun()
			if self.mission == "waterloo":
				self.mission_waterloo()
				self.move_to_arty()
			if self.mission == "borodino":
				self.mission_borodinon()
				self.move_to_arty()
			if self.mission == "leipzig":
				self.mission_leipzig()
				self.move_to_arty()

				#if self.unit_type == "cavalry":
				#print("bruh")
				'''if self.unit_type == "cavalry":
					self.AI_point_y = self.AI_point_y + 10
					self.AI_point_x = self.AI_point_x + -1

					#if int(self.x_center) < 380:
					for unit in self.units:
						if unit.name == "2 Pulk Ulanow":
							self.mouse_point_moving = (unit.x_center,unit.y_center)

					self.is_AI_moving = True

					#print(self.mouse_point_moving)

					self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
					self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



					self.distance = self.x_distance + self.y_distance

					if self.distance != 0:
						self.x_vec = round(self.x_distance/self.distance,3)
						self.y_vec = round(self.y_distance/self.distance,3)'''






				'''for unit in self.units:
					self.rect = pygame.Rect(self.logo_x,self.logo_y,self.full_width,self.full_height)
					unit.rect = pygame.Rect(unit.logo_x,unit.logo_y,unit.full_width,unit.full_height)
				

				if unit.is_AI == False and self.is_AI_moving == False and unit.is_fighting == False:

					self.is_AI_moving = True
					#self.mouse_point_moving = (int(unit.x_center),int(unit.y_center))

					print(self.mouse_point_moving)

					self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
					self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



					self.distance = self.x_distance + self.y_distance

					if self.distance != 0:
						self.x_vec = round(self.x_distance/self.distance,3)
						self.y_vec = round(self.y_distance/self.distance,3)	'''






			for unit in self.units:
				if self.rect.colliderect(unit.rect) and unit.is_AI == False:
					self.is_fighting = True


			#
			if self.is_fighting == False:
				if self.x_center < self.mouse_point_moving[0]:
					#self.is_moving = True
					#print("1")
					self.x_center += round(self.x_v*self.x_vec,1)
				if self.x_center > self.mouse_point_moving[0]:
					#self.is_moving = True
					#print("2")
					self.x_center -= round(self.x_v*self.x_vec,1)
				if self.y_center > self.mouse_point_moving[1]:
					#self.is_moving = True
					#print("3")
					self.y_center -= round(self.y_v*self.y_vec,1)
				if self.y_center < self.mouse_point_moving[1]:
					#self.is_moving = True
					#print("4")
					self.y_center += round(self.y_v*self.y_vec,1)

				if self.x_center >= self.mouse_point_moving[0]-self.moving_precision and self.x_center <= self.mouse_point_moving[0]+self.moving_precision and self.y_center >= self.mouse_point_moving[1]-self.moving_precision and self.y_center <= self.mouse_point_moving[1]+self.moving_precision:
					self.is_moving = False
				else:
					self.is_moving = True









				self.logo_x = self.x_center-32
				self.logo_y = self.y_center-32
				self.x_center = int(self.x_center)
				self.y_center = int(self.y_center)
					
				
			

	def combat(self):
		self.mouse_pos = pygame.mouse.get_pos()

		for unit in self.units:
			

			unit.is_fighting = False
			self.rect = pygame.Rect(self.logo_x,self.logo_y,self.full_width,self.full_height)
			unit.rect = pygame.Rect(unit.logo_x,unit.logo_y,unit.full_width,unit.full_height)
			self.mouse_over_enemy = self.mouse_rect.colliderect(unit.rect)
			if self.mouse_rect.colliderect(unit.rect) and self.rmouse_down and unit.is_AI == True and self.is_selected:
				#print("bruh momento?")
				self.is_moving = False
				self.is_moving_to_fight = True
				self.is_fighting = False

				self.mouse_point_moving = pygame.mouse.get_pos()
			if self.rect.colliderect(unit.rect) and unit.is_AI and self.is_AI == False:
				self.is_moving = False
				self.is_moving_to_fight = False
				self.is_fighting = True
				unit.is_fighting = True
				self.mouse_point_moving = (self.x_center,self.y_center)
				#self.not_in_enemy = False
				

				#print("I FIGHT")
			if self.rect.colliderect(unit.rect) == False:
				self.is_fighting = False
			if self.is_fighting and self.AI_firing == False:
				#print(unit.hp)
				#print("I FIGHT")
				if self.hp >= 0 and unit.hp >= 0:
					self.hp = self.hp - unit.melee_attack*unit.hp*1/1000
					unit.hp = unit.hp - self.melee_attack*self.hp*1/1000
				#print (self.hp)
				self.screen.blit(self.fighting_icon,(self.logo_x,self.logo_y-65))
				self.screen.blit(self.fighting_icon,(unit.logo_x,unit.logo_y-65))

			if self.range_attack == True:
				self.is_moving_to_fight == False


			if self.is_moving_to_fight == True:
				self.range_attack = False
			if self.is_moving:
				self.range_attack = False


			'''if self.mouse_down == True and self.mouse_over_enemy:
				self.enemy_selected = True'''
			if self.mouse_rect.colliderect(unit.rect):

				#print(self.enemy_selected)
				if self.r_pressed  == True and unit.is_AI == True and self.is_fighting == False and self.rmouse_down:
					self.enemy_selected = unit
					self.distance_between = math.sqrt((self.enemy_selected.x_center - self.x_center)**2 + (self.enemy_selected.y_center - self.y_center)**2)
					if self.range >= self.distance_between:

						self.range_attack = True

						




					'''self.is_moving_to_fight = False
					self.distance_between = math.sqrt((unit.x_center - self.x_center)**2 + (unit.y_center - self.y_center)**2)
					if self.range >= self.distance_between:
					#print ('pog')
						unit.hp = unit.hp - (self.distant_attack/unit.defense)*self.hp*1/1000'''

				#if self.unit_type == "infantry":
					#self.sounds[2].play(0,5)

			if self.range_attack == True:
				self.enemy_selected.is_fired_at = False

				self.play_sound = True
					
				self.is_moving_to_fight = False
				self.distance_between = math.sqrt((self.enemy_selected.x_center - self.x_center)**2 + (self.enemy_selected.y_center - self.y_center)**2)
				if self.range >= self.distance_between:
				#print ('pog')
					
					self.enemy_selected.hp = self.enemy_selected.hp - (self.distant_attack/self.enemy_selected.defense)*self.hp*1/1000/len(self.units)*2
					self.enemy_selected.is_fired_at = True
				if int(self.enemy_selected.hp) <= 2:
					self.range_attack = False
					self.mouse_point_moving = (int(self.x_center),int(self.y_center))


		







			#print(unit.x_center)





		if self.is_moving_to_fight == True and self.is_moving == False:
			self.is_moving = False
			self.range_attack = False
			#self.is_idle = False
			

			self.moving_precision = self.v


			self.x_distance = int(math.fabs(self.x_center-self.mouse_point_moving[0]))
			self.y_distance = int(math.fabs(self.y_center-self.mouse_point_moving[1]))



			self.distance = self.x_distance + self.y_distance

			'''if self.distance != 0:
				self.x_vec = round(self.x_distance/self.distance,3)
				self.y_vec = round(self.y_distance/self.distance,3)

			if self.x_center < self.mouse_point_moving[0]:
				#print("1")
				self.x_center += round(self.x_v*self.x_vec,1)
			if self.x_center > self.mouse_point_moving[0]:
				#print("2")
				self.x_center -= round(self.x_v*self.x_vec,1)
			if self.y_center > self.mouse_point_moving[1]:
				#print("3")
				self.y_center -= round(self.y_v*self.y_vec,1)
			if self.y_center < self.mouse_point_moving[1]:
				#print("4")
				self.y_center += round(self.y_v*self.y_vec,1)
			if self.x_center >= self.mouse_point_moving[0]-self.moving_precision and self.x_center <= self.mouse_point_moving[0]+self.moving_precision and self.y_center >= self.mouse_point_moving[1]-self.moving_precision and self.y_center <= self.mouse_point_moving[1]+self.moving_precision:
				self.is_moving = False

			self.logo_x = self.x_center-32
			self.logo_y = self.y_center-32'''






	def update(self):

		#pygame.mixer.music.play()

		#self.rect = pygame.Rect(self.logo_x,self.logo_y,self.full_width,self.full_height)
		self.AI()

		self.draw()
		self.select()

		if self.destroying_bridge == False:
			self.move()
		self.combat()
		if self.is_fighting:
			self.range_attack = False


		'''if self.is_selected:

			#print("mouse_point_moving: " + str(self.mouse_point_moving))
			print("fighting: " + str(self.is_fighting))
			print("r: " + str(self.r_pressed))
			print("range attack "+str(self.range_attack))
			print("moving to fight: " + str(self.is_moving_to_fight))
			print("moving : " + str(self.is_moving))'''
