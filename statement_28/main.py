#!./.venv/bin/python3

import random


def main() -> None:
    my_set = set()

    for _ in range(random.randint(10, 100)):
        my_set.add("foo")

    print(len(my_set))
    print(my_set)


if __name__ == "__main__":
    main()

