text: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
path: str = "homework_10/task_2/data"

if __name__ == "__main__":
    with open(f"{path}/file_1.txt", "w") as file_1:
        file_1.write(text)

    with open(f"{path}/file_2.txt", "w") as file_2, open(
        f"{path}/file_1.txt", "r"
    ) as file_1:
        file_2.write(f"{file_1.readline().upper()}")
