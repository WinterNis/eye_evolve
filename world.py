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

        self.mutator = Mutator(1, 0.05, 0.05, 0.01, 0.5, 0.5, 0.5, 0.5, self)


    def run_evolution(self):
        # individual = Individual(1.5, self, 10000, 0, 0, 1.35)
        # print(individual)
        #
        # new_individual = self.mutator.mutate(individual)
        #
        # print(new_individual)
        #
        # new_1, new_2 = self.mutator.crossover(individual, new_individual)

        for i in range(300000):
            # select two individuals winners of tournaments
            fittest_1, fittest_2 = self.run_biased_wheel()

            # create two children from those winners
            child_1, child_2 = self.mutator.crossover(fittest_1, fittest_2)
            child_1, child_2 = self.mutator.mutate(child_1), self.mutator.mutate(child_2)

            # replace two random individuals by those children

            self.population[randint(0,len(self.population)-1)] = child_1
            self.population[randint(0,len(self.population)-1)] = child_2

            # print(i)
            # print('{} fitness:{}'.format(child_1, child_1.fitness))
            # print('{} fitness:{}'.format(child_2, child_2.fitness))

            verybest = 0
            if i % 1000 == 0:
                best = sorted(self.population, key = lambda x: x.fitness)[len(self.population) - 1]
                if best.fitness > verybest:
                    print('{}'.format(best))
                    verybest = best.fitness


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

        fittest_candidate_t1 = sorted(candidates_t1, key = lambda x: x.fitness,reverse=True)[0]
        fittest_candidate_t2 = sorted(candidates_t2, key = lambda x: x.fitness,reverse=True)[0]

        return fittest_candidate_t1, fittest_candidate_t2


    def run_biased_wheel(self):
        """
            Make two tournament using a biased wheel, give the two winners
            Supposes that at least "self.tournament_size" individual have positives scores.
        """

        tmp_collection = []
        tmp_scores_cumul = []
        prev = 0
        for i in self.population:
            if i.fitness > 0:
                tmp_collection.append(i)
                prev = prev + i.fitness
                tmp_scores_cumul.append(prev)
        
        total = tmp_scores_cumul[-1]

        competitors = []

        # biased selection of the competitors
        for i in range(self.tournament_size):
            # pick a random value
            randval = numpy.random.uniform(0.00000001,total)

            # find the index of the interval
            for j in range(len(tmp_collection)):
                if tmp_scores_cumul[j] < randval:
                    continue
                else:
                    competitors.append(tmp_collection[j])
                    break
        
        # select and return 2 best competitor

        competitors = sorted(competitors, key = lambda x: x.fitness,reverse=True)
        
        return competitors[0], competitors[1]
