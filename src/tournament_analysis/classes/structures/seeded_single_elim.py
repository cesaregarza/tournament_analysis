from src.tournament_analysis.abstract_classes.tournament import Tournament
from src.tournament_analysis.abstract_classes.seeds import Seed
from typing import List
import math

class SeededSingleEliminationKnockout(Tournament):
    """
    A class representing a seeded single elimination knockout tournament.

    Attributes:
        _seeds (List[Seed]): A list of Seed objects representing the tournament seeds.
        _results (List[List[Seed]]): A list of lists, each containing Seed objects that won their matches.
    """

    def __init__(self):
        """
        Initializes the SeededSingleEliminationKnockout with empty seeds and results lists.
        """
        self._seeds = []
        self._results = []

    def init_tournament(self, seeds: List[Seed]) -> None:
        """
        Initializes the tournament with a list of seeds, sorting them and assigning byes if necessary.

        Args:
            seeds (List[Seed]): A list of Seed objects to be sorted and initialized in the tournament.
        """
        sorted_seeds = sorted(seeds, key=lambda seed: seed.seed)
        num_byes = self._calculate_byes(len(sorted_seeds))
        self._seeds = sorted_seeds + [None] * num_byes
        self._results = []

    def run_tournament(self) -> None:
        """
        Runs the tournament, matching the top seed against the lowest seed and determining winners until a final winner is determined.
        """
        round = 1
        while len(self._seeds) > 1:
            winners = []
            losers = []
            while self._seeds:
                top_seed = self._seeds.pop(0)
                lowest_seed = self._seeds.pop()
                winner, loser = (top_seed, lowest_seed) if top_seed > lowest_seed else (lowest_seed, top_seed)
                print(f"Winner of round {round}: {winner}, loser: {loser}")
                winner.record_defeated_seed(loser, round)
                winners.append(winner)
                losers.append(loser)
            self._seeds = winners
            self._results.append(losers)
            round += 1
        # Include the final winner in the results
        self._results.append(self._seeds[0])

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


