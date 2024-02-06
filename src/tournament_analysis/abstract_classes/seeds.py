from abc import ABC, abstractmethod, abstractproperty

class Seed(ABC):
    """Base class for a seed structure.
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the Seed.
        """
        self._defeated_seeds = []
        self.defeated = False

    @abstractproperty
    def seed(self):
        """The seed of the participant.
        """
        pass

    @abstractmethod
    def __eq__(self, other):
        """Check if two seeds are equal.
        """
        pass

    @abstractmethod
    def __lt__(self, other):
        """Check if one seed is less than another.
        """
        pass

    @abstractmethod
    def __str__(self):
        """Return the string representation of the seed.
        """
        pass

    def __repr__(self):
        """Return a string representation of the seed.
        """
        return f"{type(self).__name__}({self.seed})"

    def __hash__(self):
        """Return a hash value for the seed.
        """
        return hash(self.seed)

    def __ne__(self, other):
        """Check if two seeds are not equal.
        """
        return not self == other

    def __le__(self, other):
        """Check if one seed is less than or equal to another.
        """
        return self < other or self == other

    def __gt__(self, other):
        """Check if one seed is greater than another.
        """
        return not self <= other

    def __ge__(self, other):
        """Check if one seed is greater than or equal to another.
        """
        return not self < other

    def record_defeated_seed(self: "Seed", other: "Seed", round: int) -> None:
        """Record that the seed has defeated another seed.
        """
        self._defeated_seeds.append({"seed": other, "round": round})
        if other is None:
            return
        other.record_defeat(self, round)
    
    def record_defeat(self: "Seed", other: "Seed", round: int) -> None:
        """Record that the seed has been defeated by another seed.
        """
        self.defeated = True
        self.defeated_by_node = {"seed": other, "round": round}