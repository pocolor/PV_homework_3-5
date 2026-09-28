#!./.venv/bin/python3

import random


def print_ldb(ldb) -> None:
    for i, e in enumerate(ldb, start=1):
        print(f"{i}. {e}")


def main() -> None:
    leaderboard = ["pingu", "dave", "john"]

    print_ldb(leaderboard)

    random.shuffle(leaderboard)

    print("\nafter shuffling")
    print_ldb(leaderboard)


if __name__ == "__main__":
    main()

