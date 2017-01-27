import math
from random import randint
import numpy

from individual import Individual
from mutator import Mutator

class World:
    def __init__(self, I, tournament_size, population_size):
        self.I = I
        self.tournament_size = tournament_size
        self.population = []

        for i_population in range(population_size):
            self.population.append(Individual(1.5, self, 10000, 0, 0, 1.35))

        self.mutator = Mutator(1000, 1, 1, 0, 0.5, 0.5, 0.5, 0.5, self)


    def run_evolution(self):
        # individual = Individual(1.5, self, 10000, 0, 0, 1.35)
        # print(individual)
        #
        # new_individual = self.mutator.mutate(individual)
        #
        # print(new_individual)
        #
        # new_1, new_2 = self.mutator.crossover(individual, new_individual)

        for i in range(200):
            # select two individuals winners of tournaments
            fittest_1, fittest_2 = self.run_tournament()

            # create two children from those winners
            child_1, child_2 = self.mutator.crossover(fittest_1, fittest_2)
            child_1, child_2 = self.mutator.mutate(child_1), self.mutator.mutate(child_2)

            # replace two random individuals by those children

            self.population[randint(0,len(self.population)-1)] = child_1
            self.population[randint(0,len(self.population)-1)] = child_2

            # print(i)
            # print('{} fitness:{}'.format(child_1, child_1.fitness))
            # print('{} fitness:{}'.format(child_2, child_2.fitness))


            best = sorted(self.population, key = lambda x: x.fitness)[len(self.population) - 1]
            print('{}'.format(best))


    def run_tournament(self):
        """
            Make two tournament, give the two winners
        """
        # we do that in order to be sure not being stucked (if all a 0 fitness)
        candidate_positive_fitness = [elt for elt in self.population if elt.fitness > 0]

        if(len(candidate_positive_fitness) == 0):
            raise ValueError('No candidate with a fitness > 0 !')

        candidates_t1 = [candidate_positive_fitness[randint(0, len(candidate_positive_fitness) - 1)]
                            for i in range(self.tournament_size)]

        candidates_t2 = [candidate_positive_fitness[randint(0, len(candidate_positive_fitness) - 1)]
                            for i in range(self.tournament_size)]

        fittest_candidate_t1 = sorted(candidates_t1, key = lambda x: x.fitness)[len(candidates_t1)-1]
        fittest_candidate_t2 = sorted(candidates_t2, key = lambda x: x.fitness)[len(candidates_t2)-1]

        return fittest_candidate_t1, fittest_candidate_t2
