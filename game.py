import pygame, planet

def main():
    blue = (30, 42, 156)
    grey = (59, 59, 64)
    WIDTH, HEIGHT = 16 * 40, 9 * 40
    pygame.init()
    pygame.display.set_caption("Planet simulation")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    earth = planet.Planet(blue, 5.972e24, WIDTH/2, HEIGHT/2, radius=10)
    moon = planet.Planet(grey, 7.348e22, WIDTH/2, HEIGHT/2 - 384.4e6, 1022)

    while 1:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()

if __name__ == '__main__':
    main()