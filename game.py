import pygame, planet

def realToGameCoor(orbitalPoints):
    #  this function will take all the orbital
    #  points of a planet and output that same
    #  list as coordinates pygame can understand
    output = []
    scale = planet.Planet.scale
    for coordinate in orbitalPoints:
        x = coordinate[0] * scale
        y = coordinate[1] * scale
        output.append((x, y))
    return output

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
    earth = planet.Planet(blue, 
                        5.972e24, 
                        W/(2*scale), 
                        H/(2*scale), 
                        radius=6371e3 * 10 * scale)
    moon = planet.Planet(grey, 
                        7.348e22, 
                        W/(2*scale), 
                        384.4e6 + H/(2*scale), 
                        1022, 
                        radius=1737e3 * 10 * scale)

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
            if len(entity.orbit) > 1:
                orbit = realToGameCoor(entity.orbit)
                pygame.draw.lines(screen, entity.color, False, orbit, 1)
            entity.updatePosition()
        
        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()