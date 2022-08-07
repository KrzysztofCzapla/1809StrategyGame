import pygame
import random
import time
from hud import *
from menu import *
from text import *
from unit import *
from menu2 import *
from menu3 import *
from cutscene import *
from mission_class import *
from menu4 import *
from button_new import*
from menu5 import*
from menu6 import *
from special_cutscene import *


'''
TO DO LIST:








 


'''




pygame.init()

################# ZMIENNE #######################

###### PYGAMEOWE ######

screen_size = (1600,900)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()


loading = pygame.image.load("grafika/tlo_dwa_big.png").convert_alpha()
print("1")

pygame.display.set_caption("1809")

logo_pl_icon = pygame.image.load("grafika/logo_32.png").convert_alpha()
logo_icon = pygame.image.load("grafika/icon_white.png").convert_alpha()

pygame.display.set_icon(logo_icon)

########################

logo_pl = pygame.image.load("grafika/logo_160.png").convert_alpha()
logo_pl_unit = pygame.image.load("grafika/logo_64.png").convert_alpha()
logo_at = pygame.image.load("grafika/logo_at_160.png").convert_alpha()
logo_at_unit = pygame.image.load("grafika/logo_at_64.png").convert_alpha()

logo_fr = pygame.image.load("grafika/logo_fr_160.png").convert_alpha()
logo_fr_unit = pygame.image.load("grafika/logo_fr_64.png").convert_alpha()

logo_uk_unit = pygame.image.load("grafika/logo_uk_64.png").convert_alpha()

logo_de_unit = pygame.image.load("grafika/logo_de_64.png").convert_alpha()

tlo = pygame.image.load('grafika/tlotest.png').convert_alpha()

infantry = pygame.image.load("grafika/infantry.png").convert_alpha()
cavalry = pygame.image.load("grafika/cavalry.png").convert_alpha()
artillery = pygame.image.load("grafika/artillery.png").convert_alpha()

cutscene_0_image = pygame.image.load("grafika/cutscene_0.png").convert_alpha()
cutscene_1_image = pygame.image.load("grafika/cutscene_1.png").convert_alpha()
cutscene_2_image = pygame.image.load("grafika/cutscene_2.png").convert_alpha()
cutscene_3_image = pygame.image.load("grafika/cutscene_3.png").convert_alpha()
cutscene_4_image = pygame.image.load("grafika/cutscene_4.png").convert_alpha()
cutscene_5_image = pygame.image.load("grafika/cutscene_5.png").convert_alpha()
cutscene_6_image = pygame.image.load("grafika/cutscene_6.png").convert_alpha()
cutscene_7_image = pygame.image.load("grafika/cutscene7.png").convert_alpha()
cutscene_8_image = pygame.image.load("grafika/cutscene_8.png").convert_alpha()

fighting_icon = pygame.image.load("grafika/fight_icon.png").convert_alpha()





logo = pygame.image.load('grafika/logo.png').convert_alpha()

tut_background = pygame.image.load('grafika/tut_background.png').convert_alpha()

menu_image = pygame.image.load('grafika/menu_game.png').convert_alpha()



#all_levels = ["raszyn","praga","poludnie"]
levels = ["tutorial"]

sounds = []


units_images = [infantry,cavalry,artillery]

any_selected = False

units = []


is_paused = True
tut = True
mission_menu = False

escape_wait = 0

################ MOUSE I MENU ###########################

mouse = mouse()

menu = MENU(screen, screen_size, tlo,(81, 10, 10),"freesansbold.ttf",logo)
menu2 = MENU2(screen, screen_size, tlo,(81, 10, 10),"freesansbold.ttf",logo,levels)
opcje = MENU3(screen, screen_size, tlo,(81, 10, 10),"freesansbold.ttf",logo)
menu4 = MENU4(screen, screen_size, tlo,(81, 10, 10),"freesansbold.ttf",logo)
menu5 = MENU5(screen, screen_size, tlo,(81, 10, 10),"freesansbold.ttf",logo)
menu6 = MENU6(screen, screen_size, tlo,(81, 10, 10),"freesansbold.ttf",logo)

playlist = list()

def play_music():
		global playlist


		playlist = list()
		playlist.append ( "grafika/muzyka4.mp3" )
		playlist.append ( "grafika/muzyka3.mp3" )
		playlist.append ( "grafika/muzyka5.mp3" )
		playlist.append ( "grafika/muzyka2.mp3" )
		playlist.append ( "grafika/muzyka1.mp3" )

		pygame.mixer.music.load ( playlist.pop() )  # Get the first track from the playlist
		pygame.mixer.music.set_endevent ( pygame.USEREVENT )    # Setup the end track event
		pygame.mixer.music.play() 



		'''pygame.mixer.music.load('grafika/artillery.mp3')
		pygame.mixer.music.set_volume(0.5)
		
		pygame.mixer.music.queue('grafika/muzyka2.mp3')
		pygame.mixer.music.queue('grafika/muzyka5.mp3')
		pygame.mixer.music.queue('grafika/muzyka3.mp3')
		pygame.mixer.music.queue('grafika/muzyka4.mp3')
		pygame.mixer.music.play()'''

play_music()







################ MISJE ########################

mission = "raszyn"

#mission_raszyn1 = mission_class(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,logo_pl_unit,logo_at_unit,logo_pl,"raszyn")
#mission_praga1 = mission_class(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,logo_pl_unit,logo_at_unit,logo_pl,"praga")
#mission_poludnie1 = mission_class(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,logo_pl_unit,logo_at_unit,logo_pl,"poludnie")

############### CUTSCENES
cutscene_0 = cutscene(screen,0,0,cutscene_0_image)
cutscene_1 = cutscene(screen,0,0,cutscene_1_image)
cutscene_2 = cutscene(screen,0,0,cutscene_2_image)
cutscene_3 = cutscene(screen,0,0,cutscene_3_image)
cutscene_4 = cutscene(screen,0,0,cutscene_4_image)
cutscene_5 = cutscene(screen,0,0,cutscene_5_image)
cutscene_6 = cutscene(screen,0,0,cutscene_6_image)
cutscene_7 = cutscene(screen,0,0,cutscene_7_image)
cutscene_8 = cutscene(screen,0,0,cutscene_8_image)

################################### FUNKCJE
time.perf_counter()

def tutorial():
	global mission
	global is_paused
	global tut
	global escape_wait
	tut_color = (80,0,0)
	tut_x = 50
	tut_y = 400
	tut_y_spacing = 50
	tut_size = 40
	if mission == "raszyn":
		keys = pygame.key.get_pressed()
		if is_paused == True and tut == True:
			screen.blit(tut_background,(0,0))
			tut_title = text(screen,tut_x,tut_y-50,"Sterowanie",(60,0,0),45)
			tut_lpm = text(screen,tut_x,tut_y+tut_y_spacing,"Lewy Przycisk      - Zaznaczanie, Poruszanie, Atak",tut_color,tut_size)
			tut_r = text(screen,tut_x,tut_y+2*tut_y_spacing,"R + Lewy Przycisk - Atak Dystansowy",tut_color,tut_size)
			tut_esc = text(screen,tut_x,tut_y+3*tut_y_spacing,"Escape               - Odznaczanie",tut_color,tut_size)
			tut_skip = text(screen,tut_x,tut_y+5*tut_y_spacing,"Kliknij Escape, aby kontynuowac",(0,0,0),tut_size-10)
			if keys[pygame.K_ESCAPE]:
				escape_wait = 0
				is_paused = False
				tut = False
				time.sleep(0.2)


mouse_time = 10
mission_menu_options = False

def mission_menu_def(mouse,units,which_mission,opcje):
	global mission_menu
	global is_paused
	global is_mission_on
	global is_menu_on
	global screen
	global mission_menu_options
	global screen_size
	global mouse_time

	#if mission_menu == True and is_paused == True:
	screen.blit(tut_background,(0,0))
	screen.blit(menu_image,(screen_size[0]/2-420/2,screen_size[1]/2-600/2)) ### 420 x 600

	mission_menu_rect1 = pygame.Rect(screen_size[0]/2-420/2+120,screen_size[1]/2-600/2+210,170,80)

	mission_menu_rect2 = pygame.Rect(screen_size[0]/2-420/2+120,screen_size[1]/2-600/2+210+95,170,80)

	mission_menu_rect3 = pygame.Rect(screen_size[0]/2-420/2+120,screen_size[1]/2-600/2+210+190,170,80)

	if mission_menu_options == False:
		m_text1 = "Wznow"
		m_text2 = "Opcje"
		m_text3 = "Wyjdz"
	else:
		m_text1 = "Wstecz"
		m_text2 = "Dzwiek"
		m_text3 = "Fullscreen"

	mission_menu_text1 = text(screen,screen_size[0]/2-420/2+120+27,screen_size[1]/2-600/2+210+29,m_text1,(153, 0, 0),26)
	
	if mission_menu_options == False:
		mission_menu_text1 = text(screen,screen_size[0]/2-420/2+120+32,screen_size[1]/2-600/2+210+95+28,m_text2,(153, 0, 0),26)
	else:
		if opcje.music == 1:
			mission_menu_text1 = text(screen,screen_size[0]/2-420/2+120+32,screen_size[1]/2-600/2+210+95+28,m_text2,(20,100,30),26)
		elif opcje.music == 2:
			mission_menu_text1 = text(screen,screen_size[0]/2-420/2+120+32,screen_size[1]/2-600/2+210+95+28,m_text2,(153, 0, 0),26)

	if mission_menu_options == False:
		mission_menu_text1 = text(screen,screen_size[0]/2-420/2+120+29,screen_size[1]/2-600/2+210+190+30,m_text3,(153, 0, 0),26)
	else:
		if opcje.rozdzielczosc == 1:
			mission_menu_text1 = text(screen,screen_size[0]/2-420/2+120+29-20,screen_size[1]/2-600/2+210+190+30,m_text3,(153, 0, 0),20)
		if opcje.rozdzielczosc == 2:
			mission_menu_text1 = text(screen,screen_size[0]/2-420/2+120+29-20,screen_size[1]/2-600/2+210+190+30,m_text3,(20,100,30),20)
	#pygame.draw.rect(screen,(0,0,0),mission_menu_rect1)
	#pygame.draw.rect(screen,(0,0,0),mission_menu_rect2)
	#pygame.draw.rect(screen,(0,0,0),mission_menu_rect3)

	if units[0].mouse_down and mouse_time == 10:
		mouse_time = 0
		if mouse.rect.colliderect(mission_menu_rect1):
			if mission_menu_options == False:

		
				mission_menu = False
				is_paused = False
			else:
				mission_menu_options = False

		if mouse.rect.colliderect(mission_menu_rect2):

			if mission_menu_options == False:
				print("opcje")
				mission_menu_options = True
			else:
				if opcje.music == 1:
					opcje.music = 2
					pygame.mixer.music.pause()
				elif opcje.music == 2:
					print("music change")
					opcje.music = 1
					play_music()

		if mouse.rect.colliderect(mission_menu_rect3):
			if mission_menu_options == False:
				is_mission_on = False
				is_menu_on = True
			else:
				if opcje.rozdzielczosc == 1:
					screen = pygame.display.set_mode(screen_size,pygame.FULLSCREEN)
					opcje.rozdzielczosc = 2

				elif opcje.rozdzielczosc == 2:
					screen = pygame.display.set_mode(screen_size)
					opcje.rozdzielczosc = 1


	mouse_time += 1
	if mouse_time > 10:
		mouse_time = 10
	print(opcje.music)







is_mission_on = True
is_menu_on = True
is_game_on = True

mouse_once_pressed = False

def menu_def():
	global is_mission_on
	global is_menu_on
	global is_game_on
	global mouse_once_pressed
	global mission
	global levels
	global playlist


	menu.which_menu = 1

	escape_wait = 0

	while is_menu_on:

		mouse.update()
		
		menu2.levels = levels
		menu4.levels = levels
		menu5.levels = levels
		menu6.levels = levels
		#print(mission)
		
		#print(menu.which_menu)












		for event in pygame.event.get():
			mouse_once_pressed = False

			if event.type == pygame.QUIT:
				is_mission_on = False
				is_menu_on = False
				is_game_on = False
			if event.type == pygame.USEREVENT:
				    # A track has ended
				if len ( playlist ) > 0: 
					print("MUZAAAAAAAAAAAA")      # If there are more tracks in the queue...
					pygame.mixer.music.load( playlist.pop() )
					pygame.mixer.music.play()
					pygame.mixer.music.set_endevent ( pygame.USEREVENT )
			if event.type == pygame.MOUSEBUTTONDOWN:
				#print(menu2.levels)
				#print(menu.which_menu)
				pos = pygame.mouse.get_pos()

				if menu.which_menu == 3:
					#print(mouse.pos)
					if mouse.rect.colliderect(opcje.suwak_volume):
						if mouse.pos[0] <= 294+703 and mouse.pos[0] >= 703:
							opcje.volume_x = mouse.pos[0]

			


				if menu.which_menu == 2 and mouse_once_pressed == False:
					if mouse.rect.colliderect(przycisk1):
						print('skr')
						menu.which_menu = 4
						mouse_once_pressed = True
					if mouse.rect.colliderect(przycisk2) and len(menu2.levels) >= 4:
						print('ok')
						menu.which_menu = 5
						mouse_once_pressed = True

					if mouse.rect.colliderect(przycisk3) and len(menu2.levels) >= 7:
						menu.which_menu = 6
						mouse_once_pressed = True
				if menu.which_menu == 5 and mouse_once_pressed == False:
					if mouse.rect.colliderect(przycisk1) and len(menu2.levels) >= 4:
						is_menu_on = False
						is_mission_on = True
						is_paused = False
						mission = "ostrowek"
						mouse_once_pressed = True
						print("B)")
					if mouse.rect.colliderect(przycisk2) and len(menu2.levels) >= 5:
						is_menu_on = False
						is_mission_on = True
						mission = "torun"
						mouse_once_pressed = True
						print("B)")
					if mouse.rect.colliderect(przycisk3) and len(menu2.levels) >= 6:
						is_menu_on = False
						is_mission_on = True
						mission = "poludnie"
						mouse_once_pressed = True
						print("misja")
				if menu.which_menu == 6 and mouse_once_pressed == False:
					if mouse.rect.colliderect(przycisk1) and len(menu2.levels) >= 7:
						is_menu_on = False
						is_mission_on = True
						mission = "borodino"
						mouse_once_pressed = True
						print("B)")
					if mouse.rect.colliderect(przycisk2) and len(menu2.levels) >= 8:
						is_menu_on = False
						is_mission_on = True
						mission = "leipzig"
						mouse_once_pressed = True
					if mouse.rect.colliderect(przycisk3) and len(menu2.levels) >= 9:
						is_menu_on = False
						is_mission_on = True
						mission = "waterloo"
						mouse_once_pressed = True
				if menu.which_menu == 4 and mouse_once_pressed == False:
					if menu2.przycisk.buttonpress1(pos):
						
						is_menu_on = False
						is_mission_on = True
						mission = "tutorial"
						mouse_once_pressed = True
					if menu2.przycisk.buttonpress3(pos) and len(menu2.levels) >= 2:
						print("HMMM")
						is_menu_on = False
						is_mission_on = True
						mission = "raszyn"
						mouse_once_pressed = True
					if menu2.przycisk.buttonpress2(pos) and len(menu2.levels) >= 3:
						is_menu_on = False
						is_mission_on = True
						mission = "praga"
						mouse_once_pressed = True

						


				if menu.which_menu == 1 and mouse_once_pressed == False:
					if menu.przycisk.buttonpress1(pos):
						menu.which_menu = 2
						mouse_once_pressed = True
					if menu.button2.buttonpress3(pos):
						menu.which_menu = 3
						mouse_once_pressed = True
					if menu.button3.buttonpress2(pos):
						is_mission_on = False
						is_menu_on = False
						is_game_on = False
						mouse_once_pressed = True
				if menu.which_menu == 3 and mouse_once_pressed == False:
					if opcje.przycisk2.buttonpress1(pos):
						menu.which_menu = 1
						mouse_once_pressed = True
					if opcje.przycisk.buttonpress3(pos):
						if opcje.music == 1:
							opcje.music = 2
						elif opcje.music == 2:
							opcje.music = 1
							play_music()

						mouse_once_pressed = True
					if mouse.rect.colliderect(przycisk3) and opcje.rozdzielczosc == 1 and mouse_once_pressed == False:
						opcje.rozdzielczosc = 2
						mouse_once_pressed = True
						screen = pygame.display.set_mode(screen_size,pygame.FULLSCREEN)
					if mouse.rect.colliderect(przycisk3) and opcje.rozdzielczosc == 2 and mouse_once_pressed == False:
						opcje.rozdzielczosc = 1
						mouse_once_pressed = True
						screen = pygame.display.set_mode(screen_size)


				
		
		if menu.which_menu == 1:
			#print("bruh1")
			menu.update() 
		if menu.which_menu == 2:
			#print("bruh2")
			menu4.update()
			#
		if menu.which_menu == 3:
			#print("bruh3")
			#menu.update()
			opcje.update()
		if menu.which_menu == 4:
			menu2.update()
		if menu.which_menu == 5:
			menu5.update()
		if menu.which_menu == 6:
			menu6.update()
		if opcje.music == 2:
			#print("bruh4")
			pygame.mixer.music.stop()


		'''if menu.which_menu == 1:
			pygame.mixer.music.play(-1)	
		if menu.which_menu == 2:
			pygame.mixer.music.play(-1)
		elif menu.which_menu == 4:'''
		#print(menu.which_menu)


		keys = pygame.key.get_pressed()

		if keys[pygame.K_ESCAPE] and escape_wait == 10:
			print("escape")
			escape_wait = 0
			if menu.which_menu == 2:
				menu.which_menu = 1

			if menu.which_menu == 3:
				menu.which_menu = 1

			if menu.which_menu == 4:
				menu.which_menu = 2

			if menu.which_menu == 5:
				menu.which_menu = 2

			if menu.which_menu == 6:
				menu.which_menu = 2


		escape_wait += 1
		if escape_wait > 10:
			escape_wait = 10


		pygame.display.update()
		clock.tick(30)


def mission_def(which_mission):
	global is_mission_on
	global is_menu_on
	global is_game_on
	global any_selected
	global is_paused
	global tut
	global mission_menu
	global escape_wait
	global levels
	global playlist



	escape_wait = 0

	mission_menu = False
	is_paused = False

	which_mission.is_over = False
	which_mission.is_win = False
	if mission == "praga":
		is_paused = False
		which_mission.units = [which_mission.unit1,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6,which_mission.unit7,which_mission.unit8,which_mission.unit9,which_mission.unit10,which_mission.unit11,which_mission.unit12,which_mission.unit13,which_mission.unit14,which_mission.unit15,which_mission.unit16,which_mission.unit18,which_mission.unit17,which_mission.unit19,which_mission.unit20,which_mission.unit21,which_mission.unit22]

		which_mission.ally_units = [which_mission.unit1,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6,which_mission.unit7,which_mission.unit8,which_mission.unit19,which_mission.unit20,which_mission.unit21,which_mission.unit22]
		which_mission.enemy_units =[which_mission.unit9,which_mission.unit10,which_mission.unit11,which_mission.unit12,which_mission.unit13,which_mission.unit14,which_mission.unit15,which_mission.unit16,which_mission.unit17,which_mission.unit18,]
	if mission == "raszyn":
		is_paused = False
		which_mission.units = [which_mission.unit1,which_mission.unit2,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6,which_mission.unit7,which_mission.unit8,which_mission.unit9,which_mission.unit11,which_mission.unit12,which_mission.unit13,which_mission.unit14,which_mission.unit15,which_mission.unit16]

		which_mission.ally_units = [which_mission.unit1,which_mission.unit2,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6,which_mission.unit7,which_mission.unit8]
		which_mission.enemy_units = [which_mission.unit9,which_mission.unit11,which_mission.unit12,which_mission.unit13,which_mission.unit14,which_mission.unit15,which_mission.unit16]
	if mission == "poludnie":
		is_paused = False
		which_mission.units = [which_mission.unit1,which_mission.unit2,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6,which_mission.unit7,which_mission.unit9,which_mission.unit11,which_mission.unit12,which_mission.unit13,which_mission.unit14,which_mission.unit15,which_mission.unit16]

		which_mission.ally_units = [which_mission.unit1,which_mission.unit2,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6,which_mission.unit7]
		which_mission.enemy_units = [which_mission.unit9,which_mission.unit11,which_mission.unit12,which_mission.unit13,which_mission.unit14,which_mission.unit15,which_mission.unit16]
	if mission == "tutorial":
		is_paused = False
		which_mission.units = [which_mission.unit1,which_mission.unit2,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6,which_mission.unit9,which_mission.unit11,which_mission.unit12,which_mission.unit13]

		which_mission.ally_units = [which_mission.unit1,which_mission.unit2,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6]
		which_mission.enemy_units = [which_mission.unit9,which_mission.unit11,which_mission.unit12,which_mission.unit13]
	if mission == "ostrowek":
		is_paused = False
		which_mission.units = [which_mission.unit1,which_mission.unit2,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6,which_mission.unit9,which_mission.unit11,which_mission.unit12,which_mission.unit13,which_mission.unit14,which_mission.unit15]

		which_mission.ally_units = [which_mission.unit1,which_mission.unit2,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6]
		which_mission.enemy_units =[which_mission.unit9,which_mission.unit11,which_mission.unit12,which_mission.unit13,which_mission.unit14,which_mission.unit15]
	if mission == "torun":
		is_paused = False
		which_mission.units = [which_mission.unit1,which_mission.unit2,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6,which_mission.unit9,which_mission.unit11,which_mission.unit12,which_mission.unit13,which_mission.unit14,which_mission.unit15,which_mission.unit16,which_mission.unit18]
		which_mission.ally_units = [which_mission.unit1,which_mission.unit2,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6,which_mission.unit18]
		which_mission.enemy_units =[which_mission.unit9,which_mission.unit11,which_mission.unit12,which_mission.unit13,which_mission.unit14,which_mission.unit15,which_mission.unit16]
	if mission == "waterloo":
		is_paused = False
		which_mission.units = [which_mission.unit1,which_mission.unit2,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6,which_mission.unit7,which_mission.unit8,which_mission.unit9,which_mission.unit10,which_mission.unit11,which_mission.unit12,which_mission.unit13,which_mission.unit14]

		which_mission.ally_units = [which_mission.unit1,which_mission.unit2,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6]
		which_mission.enemy_units =[which_mission.unit7,which_mission.unit8,which_mission.unit9,which_mission.unit10,which_mission.unit11,which_mission.unit12,which_mission.unit13,which_mission.unit14]
	if mission == "borodino":
		is_paused = False
		which_mission.units = [which_mission.unit1,which_mission.unit2,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6,which_mission.unit7,which_mission.unit8,which_mission.unit9,which_mission.unit10,which_mission.unit11,which_mission.unit12,which_mission.unit13,which_mission.unit15,which_mission.unit16]

		which_mission.ally_units = [which_mission.unit1,which_mission.unit2,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6,which_mission.unit15,which_mission.unit16]
		which_mission.enemy_units =[which_mission.unit7,which_mission.unit8,which_mission.unit9,which_mission.unit10,which_mission.unit11,which_mission.unit12,which_mission.unit13]
	if mission == "leipzig":
		is_paused = False
		which_mission.units = [which_mission.unit1,which_mission.unit2,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6,which_mission.unit7,which_mission.unit8,which_mission.unit9,which_mission.unit10,which_mission.unit11,which_mission.unit12,which_mission.unit13,which_mission.unit14,which_mission.unit15,which_mission.unit16,which_mission.unit17,which_mission.unit18,which_mission.unit19]

		which_mission.ally_units = [which_mission.unit1,which_mission.unit2,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6,which_mission.unit15,which_mission.unit16,which_mission.unit19]
		which_mission.enemy_units =[which_mission.unit7,which_mission.unit8,which_mission.unit9,which_mission.unit10,which_mission.unit11,which_mission.unit12,which_mission.unit13,which_mission.unit14,which_mission.unit17,which_mission.unit18]




	keys = pygame.key.get_pressed()
	for unit in which_mission.units:
		unit.any_selected = False
	any_selected = False

	while is_mission_on == True:
		
		
		#print("B)")



		#which_mission.units = [which_mission.unit1,which_mission.unit2,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6,which_mission.unit7,which_mission.unit8,which_mission.unit9,which_mission.unit10,which_mission.unit11,which_mission.unit12,which_mission.unit13,which_mission.unit14,which_mission.unit15,which_mission.unit16]

		#which_mission.ally_units = [which_mission.unit1,which_mission.unit2,which_mission.unit3,which_mission.unit4,which_mission.unit5,which_mission.unit6,which_mission.unit7,which_mission.unit8]
		#which_mission.enemy_units = [which_mission.unit9,which_mission.unit10,which_mission.unit11,which_mission.unit12,which_mission.unit13,which_mission.unit14,which_mission.unit15,which_mission.unit16]
		#print(which_mission.is_over)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				is_mission_on = False
				is_menu_on = False
				is_game_on = False
			if event.type == pygame.USEREVENT:
				    # A track has ended
				if len ( playlist ) > 0: 
					print("MUZAAAAAAAAAAAA")      # If there are more tracks in the queue...
					pygame.mixer.music.load( playlist.pop() )
					pygame.mixer.music.play()
					pygame.mixer.music.set_endevent ( pygame.USEREVENT )





			if event.type == pygame.MOUSEBUTTONDOWN:
				print(event.button)
				for unit in which_mission.units:
					unit.mouse_down = True
				if event.button == 1:
					for unit in which_mission.units:
						unit.lmouse_down = True
				if event.button == 3:
					for unit in which_mission.units:
						unit.rmouse_down = True




			if event.type == pygame.MOUSEBUTTONUP:
				for unit in which_mission.units:
					unit.mouse_down = False
					unit.lmouse_down = False
					unit.rmouse_down = False

		mouse.update()
		if which_mission.is_over == False:
			which_mission.update()

		if is_paused == False and which_mission.is_over == False and mission_menu == False:
			which_mission.hud.update()
			#which_mission.bridge_rect_progress()

			for unit in which_mission.units:
				unit.mission = mission
				if int(unit.hp) <= 2:
					unit.is_selected = False
					unit.any_selected = False
					unit.is_idle = True
					which_mission.units.remove(unit)
					if unit in which_mission.enemy_units:
						which_mission.enemy_units.remove(unit)
					if unit in which_mission.ally_units:
						which_mission.ally_units.remove(unit)						
					any_selected = False

				unit.units = which_mission.units
				unit.ally_units = which_mission.ally_units
				unit.enemy_units = which_mission.enemy_units


				unit.update()
				if unit.is_selected == True:
					#print("1")
					any_selected = True
				if unit.escape_pressed == True:
					#print("2")
					any_selected = False
				unit.any_selected = any_selected
		#print("any2 " + str(any_selected))


		if which_mission.is_over == False:
			tutorial()



		keys = pygame.key.get_pressed()	
		#print(escape_wait)	
		if keys[pygame.K_ESCAPE] and escape_wait == 10:
			print("escape")
			escape_wait = 0

			if mission_menu:
				is_paused = False
				
				#is_paused = True
				mission_menu = False
			else:
				mission_menu = True
				is_paused = True
		escape_wait += 1
		if escape_wait > 10:
			escape_wait = 10

		if mission_menu:
			mission_menu_def(mouse,which_mission.units,which_mission,opcje)





		if which_mission.is_over == True:

			which_mission.end_screen()
			keys = pygame.key.get_pressed()
			if keys[pygame.K_SPACE]:
				is_mission_on = False
				is_menu_on = True
				if len(levels) == 8 and which_mission.mission == "leipzig" and which_mission.is_win:
					levels = ["tutorial","raszyn","praga","ostrowek","torun","poludnie","borodino","leipzig","waterloo"]
				
				if len(levels) == 7 and which_mission.mission == "borodino" and which_mission.is_win:
					levels = ["tutorial","raszyn","praga","ostrowek","torun","poludnie","borodino","leipzig"]

				if len(levels) == 6 and which_mission.mission == "poludnie" and which_mission.is_win:
					levels = ["tutorial","raszyn","praga","ostrowek","torun","poludnie","borodino"]
				elif len(levels) == 5 and which_mission.mission == "torun" and which_mission.is_win:
					levels = ["tutorial","raszyn","praga","ostrowek","torun","poludnie"]
				elif len(levels) == 4 and which_mission.mission == "ostrowek" and which_mission.is_win:
					levels = ["tutorial","raszyn","praga","ostrowek","torun"]

				if len(levels) == 3 and which_mission.mission == "praga" and which_mission.is_win:
					levels = ["tutorial","raszyn","praga","ostrowek"]				
				elif len(levels) == 2 and which_mission.mission == "raszyn" and which_mission.is_win:
					levels = ["tutorial","raszyn","praga"]
				elif len(levels) == 1 and which_mission.mission == "tutorial" and which_mission.is_win:
					levels = ["tutorial","raszyn"]

		#print(any_selected)
		pygame.display.update()
		clock.tick(30)


############################## WHILE

while is_game_on:
	with open('progress/levels.txt', 'r') as file_levels:
		levels = []
		for line in file_levels:
			levels.append(str(line.strip()))



	if is_menu_on:
		menu_def()
	if is_mission_on:


		if mission == "tutorial":
			mission_raszyn1 = mission_class(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,logo_pl_unit,logo_at_unit,logo_pl,"tutorial")
			cutscene_0.cutscene()
			mission_def(mission_raszyn1)
		if mission == "raszyn":
			mission_raszyn1 = mission_class(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,logo_pl_unit,logo_at_unit,logo_pl,"raszyn")
			cutscene_1.cutscene()
			special_raszyn = special_cutscene(screen,"raszyn")
			special_raszyn.show()
			mission_def(mission_raszyn1)
		if mission == "praga":
			mission_praga1 = mission_class(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,logo_pl_unit,logo_at_unit,logo_pl,"praga")
			cutscene_2.cutscene()
			special_praga = special_cutscene(screen,"praga")
			special_praga.show()
			mission_def(mission_praga1)
		if mission == "ostrowek":
			mission_ostrowek1 = mission_class(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,logo_pl_unit,logo_at_unit,logo_pl,"ostrowek")
			cutscene_4.cutscene()
			special_ostrowek = special_cutscene(screen,"ostrowek")
			special_ostrowek.show()
			mission_def(mission_ostrowek1)
		if mission == "poludnie":
			mission_poludnie1 = mission_class(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,logo_pl_unit,logo_at_unit,logo_pl,"poludnie")
			cutscene_3.cutscene()
			special_poludnie = special_cutscene(screen,"poludnie")
			special_poludnie.show()
			mission_def(mission_poludnie1)
		if mission == "torun":
			mission_torun1 = mission_class(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,logo_pl_unit,logo_at_unit,logo_pl,"torun")
			cutscene_5.cutscene()
			special_torun = special_cutscene(screen,"torun")
			special_torun.show()
			mission_def(mission_torun1)
		if mission == "waterloo":
			cutscene_8.cutscene()
			mission_waterloo1 = mission_class(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,logo_pl_unit,logo_at_unit,logo_pl,"waterloo")

			mission_def(mission_waterloo1)
		if mission == "borodino":
			cutscene_6.cutscene()
			mission_borodino1 = mission_class(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,logo_pl_unit,logo_at_unit,logo_pl,"borodino")

			mission_def(mission_borodino1)
		if mission == "leipzig":
			cutscene_7.cutscene()
			mission_leipzig1 = mission_class(screen,screen_size,mouse,units_images,units,fighting_icon,sounds,logo_pl_unit,logo_at_unit,logo_pl,"leipzig")
			mission_def(mission_leipzig1)
	with open('progress/levels.txt', 'w') as file_levels:
		for i in levels:
			file_levels.write(str(i)+"\n")
		




