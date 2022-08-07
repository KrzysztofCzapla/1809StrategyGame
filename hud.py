import pygame
import random
import time
from text import *


pygame.init()

class HUD(pygame.sprite.Sprite):
	def __init__(self,screen,screen_size,logo,units,unit,quest="Bruh momento n numero dos"):
		self.start_time = time.perf_counter()

		self.time = int(time.perf_counter())
		self.time = int(self.time - self.start_time)

		#self.time_text = time.perf_counter()

		self.x = 0
		self.y = 0
		self.screen = screen
		self.width = screen_size[0]
		self.height = screen_size[1]

		self.font_color = (1,1,1)

		self.unit = unit
		self.time_text = 0

		############## background i frame'y
		self.logo = logo
		self.logo_pos_x = 30 # odleglosc od boków kwadratu
		self.logo_pos_y = 10 # -||- tylko w y, jakby cos sie mialo zmienic
		self.logo_width = 160
		self.logo_height = 160
		self.background_color = (61, 37, 24)
		self.frame_color = (1,1,1)
		self.backogrund_rect_size = (self.width,self.logo_pos_y*2+self.logo_height) #ustawienie wielkości kwadratu wokół loga
		self.backogrund_rect = pygame.Rect((self.x,self.y),self.backogrund_rect_size) # sam kwadrat
		# Obramowanie
		self.frame_width = 10 # grubosc obramowek

		self.logo_rect_width = self.logo_width+self.logo_pos_x*2 # wymairy loga
		self.logo_rect_height = self.logo_height+self.logo_pos_y*2

		self.third_frame_x = self.width/2 # x trzeciego paska
		self.fourth_frame_x = self.width*5/6 # x czwartego paska



		##################### quest zone #####################
		self.quest_title_text_x = self.third_frame_x+20
		self.quest_title_text_y = 15
		self.quest = str(quest)
		self.quest2 = ""
		self.quest_title_color = (118,17,17)
		self.quest_title_size = 32

		self.quest_desc_text_x = self.third_frame_x+20
		self.quest_desc_text_y = 50
		self.quest_desc_size = 25

		#####################################

		self.units = units

		self.unit_type_text = ""
		
		self.stats_x = self.logo_rect_width + 20#20
		self.stats_y = self.quest_title_text_y#self.quest_title_text_y+ self.logo_rect_height + 20
		self.stats_name_spacing = 30
		self.stats_type_spacing = 5
		self.stats_spacing = 20


		self.stats_size_name = 29
		self.stats_size_type = 28
		self.stats_size_stats = 25

		self.stats_x_space = 280

		self.stats_words_color = (118,17,17)
		self.stats_numbers_color = (118,17,17)

		self.hud_background = pygame.image.load("grafika/hud_tlo.png").convert_alpha()


		###########################
	def draw(self):
		##### LOGO PART ###############
		'''
		pygame.draw.rect(self.screen,self.background_color,self.backogrund_rect) # rysowanie tla
		

		# obramówka
		pygame.draw.rect(self.screen,self.frame_color,self.backogrund_rect,self.frame_width) # ogolna
		pygame.draw.rect(self.screen,self.frame_color,((self.logo_rect_width,0),(self.frame_width,self.logo_rect_height)))# boczna po logo

		pygame.draw.rect(self.screen,self.frame_color,((self.third_frame_x,0),(self.frame_width,self.logo_rect_height))) # 3 pasek
		pygame.draw.rect(self.screen,self.frame_color,((self.fourth_frame_x,0),(self.frame_width,self.logo_rect_height))) # 4 pasek
		'''

		#### NAPISY
		self.screen.blit(self.hud_background,(0,0))

		self.screen.blit(self.logo,(self.logo_pos_x,self.logo_pos_y)) # rysowanie loga

		self.quest_text_title = text(self.screen,self.x+self.quest_title_text_x,self.y+self.quest_title_text_y,"Zadanie:",self.quest_title_color,self.quest_title_size)
		self.quest_text_desc = text(self.screen,self.x+self.quest_desc_text_x,self.y+self.quest_desc_text_y,str(self.quest),self.quest_title_color,self.quest_desc_size)
		self.quest_text_desc2 = text(self.screen,self.x+self.quest_desc_text_x,self.y+self.quest_desc_text_y+25,str(self.quest2),self.quest_title_color,self.quest_desc_size)
		#print(pygame.font.get_fonts())

		########## STATY JEDNOSTEK #########

		self.m_attack = self.unit.melee_attack
		self.d_attack = self.unit.distant_attack
		self.defense = self.unit.defense
		self.v = self.unit.v
		self.unit_type = self.unit.unit_type

		self.unit_name = self.unit.name


		if self.unit_type == "infantry":

			self.unit_type_text = "Piechota"


		if self.unit_type == "cavalry":

			self.unit_type_text = "Kawaleria"

		if self.unit_type == "artillery":

			self.unit_type_text = "Artyleria"				


		if self.unit.is_selected == True:

			self.unit_name_text = text(self.screen,self.stats_x,self.stats_y,str(self.unit_name),self.stats_words_color,self.stats_size_name)
			self.unit_type_text = text(self.screen,self.stats_x,self.stats_y+self.stats_name_spacing,self.unit_type_text,self.stats_words_color,self.stats_size_type)

			self.unit_type_text = text(self.screen,self.stats_x,self.stats_y+3*self.stats_spacing+self.stats_type_spacing,"Atak",self.stats_words_color,self.stats_size_stats)
			self.unit_type_text = text(self.screen,self.stats_x+self.stats_x_space,self.stats_y+3*self.stats_spacing+self.stats_type_spacing,str(self.m_attack),self.stats_numbers_color,self.stats_size_stats)


			self.unit_type_text = text(self.screen,self.stats_x,self.stats_y+4*self.stats_spacing+self.stats_type_spacing,"Atak Dyst.",self.stats_words_color,self.stats_size_stats)
			self.unit_type_text = text(self.screen,self.stats_x+self.stats_x_space,self.stats_y+4*self.stats_spacing+self.stats_type_spacing,str(self.d_attack),self.stats_numbers_color,self.stats_size_stats)

			self.unit_type_text = text(self.screen,self.stats_x,self.stats_y+5*self.stats_spacing+self.stats_type_spacing,"Obrona",self.stats_words_color,self.stats_size_stats)
			self.unit_type_text = text(self.screen,self.stats_x+self.stats_x_space,self.stats_y+5*self.stats_spacing+self.stats_type_spacing,str(self.defense),self.stats_numbers_color,self.stats_size_stats)

			self.unit_type_text = text(self.screen,self.stats_x,self.stats_y+6*self.stats_spacing+self.stats_type_spacing,"Predkosc",self.stats_words_color,self.stats_size_stats)
			self.unit_type_text = text(self.screen,self.stats_x+self.stats_x_space,self.stats_y+6*self.stats_spacing+self.stats_type_spacing,str(self.v),self.stats_numbers_color,self.stats_size_stats)


			##### STATY OBRAZKI ####
			if self.unit_type == "infantry":

				#self.unit_type_text = "Piechota"

				self.image_width = 50
				self.image_height = 160
				self.image_x = self.stats_x + 500
				self.image_y = self.stats_y -5
				self.images_spacing = 20
				self.screen.blit(self.unit.units_images[0],(self.image_x,self.image_y))
				self.screen.blit(self.unit.units_images[0],(self.image_x-self.images_spacing-self.image_width,self.image_y))
				self.screen.blit(self.unit.units_images[0],(self.image_x-2*self.images_spacing-2*self.image_width,self.image_y))
			if self.unit_type == "cavalry":

				#self.unit_type_text = "Kawaleria"

				self.image_width = 150
				self.image_height = 160
				self.image_x = self.stats_x + 350
				self.image_y = self.stats_y -5
				self.images_spacing = 20
				self.screen.blit(self.unit.units_images[1],(self.image_x,self.image_y))
			if self.unit_type == "artillery":

				#self.unit_type_text = "Artyleria"

				self.image_width = 215
				self.image_height = 159
				self.image_x = self.stats_x + 340
				self.image_y = self.stats_y -5
				self.images_spacing = 20
				self.screen.blit(self.unit.units_images[2],(self.image_x,self.image_y))

		####################### CZAS
		more_than_10 = 0
		self.time_title = text(self.screen,self.fourth_frame_x+60-10,self.logo_rect_height/2-75,"Czas:",self.quest_title_color,50)
		self.time = int(time.perf_counter())
		self.time = int(self.time - self.start_time)
		self.time_text = str(int(self.time))
		if int(self.time) >= 10:
			more_than_10 = 10
		elif int(self.time) >= 100:
			more_than_10 = 20
		self.time1 = text(self.screen,self.fourth_frame_x+(self.width-self.fourth_frame_x)/2-15-more_than_10,self.logo_rect_height/2-15,self.time_text,self.quest_title_color,50)
		#self.time_text = 0 		




	def update(self):
		for unit in self.units:
			if unit.is_selected == True:
				self.unit = unit
		self.draw()
		#print(self.unit.unit_type)



##KOLORKI:  88 44 44, 75 26 22, 105 65 44, 61 37 24, 32 19 13