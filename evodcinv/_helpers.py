import numpy

nafe_drake_poly = numpy.poly1d([0.000106, -0.0043, 0.0671, -0.4721, 1.6612, 0.0])


def nafe_drake(velocity_p):
    return nafe_drake_poly(velocity_p)
