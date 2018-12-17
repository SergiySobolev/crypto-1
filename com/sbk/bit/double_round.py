import numpy as np

from com.sbk.bit.column_round import column_round
from com.sbk.bit.row_round import row_round


def double_round(y):
    assert np.asarray(y).shape == (4, 4)
    return row_round(column_round(y))


def double_round_tuple(y):
    y_r = np.asarray(y).reshape(4,4)
    return double_round(y_r).reshape(1,16)[0]

