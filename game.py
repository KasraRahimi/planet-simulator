import pygame, planet

def main():
    blue = (30, 42, 156)
    grey = (59, 59, 64)
    black = (0, 0, 0)
    W, H = 16 * 60, 9 * 60
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Planet simulation")

    scale = planet.Planet.scale
    earth = planet.Planet(blue, 5.972e24, W/(2*scale), H/(2*scale), radius=20)
    moon = planet.Planet(grey, 7.348e22, W/(2*scale), 384.4e6 + H/(2*scale), 1022)

    running = True
    while running:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for entity in planet.Planet.planets:
            x = entity.x * scale
            y = entity.y * scale
            pygame.draw.circle(screen, entity.color, (x, y), entity.radius)
            entity.updatePosition()
        
        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()