from string import ascii_uppercase
import random
from pathlib import Path

path = "homework_10/task_1/data"

if __name__ == "__main__":
    with open(f"{path}/summary.txt", "w") as summary:
        for letter in ascii_uppercase:
            with open(f"{path}/{letter}.txt", "w") as file:
                file.write(str(random.randint(1, 100)))
                file.close()
                with open(f"{path}/{letter}.txt", "r") as file:
                    summary.write(f"{Path(file.name).stem}.txt: {file.readline()}\n")
