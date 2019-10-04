import itertools

from Values.procedures.create.base import BaseValue


class PositionTenderValue(BaseValue):
    pass

ppz = (list(itertools.product([0, 1, 2], [0, 1], [0, 1, 2, 3])))
