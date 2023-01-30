import numpy as np


def polyfit(dates, levels, p):
    x = dates
    y = levels

    # Shift in base for accuracy purposes
    d0 = -x[1] + 2 * x[0]

    # Find coefficients of best-fit polynomial f(x) of degree p, with a change of base of d0
    p_coeff = np.polyfit(x - d0, y, p)

    # Convert coefficient into a polynomial that can be evaluated,
    poly = np.poly1d(p_coeff)

    return poly, d0
