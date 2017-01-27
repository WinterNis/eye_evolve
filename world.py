import math
import numpy

from individual import Individual
from mutator import Mutator

class World:
    def __init__(self, I, tournament_size, population):
        self.I = I
        self.tournament_size = tournament_size
        self.population = population
        self.mutator = Mutator(1, 1, 1, 0, 0.5, 0.5, 0.5, 0.5, self)


    def run_evolution(self):
        individual = Individual(1.5, self, 10000, 0, 0, 1.35)
        print(individual)

        new_individual = self.mutator.mutate(individual)

        print(new_individual)
        new_1, new_2 = self.mutator.crossover(individual, new_individual)
        print(new_1)
        print(new_2)
