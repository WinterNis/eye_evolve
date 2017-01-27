import math
import numpy

from individual import Individual
from mutator import Mutator

class World:
    def __init__(self, I, tournament_size, population):
        self.I = I
        self.tournament_size = tournament_size
        self.population = population
        self.mutator = Mutator(1, 1, 1, 1, 0.1, 0.1, 0.1, 0.1, self)


    def run_evolution(self):
        individual = Individual(1.5, 10000, 0, 0, 1.35, self)
        print(individual)

        new_individual = self.mutator.mutate(individual)

        print(new_individual)
