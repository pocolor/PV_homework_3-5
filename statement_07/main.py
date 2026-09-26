#!./.venv/bin/python3

import time


def main() -> None:
    my_list = list(range(1_000_000))
    my_set = set(my_list)

    start = time.time()

    for _ in range(1000):
        found = 10 in my_list
        found = 100 in my_list
        found = 1000 in my_list
        found = 10_000 in my_list
        found = 100_000 in my_list
        found = 999_999 in my_list

    end = time.time()

    print(f"List took: {end - start:0.6f}s")


    start = time.perf_counter()

    for _ in range(1000):
        found = 10 in my_set
        found = 100 in my_set
        found = 1000 in my_set
        found = 10_000 in my_set
        found = 100_000 in my_set
        found = 999_999 in my_set

    end = time.perf_counter()

    print(f"Set took: {end - start:0.6f}s")


if __name__ == "__main__":
    main()

