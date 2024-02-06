from abc import ABC, abstractmethod, abstractproperty

from src.tournament_analysis.abstract_classes.seeds import Seed

class Tournament(ABC):
    """Base class for a tournament structure.
    """

    @abstractmethod
    def init_tournament(self, seeds: list[Seed]) -> None:
        """Initialize the tournament.

        Args:
            seeds (list): List of seeds representing the participants.

        Returns:
            None
        """
        pass

    @abstractmethod
    def run_tournament(self, seeds: list[Seed]) -> None:
        """Run the tournament based on the input seeds.
        """
        pass

    @abstractproperty
    def results(self) -> list:
        """Return the results of the tournament.
        """
        pass