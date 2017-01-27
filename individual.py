import numpy


class Individual:

    def __init__(self, omega, pc, i, phi1, n0):
        self.omega = omega
        self.pc = pc
        self.i = i
        self.phi1 = phi1
        self.n0 = n0

    def depth(self):
        if self.pc > self.omega/2:
            return self.pc - numpy.sqrt((self.pc*self.pc) - (self.omega*self.omega/4))
        elif self.pc == self.omega/2:
            return (self.omega/2)*(1 + numpy.sin(self.phi1))

    def aperture(self):
        if self.pc > self.omega/2:
            return self.omega - 2*self.i
        elif self.pc == self.omega/2:
            return self.omega*numpy.cos(self.phi1) - 2*self.i

    def lense_ratio(self):
        return 0

    def view_angle(self):
        return 0
