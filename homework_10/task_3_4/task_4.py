# Context manager (result file: high_scores_cm.csv)

from operator import itemgetter
import csv
from task_3 import players

path: str = "homework_10/task_3_4/data"


def get_highest(player) -> dict:
    with open(f"{path}/scores.csv", "r") as file:
        reader = csv.DictReader(file)
        my_list: list = [
            int(row["Score"]) for row in reader if row["Player name"] == player
        ]
    max_score = max(my_list)
    return {"Player name": player, "Highest score": max_score}


def sort_dict() -> list:
    my_list: list = [get_highest(player) for player in players]
    my_list.sort(key=itemgetter("Highest score"), reverse=True)
    return my_list


if __name__ == "__main__":
    with open(f"{path}/high_scores_cm.csv", "w") as high:
        fieldnames: list = ["Player name", "Highest score"]
        writer = csv.DictWriter(high, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sort_dict())
