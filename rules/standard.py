"""Standard Gomoku"""

from .rule import Rule
from error import GameWon
from typing import List, Tuple, Dict

class Standard(Rule):

    def __call__(self, position: Tuple[int, int], step: int,
                 situation: Dict[int, List[Tuple[int, int]]]) -> None:

        for pieces in situation.values():
            if len(pieces) == self.VJC:
                raise GameWon(pieces)

