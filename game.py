import pygame, planet

# ~ simple color list ~
blue = (0,0,255)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
navy = (0, 0, 150)
green = (0, 128, 0)
grey = (128, 128, 128)
yellow = (255,215,0)
orange = (255,140,0)
khaki = (240,230,140)
# =====================

def realToGameCoor(orbitalPoints, W, H):
    #  this function will take all the orbital
    #  points of a planet and output that same
    #  list as coordinates pygame can understand
    output = []
    scale = planet.Planet.scale
    for coordinate in orbitalPoints:
        x = coordinate[0] * scale + W/2
        y = coordinate[1] * scale + H/2
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

    sun = planet.Planet(
        yellow,
        1.989e30,
        0,
        0,
        radius=15
    )

    mercury = planet.Planet(
        grey,
        33e22,
        57.9e9,
        0,
        dy=47.9e3,
        radius=3
    )

    venus = planet.Planet(
        khaki,
        4.87e24,
        108.2e9,
        0,
        dy=36e3,
        radius=5
    )

    earth = planet.Planet(
        blue,
        5.9736e24,
        149.6e9,
        0,
        dy=29.8e3,
        radius=6
    )

    mars = planet.Planet(
        red,
        642e21,
        228e9,
        0,
        dy=24.1e3,
        radius=4
    )

    jupiter = planet.Planet(
        orange,
        1898e24,
        778.5e9,
        0,
        dy=13.1e3,
        radius=10
    )

    running = True
    while running:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for entity in planet.Planet.planets:
            x = entity.x * scale + W/2
            y = entity.y * scale + H/2
            pygame.draw.circle(screen, entity.color, (x, y), entity.radius)
            if len(entity.orbit) > 1:
                orbit = realToGameCoor(entity.orbit, W, H)
                pygame.draw.lines(screen, entity.color, False, orbit, 1)
            entity.updatePosition()
        
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()