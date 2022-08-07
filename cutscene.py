import pygame

pygame.init()

class cutscene(pygame.sprite.Sprite):
	def __init__(self,screen,x,y,image):
		self.screen = screen
		self.x = x
		self.y = y
		self.image = image

		self.is_space_pressed = False
		self.clock = pygame.time.Clock()


	def cutscene(self):

		while self.is_space_pressed == False:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.is_space_pressed = True


			self.keys = pygame.key.get_pressed()
			if self.keys[pygame.K_SPACE]:
				self.is_space_pressed = True
			else:
				self.screen.blit(self.image,(self.x,self.y))



			pygame.display.update()
			self.clock.tick(30)


		