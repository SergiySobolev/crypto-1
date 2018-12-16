import numpy as np

from com.sbk.bit.column_round import column_round
from com.sbk.bit.row_round import row_round


def double_round(y):
    assert np.asarray(y).shape == (4, 4)
    return row_round(column_round(y))