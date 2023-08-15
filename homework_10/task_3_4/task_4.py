# Context manager (result file: high_scores_cm.csv)

from operator import itemgetter
import csv
from task_3 import players

path: str = "homework_10/task_3_4/data"


# Run task_3.py to get scores.csv
def get_highest() -> list:
    result_list: list = []
    for player in players:
        with open(f"{path}/scores.csv", "r") as file:
            reader = csv.DictReader(file)
            inner_list: list = [
                int(row["Score"]) for row in reader if row["Player name"] == player
            ]
        max_score = max(inner_list)

        result_list.append({"Player name": player, "Highest score": max_score})
    return result_list


def sort_list(list) -> list:
    list.sort(key=itemgetter("Highest score"), reverse=True)
    return list


if __name__ == "__main__":
    with open(f"{path}/high_scores_cm.csv", "w") as high:
        fieldnames: list = ["Player name", "Highest score"]
        writer = csv.DictWriter(high, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sort_list(get_highest()))
