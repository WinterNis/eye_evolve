import math
import numpy

from individual import Individual

class World:
    def __init__(self, I, tournament_size, population, mutator):
        self.I = I
        self.tournament_size = tournament_size
        self.population = population
        self.mutator = mutator

    def fitness(self, individual):
        """
        Return the score of the individual. 0 means the individual is sterile
        """

        # check if the individual is sterile.
        if individual.phi1 != 0 and individual.omega/2 != individual.pc:
            return 0

        cache_1 = individual.omega*math.cos(individual.phi1)
        if individual.phi1 != 0 and individual.i > cache_1/2:
            return 0

        cache_2 = math.sqrt(math.e/(0.746*math.sqrt(self.I)))
        if individual.n0 == 1.35 and individual.phi1 == 0 and individual.i > (individual.omega- cache_2)/2:
            return 0

        if individual.n0 == 1.35 and individual.phi1 != 0 and individual.i > (cache_1 - cache_2)/2:
            return 0

        if individual.n0 != 1.35 and (individual.depth > individual.lense_ratio*individual.aperture/2 or
                                      individual.depth < individual.aperture/2) :
            return 0

        # compute the fitness score of the individual.
        if individual.n0 == 1.35:
            return (0.375*(individual.depth/individual.aperture)*
                    math.sqrt(math.log(0.746*individual.aperture*individual.aperture*math.sqrt(self.I))))
        else:
            return 1/individual.view_angle

    def run_evolution(self):
        individual = Individual(1.5, 10000, 0, 0, 1.35, self)
        
