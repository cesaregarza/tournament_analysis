from src.tournament_analysis.abstract_classes.tournament import Tournament
from src.tournament_analysis.abstract_classes.seeds import Seed
from typing import List
import math
import random

class SeedlessSingleEliminationKnockout(Tournament):
    """
    A class representing a seedless single elimination knockout tournament.

    Attributes:
        _participants (List[Seed]): A list of Seed objects representing the tournament participants.
        _results (List[List[Seed]]): A list of lists, each containing Seed objects that won their matches.
    """

    def __init__(self):
        """
        Initializes the SeedlessSingleEliminationKnockout with empty participants and results lists.
        """
        self._participants = []
        self._results = []

    def init_tournament(self, participants: List[Seed]) -> None:
        """
        Initializes the tournament with a list of participants, randomly assigning them and assigning byes if necessary.

        Args:
            participants (List[Seed]): A list of Seed objects to be randomly initialized in the tournament.
        """
        random.shuffle(participants)
        num_byes = self._calculate_byes(len(participants))
        self._participants = participants + [None] * num_byes
        self._results = []

    def run_tournament(self, participants: List[Seed]) -> None:
        """
        Runs the tournament, matching participants in pairs and determining winners until a final winner is determined.

        Args:
            participants (List[Seed]): A list of Seed objects participating in the tournament.
        """
        if not self._participants:
            self.init_tournament(participants)
        while len(self._participants) > 1:
            winners = []
            for i in range(0, len(self._participants), 2):
                match = self._participants[i:i+2]
                if len(match) == 2 and None not in match:
                    winner = match[0] if match[0] < match[1] else match[1]
                    winners.append(winner)
                else:
                    # Assign the bye (if any) to the next round
                    winners.append(match[0] if match[0] is not None else match[1])
            self._participants = winners
            self._results.append(winners)
        if self._participants:
            self._results.append(self._participants)

    @property
    def results(self) -> List:
        """
        Returns the results of the tournament.

        Returns:
            List[List[Seed]]: A list of lists, each containing Seed objects that won their matches.
        """
        return self._results

    def _calculate_byes(self, num_participants: int) -> int:
        """
        Calculates the number of byes needed to make the number of participants a power of 2.

        Args:
            num_participants (int): The number of participants in the tournament.

        Returns:
            int: The number of byes needed.
        """
        next_power_of_two = 2 ** math.ceil(math.log2(num_participants))
        return next_power_of_two - num_participants
