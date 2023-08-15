# Pandas (result file: high_scores_pd.csv)

from operator import itemgetter
import pandas as pd
from task_3 import players

path: str = "homework_10/task_3_4/data"
scores_path = f"{path}/scores.csv"
scores_data = pd.read_csv(scores_path)


def return_highest_score(player) -> list:
    highest_score: int = (scores_data[scores_data["Player name"] == player])[
        "Score"
    ].max()
    return [player, highest_score]


def return_sorted_list() -> list:
    my_list: list = [return_highest_score(player) for player in players]
    my_list.sort(key=itemgetter(1), reverse=True)
    return my_list


if __name__ == "__main__":
    df = pd.DataFrame(return_sorted_list(), columns=["Player name", "Highest score"])
    df.to_csv(f"{path}/high_scores_pd.csv", index=False)
