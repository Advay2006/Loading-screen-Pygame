import pygame
import math

pygame.init()

WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Planet Simulation")

WIDTH, HEIGHT = WIN.get_size()

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
LIGHT_GREY = (200, 200, 200)
GREEN = (50, 188, 39)
BLACK = (0, 0, 0)

FONT = pygame.font.SysFont("comicsans", 16)


class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU  # 1AU = 100 pixels
    TIMESTEP = 3600 * 24  # 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)

        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun / 1000, 1)}km", 1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2))

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))


# SIMULATOR RECTANGLES
menu = (WIDTH - WIDTH // 5, HEIGHT // 24, WIDTH // 6, HEIGHT // 2)  # X, Y, WIDTH, HEIGHT
menur = pygame.Rect(menu[0], menu[1], menu[2], menu[3])
mass = (menu[0] + menu[2] // 6, menu[1] + (menu[3])//6, (menu[2] * 2) // 3, menu[3] // 10)
massr = pygame.Rect(mass[0], mass[1], mass[2], mass[3])
radius = (menu[0] + menu[2] // 6, menu[1] + (menu[3]*2) // 6, (menu[2] * 2) // 3, menu[3] // 10)
radiusr = pygame.Rect(radius[0], radius[1], radius[2], radius[3])
colour = (menu[0] + menu[2] // 6, menu[1] + (menu[3] * 3) // 6, (menu[2] * 2) // 3, menu[3] // 10)
colourr = pygame.Rect(colour[0], colour[1], colour[2], colour[3])
velocity = (menu[0] + menu[2] // 6, menu[1] + (menu[3] * 4) // 6, (menu[2] * 2) // 3, menu[3] // 10)
velr = pygame.Rect(velocity[0], velocity[1], velocity[2], velocity[3])
drop = (menu[0] + menu[2] // 6, menu[1] + (menu[3] * 5) // 6, (menu[2] * 2) // 3, menu[3] // 10)
dropr = pygame.Rect(drop[0], drop[1], drop[2], drop[3])
rectlist = [[massr, 'mass'], [radiusr, 'radius'], [colourr, 'colour'], [velr, 'velocity'], [dropr, 'drop']]
currentobj = {'mass': 'MASS', 'radius': 'RADIUS', 'colour': 'COLOUR', 'velocity': 'VELOCITY', 'drop': 'drop'}


def sim(mas='MASS', rad='RADIUS', col='COLOUR', vel='VELOCITY'):

    headfont = pygame.font.SysFont('arial', 30)
    childfont = pygame.font.SysFont('arial', 20)

    # MENU SURFACE
    pygame.draw.rect(WIN, WHITE, menur, 0, 10)
    head = headfont.render('SIMULATOR', True, DARK_GREY)
    WIN.blit(head, (menu[0] + menu[2] // 2 - head.get_width() // 2, menu[1] + head.get_height() // 2))

    # ELEMENTS
    pygame.draw.rect(WIN, LIGHT_GREY, massr, 0, 10)
    head = childfont.render(mas, True, DARK_GREY)
    WIN.blit(head, (mass[0] + mass[2] // 2 - head.get_width() // 2, mass[1] + head.get_height() // 2))

    pygame.draw.rect(WIN, LIGHT_GREY, radiusr, 0, 10)
    head = childfont.render(rad, True, DARK_GREY)
    WIN.blit(head, (radius[0] + radius[2] // 2 - head.get_width() // 2, radius[1] + head.get_height() // 2))

    pygame.draw.rect(WIN, LIGHT_GREY, colourr, 0, 10)
    head = childfont.render(col, True, DARK_GREY)
    WIN.blit(head, (colour[0] + colour[2] // 2 - head.get_width() // 2, colour[1] + head.get_height() // 2))

    pygame.draw.rect(WIN, LIGHT_GREY, velr, 0, 10)
    head = childfont.render(vel, True, DARK_GREY)
    WIN.blit(head, (velocity[0] + velocity[2] // 2 - head.get_width() // 2, velocity[1] + head.get_height() // 2))

    pygame.draw.rect(WIN, GREEN, dropr, 0, 10)
    head = childfont.render('DROP!', True, BLACK)
    WIN.blit(head, (drop[0] + drop[2] // 2 - head.get_width() // 2, drop[1] + head.get_height() // 2))


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10 ** 30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10 ** 24)
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10 ** 23)
    mars.y_vel = 24.077 * 1000

    mercury = Planet(0.387 * Planet.AU, 0, 8, LIGHT_GREY, 3.30 * 10 ** 23)
    mercury.y_vel = -47.4 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10 ** 24)
    venus.y_vel = -35.02 * 1000

    #planets = [sun, earth, mars, mercury, venus]
    planets = []
    active_rect = None
    drop_active = False
    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))
        x, y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                if active_rect:
                    if event.key == pygame.K_BACKSPACE:
                        currentobj[active_rect[1]] = currentobj[active_rect[1]][:-1]
                        if currentobj[active_rect[1]] == '':
                            currentobj[active_rect[1]] = active_rect[1].upper()
                    else:
                        if active_rect[1] == currentobj[active_rect[1]].lower():
                            currentobj[active_rect[1]] = ''
                        currentobj[active_rect[1]] += event.unicode
            elif event.type == pygame.MOUSEBUTTONUP:

                for rect in rectlist:
                    if rect[0].collidepoint(float(x), float(y)):
                        if currentobj[rect[1]] == 'drop':
                            drop_active = True
                        active_rect = rect
                        if currentobj[active_rect[1]] == active_rect[1].upper():
                            currentobj[active_rect[1]] = ''
                        break
                    else:
                        if currentobj[rect[1]] == '':
                            currentobj[rect[1]] = rect[1].upper()
                else:
                    active_rect = None
                    if drop_active:
                        drop_active = False
                        new_planet = Planet((x - WIDTH // 2) / 250 * Planet.AU, (y - HEIGHT // 2) / 250 * Planet.AU, int(currentobj['radius']), eval(currentobj['colour']), eval(currentobj['mass']))
                        new_planet.y_vel = eval(currentobj['velocity'])
                        planets.append(new_planet)

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)
        sim(currentobj['mass'], currentobj['radius'], currentobj['colour'], currentobj['velocity'])

        pygame.display.update()

    pygame.quit()


main()