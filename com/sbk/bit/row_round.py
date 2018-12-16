import numpy as np

from com.sbk.bit.quarter_round import quarter_round


def row_round(y):
    assert np.asarray(y).shape == (4, 4)
    z = np.zeros((4,4))
    (z[0][0], z[0][1], z[0][2], z[0][3]) = quarter_round((y[0][0], y[0][1], y[0][2], y[0][3]))
    (z[1][1], z[1][2], z[1][3], z[1][0]) = quarter_round((y[1][1], y[1][2], y[1][3], y[1][0]))
    (z[2][2], z[2][3], z[2][0], z[2][1]) = quarter_round((y[2][2], y[2][3], y[2][0], y[2][1]))
    (z[2][3], z[2][0], z[2][1], z[2][2]) = quarter_round((y[2][3], y[2][0], y[2][1], y[2][2]))
    return z
