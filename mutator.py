import numpy
import math
from individual import Individual

class Mutator:

    def __init__(self, Sigma_pc, Sigma_i, Sigma_phi1, Sigma_n0, CT_pc, CT_i, CT_phi1, CT_n0, world):
        # probabilistic distribution spread of the genes.
        self.Sigma_pc = Sigma_pc
        self.Sigma_i = Sigma_i
        self.Sigma_phi1 = Sigma_phi1
        self.Sigma_n0 = Sigma_n0
        self.world = world

        # Crossover thresholds for pc, i, phi1 and n0
        self.CT_pc = CT_pc
        self.CT_i = CT_i
        self.CT_phi1 = CT_phi1
        self.CT_n0 = CT_n0


    def mutate(self, individual):
        """
        Mutates the individual given as parameter using numpy.normal
        Returns a NEW individual resulting from the mutation of the given individual
        """

        # mutate pc
        pc_delta = numpy.random.normal(loc=0.0, scale=self.Sigma_pc, size=None)
        new_pc = individual.pc + pc_delta
        new_pc = max(min(new_pc, 10000), individual.omega/2)

        # mutate i
        i_delta = numpy.random.normal(loc=0.0, scale=self.Sigma_i, size=None)
        new_i = individual.i + i_delta
        new_i = max(min(new_i, individual.omega/2), 0)

        # mutate phi1
        phi1_delta = numpy.random.normal(loc=0.0, scale=self.Sigma_phi1, size=None)
        new_phi1 = individual.phi1 + phi1_delta
        new_phi1 = max(min(new_phi1, math.pi/2), 0)

        # mutate n0
        n0_delta = numpy.random.normal(loc=0.0, scale=self.Sigma_n0, size=None)
        new_n0 = individual.n0 + n0_delta
        new_n0 = max(min(new_n0, 1.550),1.350)

        new_individual = Individual(individual.omega, self.world, new_pc, new_i, new_phi1, new_n0)

        return new_individual


    def crossover(self, indiv_1, indiv_2):
        """
        Creates 2 "crossovered" individuals from the 2 parents given as parameters
        Crossovered individuals share 1 exclusive copy of the parent genes
        Probability that gene crossing occurs respects the crossover thresholds.
        """

        # genes of parent individuals
        genes_1 = [indiv_1.pc, indiv_1.i, indiv_1.phi1, indiv_1.n0]
        genes_2 = [indiv_2.pc, indiv_2.i, indiv_2.phi1, indiv_2.n0]

        # for each gene, the probability to be exchanged respects a given threshold
        nrand = numpy.random.uniform()
        if nrand > self.CT_pc :
            genes_1[0], genes_2[0] = genes_2[0], genes_1[0]

        nrand = numpy.random.uniform()
        if nrand > self.CT_i :
            genes_1[0], genes_2[0] = genes_2[0], genes_1[0]

        nrand = numpy.random.uniform()
        if nrand > self.CT_phi1 :
            genes_1[0], genes_2[0] = genes_2[0], genes_1[0]

        nrand = numpy.random.uniform()
        if nrand > self.CT_n0 :
            genes_1[0], genes_2[0] = genes_2[0], genes_1[0]

        new_indiv_1 = Individual(indiv_1.omega, self.world, *genes_1)
        new_indiv_2 = Individual(indiv_1.omega, self.world, *genes_2)

        return new_indiv_1, new_indiv_2
