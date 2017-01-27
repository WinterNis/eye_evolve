import numpy
import math

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
        if individual.phi1 != 0 and individual.omega/2 != individual.pc:
            return 0
        if individual.phi1 != 0 and individual.i > (individual.omega*math.cos(individual.phi1))/2:
            return 0
        if indivdual.n0 == 1.35 and True:
            pass
