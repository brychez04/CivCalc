import numpy

class Gaussian:

    def solve(coefficients, equal_values):
        return numpy.linalg.solve(coefficients, equal_values)
