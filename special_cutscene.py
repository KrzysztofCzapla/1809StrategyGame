import pygame
from text import *

pygame.init()

class special_cutscene(pygame.sprite.Sprite):
	def __init__(self,screen,mission):
		self.screen = screen
		self.mission = mission

		self.is_space_pressed = False
		self.clock = pygame.time.Clock()
		self.pl_unit = pygame.image.load("grafika/logo_32.png").convert_alpha()
		self.at_unit = pygame.image.load("grafika/logo_at_32.png").convert_alpha()
		#if self.mission == "raszyn":
		self.inf_sound = pygame.mixer.Sound('grafika/infantry.wav')
		self.image = pygame.image.load("grafika/ksiestwo2.png").convert_alpha()
		self.image1 = pygame.image.load("grafika/ksiestwo2.png").convert_alpha()

		self.stage = 1
		self.stage_timer = 0
		self.x = 0 
		self.y = 0
		self.x_scale = 0
		self.y_scale = 0
		self.scale = 0
		self.scale_prop = 1.777777777
		self.at_y = 0

	def show(self):
		while self.is_space_pressed == False:
			#print(self.x_scale)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.is_space_pressed = True


			self.keys = pygame.key.get_pressed()
			if self.keys[pygame.K_SPACE]:
				self.is_space_pressed = True
			else:
				if self.mission == "raszyn":
					self.screen.blit(self.image1,(self.x-self.x_scale/2,self.y-int(self.y_scale/1.5)))


					if self.stage == 1:
						self.text = text(self.screen,20,30,"Ksiestwo Warszawskie",(31,4,4),50)
						self.text2 = text(self.screen,20,75,"1809 rok",(31,4,4),50)
						self.stage_timer += 2
						if self.stage_timer >= 100:
							self.stage_timer = 0
							self.stage = 2

					if self.stage == 2:
						if self.x_scale < 700:
							self.scale = 5
							self.x_scale += int(self.scale*self.scale_prop)
							self.y_scale += self.scale
							self.image1 = pygame.transform.scale(self.image, (1600+self.x_scale,900+self.y_scale))
						else:
							self.stage = 3

					if self.stage == 3:
						self.screen.blit(self.pl_unit,(950,480))
						self.screen.blit(self.pl_unit,(985,500))
						self.screen.blit(self.at_unit,(850,720))
						self.screen.blit(self.at_unit,(800,700))
						self.stage_timer += 2
						if self.stage_timer >= 30:
							self.stage_timer = 0
							self.stage = 4

					if self.stage == 4:
						print(self.at_y)
						self.quick_v = 3
						if self.at_y < 120:
							self.at_y += self.quick_v
							self.screen.blit(self.pl_unit,(950,480))
							self.screen.blit(self.pl_unit,(985,500))

							self.screen.blit(self.at_unit,(850,720-self.at_y))
							self.screen.blit(self.at_unit,(800,700-self.at_y))
						else:
							self.stage = 5
							self.quick_v = 0						
					if self.stage == 5:
						if self.quick_v < 50:
							self.quick_v += 2
						else:
							self.inf_sound.play(0,2000)
							for i in range(100):
								print("wait")
								
								self.is_space_pressed = True

						self.screen.blit(self.pl_unit,(950-self.quick_v,480+self.quick_v))
						self.screen.blit(self.pl_unit,(985-self.quick_v,500+self.quick_v))

						self.screen.blit(self.at_unit,(850+self.quick_v,600-self.quick_v))
						self.screen.blit(self.at_unit,(800+self.quick_v,600-self.quick_v))




				if self.mission == "praga":
					self.scale = 700
					self.screen.blit(self.image1,(self.x-self.x_scale/2,self.y-int(self.y_scale/1.5)))


					if self.stage == 1:
						self.stage = 2

					if self.stage == 2:
						
						self.x_scale = int(self.scale*self.scale_prop)
						self.y_scale = self.scale
						self.image1 = pygame.transform.scale(self.image, (1600+self.x_scale,900+self.y_scale))
					
						self.stage = 3

					if self.stage == 3:
						self.spacing = 90
						self.screen.blit(self.pl_unit,(950,480))
						self.screen.blit(self.pl_unit,(985,500))
						self.screen.blit(self.at_unit,(950-self.spacing,480+self.spacing))
						self.screen.blit(self.at_unit,(985-self.spacing,500+self.spacing))
						self.stage_timer += 2
						if self.stage_timer >= 30:
							self.stage_timer = 0
							self.stage = 4

					if self.stage == 4:
						print(self.stage)
						self.quick_v = 3
						if self.at_y < 100:
							self.at_y += self.quick_v
							self.screen.blit(self.pl_unit,(950+self.at_y/3,480-self.at_y/3))
							self.screen.blit(self.pl_unit,(985+self.at_y/3,500-self.at_y/3))

							self.screen.blit(self.at_unit,(950-self.spacing+self.at_y/9,480+self.spacing-self.at_y/9))
							self.screen.blit(self.at_unit,(985-self.spacing+self.at_y/9,500+self.spacing-self.at_y/9))
						else:
							self.stage = 5
							self.quick_v = 0
					if self.stage == 5:
						self.quick_v = 9
						if self.at_y < 850:
							self.at_y += self.quick_v
							self.screen.blit(self.pl_unit,(950+102/3,480-102/3))
							self.screen.blit(self.pl_unit,(985+102/3,500-102/3))
							self.screen.blit(self.at_unit,(950-self.spacing+self.at_y/9,480+self.spacing-self.at_y/9))
							self.screen.blit(self.at_unit,(985-self.spacing+self.at_y/9,500+self.spacing-self.at_y/9))
						else:
							self.stage = 6


					if self.stage == 6:
						
						self.inf_sound.play(0,2000)
						for i in range(100):
							print("wait")
								
							self.is_space_pressed = True

				if self.mission == "ostrowek":
					self.scale = 700
					self.screen.blit(self.image1,(self.x-self.x_scale/2,self.y-int(self.y_scale/1.5)))


					if self.stage == 1:
						self.stage = 2

					if self.stage == 2:
						
						self.x_scale = int(self.scale*self.scale_prop)
						self.y_scale = self.scale
						self.image1 = pygame.transform.scale(self.image, (1600+self.x_scale,900+self.y_scale))
					
						self.stage = 3

					if self.stage == 3:
						self.spacing = 35
						self.screen.blit(self.pl_unit,(960,470))
						self.screen.blit(self.pl_unit,(995+20,490))
						self.screen.blit(self.at_unit,(960-self.spacing,470+self.spacing))
						self.screen.blit(self.at_unit,(995-self.spacing,490+self.spacing))
						self.stage_timer += 2
						if self.stage_timer >= 30:
							self.stage_timer = 0
							self.stage = 4

					if self.stage == 4:
						print(self.stage)
						self.quick_v = 3
						if self.at_y < 300:
							self.at_y += self.quick_v
							self.screen.blit(self.pl_unit,(960,470))
							self.screen.blit(self.pl_unit,(995+20,490))

							self.screen.blit(self.at_unit,(960-self.spacing,470+self.spacing))
							self.screen.blit(self.at_unit,(995-self.spacing+self.at_y/9,490+self.spacing+self.at_y/3))
						else:
							self.stage = 5
							self.at_y = 0
					if self.stage == 5:
						self.quick_v = 4

						if self.at_y < 400:
							self.at_y += self.quick_v
							self.screen.blit(self.pl_unit,(960,470))
							self.screen.blit(self.pl_unit,(995+20+self.at_y/12,490+self.at_y/4))

							self.screen.blit(self.at_unit,(960-self.spacing,470+self.spacing))
							self.screen.blit(self.at_unit,(995-self.spacing+300/9+self.at_y/18,490+self.spacing+300/3-self.at_y/18))
						else:
							self.stage = 6


					if self.stage == 6:
						
						self.inf_sound.play(0,2000)
						for i in range(100):
							print("wait")
								
							self.is_space_pressed = True


				if self.mission == "poludnie":
					self.scale = 700
					self.screen.blit(self.image1,(self.x-self.x_scale/2,self.y-int(self.y_scale/1.5)))


					if self.stage == 1:
						self.stage = 2

					if self.stage == 2:
						
						self.x_scale = int(self.scale*self.scale_prop)
						self.y_scale = self.scale
						self.image1 = pygame.transform.scale(self.image, (1600+self.x_scale,900+self.y_scale))
					
						self.stage = 3

					if self.stage == 3:
						self.spacing = 35
						self.screen.blit(self.pl_unit,(1150,600))
						self.screen.blit(self.pl_unit,(1200,590))
						self.screen.blit(self.at_unit,(1240,700))
						self.screen.blit(self.at_unit,(1300,750))
						self.stage_timer += 2
						if self.stage_timer >= 30:
							self.stage_timer = 0
							self.stage = 4

					if self.stage == 4:
						#print(self.at)
						self.quick_v = 3
						if self.at_y < 200:
							self.at_y += self.quick_v
							self.screen.blit(self.pl_unit,(1150+self.at_y/3,600+self.at_y/3))
							self.screen.blit(self.pl_unit,(1200+self.at_y/9,590+self.at_y/3))

							self.screen.blit(self.at_unit,(1240,700))
							self.screen.blit(self.at_unit,(1300-self.at_y/9,750-self.at_y/9))
						else:
							self.stage = 6
							self.at_y = 0


					if self.stage == 6:
						
						self.inf_sound.play(0,2000)
						for i in range(100):
							print("wait")
								
							self.is_space_pressed = True

				if self.mission == "torun":
					self.scale = 700
					self.screen.blit(self.image1,(self.x-self.x_scale/2,self.y-int(self.y_scale/1.5)))


					if self.stage == 1:
						self.stage = 2

					if self.stage == 2:
						
						self.x_scale = int(self.scale*self.scale_prop)
						self.y_scale = self.scale
						self.image1 = pygame.transform.scale(self.image, (1600+self.x_scale,900+self.y_scale))
					
						self.stage = 3

					if self.stage == 3:
						self.spacing = 35
						self.screen.blit(self.pl_unit,(630,320))
						#self.screen.blit(self.pl_unit,(1200,590))
						self.screen.blit(self.at_unit,(550,350))
						self.screen.blit(self.at_unit,(600,400))
						self.stage_timer += 2
						if self.stage_timer >= 30:
							self.stage_timer = 0
							self.stage = 4

					if self.stage == 4:
						#print(self.at)
						self.quick_v = 3
						if self.at_y < 60:
							self.at_y += self.quick_v
							self.screen.blit(self.pl_unit,(630,320))
							

							self.screen.blit(self.at_unit,(550+self.at_y,350-self.at_y/4))
							self.screen.blit(self.at_unit,(600+self.at_y/4,400-self.at_y))
						else:
							self.stage = 6
							self.at_y = 0


					if self.stage == 6:
						
						self.inf_sound.play(0,2000)
						for i in range(100):
							print("wait")
								
							self.is_space_pressed = True


			pygame.display.update()
			self.clock.tick(30)
