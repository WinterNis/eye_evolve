import math

import pdb

# load indice refraction file
indice_refraction_temp = {}
with open('indice_refraction_facile.dat', 'r') as file:
    next(file)
    for line in file:
        line = line.split()
        indice_refraction_temp[line[1]] = line[0]


class Individual:
    indice_refraction_dict = indice_refraction_temp

    def __repr__(self):
        return '{} {} {} {} {} {}'.format(self.omega, self.pc, self.i, self.phi1, self.n0, self.fitness)

    def __init__(self, omega, world, pc, i, phi1, n0):
        self.omega = omega
        self.pc = pc
        self.i = i
        self.phi1 = phi1
        self.n0 = n0
        self.world = world

        if self.pc > self.omega/2:
            self.depth = self.pc - math.sqrt((self.pc*self.pc) - (self.omega*self.omega/4))
        elif self.pc == self.omega/2:
            self.depth = (self.omega/2)*(1 + math.sin(self.phi1))

        if self.pc > self.omega/2:
            self.aperture = self.omega - 2*self.i
        elif self.pc == self.omega/2:
            self.aperture = self.omega*math.cos(self.phi1) - 2*self.i

        self.lense_ratio = float(Individual.indice_refraction_dict['%.3f' % self.n0])


        if self.n0 == 1.350:
            self.view_angle = 2*math.atan(self.aperture/(2*self.depth))
        elif self.n0 > 1.350:
            sq_ratio = self.lense_ratio*self.lense_ratio
            sq_aperture = self.aperture*self.aperture
            sq_depth = self.depth*self.depth

            try:
                up = (sq_ratio*self.aperture/(2*self.depth)) - math.sqrt(1 + sq_ratio - (sq_ratio*sq_aperture/(4*sq_depth)))
            except:
                up = 0

            down = 1 + sq_depth

            try:
                self.view_angle = 2 * math.asin(up/down)
            except:
                self.view_angle = float('inf')

        self.compute_fitness()

    def compute_fitness(self):
        """
        Assign the fitness of the individual. 0 means the individual is sterile
        """
        # check if the individual is sterile.
        if self.phi1 != 0 and self.omega/2 != self.pc:
            self.fitness = 0
            return

        cache_1 = self.omega*math.cos(self.phi1)
        if self.phi1 != 0 and self.i > cache_1/2:
            self.fitness = 0
            return

        cache_2 = math.sqrt(math.e/(0.746*math.sqrt(self.world.I)))
        if self.n0 == 1.35 and self.phi1 == 0 and self.i > (self.omega- cache_2)/2:
            self.fitness = 0
            return

        if self.n0 == 1.35 and self.phi1 != 0 and self.i > (cache_1 - cache_2)/2:
            self.fitness = 0
            return

        if self.n0 != 1.35 and (self.depth > self.lense_ratio*self.aperture/2 or
                                      self.depth < self.aperture/2) :
            self.fitness = 0
            return

        # compute the fitness score of the individual.
        if self.n0 == 1.35:
            self.fitness = (0.375*(self.depth/self.aperture)*
                    math.sqrt(math.log(0.746*self.aperture*self.aperture*math.sqrt(self.world.I))))
            return
        else:
            self.fitness = 1/self.view_angle
            return
