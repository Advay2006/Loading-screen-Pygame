import pygame, sys, random

#BG = pygame.image.load("assets/Background.png")
BG = pygame.image.load("mt.jpg")

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
			
class ParticlePrinciple:
	def __init__(self):
		self.particles = []

	def emit(self):
		if self.particles:
			self.delete_particles()
			for particle in self.particles:
				particle[0][1] += particle[2][0]
				particle[0][0] += particle[2][1]
				particle[1] -= 0.2
				pygame.draw.circle(screen,pygame.Color('White'),particle[0], int(particle[1]))

	def add_particles(self):
		pos_x = pygame.mouse.get_pos()[0]
		pos_y = pygame.mouse.get_pos()[1] 
		radius = 10
		direction_x = random.randint(-3,3)
		direction_y = random.randint(-3,3)
		particle_circle = [[pos_x,pos_y],radius,[direction_x,direction_y]]
		self.particles.append(particle_circle)

	def delete_particles(self):
		particle_copy = [particle for particle in self.particles if particle[1] > 0]
		self.particles = particle_copy

'''
class ParticleStar:
	def __init__(self):
		self.particles = []
		self.surface = pygame.image.load('Star.jpg').convert_alpha()
		self.width = self.surface.get_rect().width
		self.height = self.surface.get_rect().height

	def emit(self):
		if self.particles:
			self.delete_particles()
			for particle in self.particles:
				particle[0].x += particle[1]
				particle[0].y += particle[2]
				particle[3] -= 0.2
				screen.blit(self.surface,particle[0])

	def add_particles(self):
		pos_x = pygame.mouse.get_pos()[0] - self.width / 2
		pos_y = pygame.mouse.get_pos()[1] - self.height / 2
		direction_x = random.randint(-3,3)
		direction_y = random.randint(-3,3)
		lifetime = random.randint(4,10)
		particle_rect = pygame.Rect(int(pos_x),int(pos_y),self.width,self.height)
		self.particles.append([particle_rect,direction_x,direction_y,lifetime])

	def delete_particles(self):
		particle_copy = [particle for particle in self.particles if particle[3] > 0]
		self.particles = particle_copy
		
'''

pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Menu")

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
particle1 = ParticlePrinciple()

#nyan_surface = pygame.image.load('nyan_cat.png').convert_alpha()
#particle2 = ParticleNyan()

#particle3 = ParticleStar()

PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT,40)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Exan-Regular.ttf", size)

def getanother_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("thefont.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        screen.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("#4f5752")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()





def main_menu():
    while True:
        screen.blit(BG, (0, 0))
        #screen.fill((30,30,30))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = getanother_font(100).render("Space Jam", True, "#a1320d")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 160))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 350), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="#19ff9f")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Play Rectn.png"), pos=(640, 480), 
                            text_input="OPTIONS", font=get_font(35), base_color="#d7fcd4", hovering_color="#19ff9f")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Play Rectn.png"), pos=(640, 580), 
                            text_input="QUIT", font=get_font(35), base_color="#d7fcd4", hovering_color="#19ff9f")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == PARTICLE_EVENT:
                particle1.add_particles()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        particle1.emit()
        pygame.display.update()
        clock.tick(120)

main_menu()
'''
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == PARTICLE_EVENT:
			particle1.add_particles()
			#particle3.add_particles()

	
	particle1.emit()
	
	#particle3.emit()
	pygame.display.update()
'''
	