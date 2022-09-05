class Planet:
    scale = 3 / 1e7
    timestep = 60 * 60
    G = 6.6743e-11
    planets = []  # lists of planets that keep track of each one

    def __init__(self, color, mass, x, y, dx=0, dy=0, radius=5):
        # assigning all the properties a planet needs
        self.color = color
        self.mass = mass
        self.x = x
        self.y = y
        self.dx = dx  # derivative of position (i.e. speed)
        self.dy = dy  # derivative of position (i.e. speed)
        self.radius = radius
        self.ddx = 0  # derivative of speed (i.e. acceleration)
        self.ddy = 0  # derivative of speed (i.e. acceleration)
        self.planets.append(self)
        self.orbit = []  # a list of points in the planet's orbit
        # to be able to display it in game
    
    @property
    def speed(self):
        # magnitude of the velocity vector
        return (self.dx**2 + self.dy**2)**(1/2)
    
    def calculateDistance(self, other, vector=False):
        # calculating the distance between a planet and
        # another and allowing the output to be a either
        # a scalar or a vector depending on need
        deltax = other.x - self.x
        deltay = other.y - self.y
        if vector:
            return deltax, deltay
        else:
            # my good friend Pythagoras taught me this trick ;)
            return (deltax**2 + deltay**2)**(1/2)
    
    def calculateForce(self, other, vector=False):
        # this method allows one to find the force between two planets
        # and allows the output to be given as a scalar
        # or as a vector
        m1 = self.mass
        m2 = other.mass
        r = self.calculateDistance(other)
        fg = (self.G * m1 * m2) / r**2  # My buddy Issac taught me this one ;)
        if vector:
            # soh cah toa go brrr
            deltax, deltay = self.calculateDistance(other, True)
            hypotenuse = self.calculateDistance(other)
            return fg * (deltax/hypotenuse), fg * (deltay/hypotenuse)
        else:
            return fg
    
    def updatePosition(self):
        # this method calculates the force between a given
        # planet and all its neighbors. It then finds the
        # total force acting on the planet and calculates
        # its acceleration. With the acceleration it will
        # update the speed and position of the planet.
        fx = 0
        fy = 0
        for entity in self.planets:
            if entity == self:
                continue
            else:
                fx += self.calculateForce(entity, True)[0]
                fy += self.calculateForce(entity, True)[1]
        self.ddx = fx / self.mass # thank you, Issac!
        self.ddy = fy / self.mass
        self.dx += self.ddx * self.timestep
        self.dy += self.ddy * self.timestep
        self.x += self.dx * self.timestep
        self.y += self.dy * self.timestep
        self.orbit.append((self.x, self.y))