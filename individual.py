import math

# load indice refraction file
indice_refraction_temp = {}
with open('indice_refraction_facile.dat', 'r') as file:
    next(file)
    for line in file:
        line = line.split()
        indice_refraction_temp[line[1]] = line[0]


class Individual:
    indice_refraction_dict = indice_refraction_temp

    def __init__(self, omega, pc, i, phi1, n0):
        self.omega = omega
        self.pc = pc
        self.i = i
        self.phi1 = phi1
        self.n0 = n0

        if self.pc > self.omega/2:
            self.depth = self.pc - math.sqrt((self.pc*self.pc) - (self.omega*self.omega/4))
        elif self.pc == self.omega/2:
            self.depth = (self.omega/2)*(1 + math.sin(self.phi1))

        if self.pc > self.omega/2:
            self.aperture = self.omega - 2*self.i
        elif self.pc == self.omega/2:
            self.aperture = self.omega*math.cos(self.phi1) - 2*self.i

        self.lense_ratio = Individual.indice_refraction_dict['%.3f' % self.n0]

        if self.n0 == 1.350:
            self.view_angle = 2*math.atan(self.aperture/2*self.depth)
        elif self.n0 > 1.350:
            sq_ratio = self.lense_ratio*self.lense_ratio
            sq_aperture = self.aperture*self.aperture
            sq_depth = self.depth*self.depth
            up = (sq_ratio*self.aperture/(2*self.depth)) - math.sqrt(1 + sq_ratio - (sq_ratio*sq_aperture/(4*sq_depth)))
            down = 1 + sq_depth
            self.view_angle = 2 * math.asin(up/down)
