def hats_on_cats(rounds: int, num_of_cats: int) -> None:
    cats: list[dict] = [
        {"cat_index": i, "hat_on": False} for i in range(1, num_of_cats + 1)
    ]

    while rounds:
        # Round 1 (stop at every cat)
        if rounds:
            for cat in cats:
                cat["hat_on"] = False if cat["hat_on"] else True
            rounds -= 1
        else:
            break

        # Round 2 (stop at every second cat)
        if rounds:
            for cat in cats:
                if cat["cat_index"] % 2 == 0:
                    cat["hat_on"] = False if cat["hat_on"] else True
            rounds -= 1
        else:
            break

        # Round 3 (stop at every third cat)
        if rounds:
            for cat in cats:
                if cat["cat_index"] % 3 == 0:
                    cat["hat_on"] = False if cat["hat_on"] else True
            rounds -= 1
        else:
            break

    res: list = []
    for cat in cats:
        if cat["hat_on"]:
            res.append(cat["cat_index"])

    print(f"Number of cats with hats on: {res}")


if __name__ == "__main__":
    hats_on_cats(100, 100)
