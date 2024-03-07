from dataclasses import dataclass
import datetime


@dataclass
class WorkoutData:
    """class for workout data"""

    exercise: str
    reps: int
    sets: int
    weightUsed: int
    rest: int

    def totalWeight(self) -> int:
        """computes total exercise load"""
        weightMoved = self.reps * self.sets * self.weightUsed
        return weightMoved


TRAINING_SESSION = {
    "pull": WorkoutData(exercise="rows", reps=10, sets=5, weightUsed=8, rest=24),
    "push": WorkoutData(exercise="rows", reps=10, sets=5, weightUsed=8, rest=24),
}

testWerk = WorkoutData(exercise="rows", reps=10, sets=5, weightUsed=8, rest=24)


def main():
    print(TRAINING_SESSION.keys())
    print("hi")
    print(TRAINING_SESSION["pull"])

    print(testWerk.totalWeight())


if __name__ == "__main__":
    main()
