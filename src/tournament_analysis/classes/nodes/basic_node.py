from tournament_analysis.abstract_classes.seeds import Seed

class BasicSeed(Seed):
    def __init__(self, seed: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._seed = seed
    
    @property
    def seed(self) -> int:
        return self._seed
    
    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.seed == other.seed
    
    def __lt__(self, other) -> bool:
        if other is None:
            return False
        return self.seed > other.seed # Lower seed is better
    
    def __str__(self) -> str:
        if not self.defeated:
            return f"Seed {self.seed}"
        
        # Return a much more thorough string if the seed has been defeated
        out = f"Seed {self.seed}(\n"
        out += f"Defeated: {self.defeated_seeds}\n"
        out += f"Defeated by: {self.defeated_by}\n"
        out += ")"
        return out
