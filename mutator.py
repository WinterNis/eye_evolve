import numpy
import math
from individual import Individual

class Mutator:

    def __init__(self, Sigma_pc, Sigma_i, Sigma_phi1, Sigma_n0):
        self.Sigma_pc = Sigma_pc
        self.Sigma_i = Sigma_i
        self.Sigma_phi1 = Sigma_phi1
        self.Sigma_n0 = Sigma_n0


    # mutates the individual given as parameter using numpy.normal
    # returns a NEW individual resulting from the mutation of the given individual
    def mutate(self, individual):

        # mutate pc
        pc_delta = numpy.random.normal(loc=0.0, scale=self.Sigma_pc, size=None)
        new_pc = individual.pc + pc_delta
        
        # mutate i
        i_delta = numpy.random.normal(loc=0.0, scale=self.Sigma_i, size=None)
        new_i = individual.i + i_delta
        
        # mutate phi1
        phi1_delta = numpy.random.normal(loc=0.0, scale=self.Sigma_phi1, size=None)
        new_phi1 = individual.phi1 + i_delta

        # mutate n0
        n0_delta = numpy.random.normal(loc=0.0, scale=self.Sigma_n0, size=None)
        new_n0 = individual.n0 + n0_delta
        new_n0 = max(min(new_n0, 1.550),1.350)

        new_individual = Individual(individual.omega, new_pc, new_i, new_phi1, new_n0)

        return new_individual
