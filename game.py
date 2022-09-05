import pygame, planet

def main():
    blue = (30, 42, 156)
    grey = (59, 59, 64)
    black = (0, 0, 0)
    W, H = 16 * 40, 9 * 40
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Planet simulation")

    scale = planet.Planet.scale
    earth = planet.Planet(blue, 5.972e24, 0, 0, radius=30)
    moon = planet.Planet(grey, 7.348e22, 0, 384.4e6, 1022)

    while 1:
        screen.fill(black)
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                quit()
        for entity in planet.Planet.planets:
            x = entity.x * scale
            y = entity.y * scale
            pygame.draw.circle(screen, entity.color, (x, y), entity.radius)
            entity.updatePosition()
        
        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()