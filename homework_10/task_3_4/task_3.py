import random
import csv

rounds: int = 100
players: list = ["Josh", "Luke", "Kate", "Mark", "Mary"]
path: str = "homework_10/task_3_4/data"


def give_random_score(player: str) -> dict:
    score: int = random.randint(1, 1000)
    return {"Player name": player, "Score": score}


if __name__ == "__main__":
    with open(f"{path}/scores.csv", "w") as scores_data:
        fieldnames: list = ["Player name", "Score"]
        writer = csv.DictWriter(scores_data, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(rounds):
            for player in players:
                writer.writerow(give_random_score(player))
