#!./.venv/bin/python3

import time


def timed(func, n):
    start = time.perf_counter()
    for _ in range(n):
        func()
    end = time.perf_counter()
    return end - start


def main() -> None:
    my_list = list(range(1_000_000))
    my_set = set(my_list)

    x = 100_000
    n = 10_000

    print(f"{x:>6} in list took {timed(lambda: x in my_list, n):.9f}s")
    print(f"{x:>6} in set  took {timed(lambda: x in my_set , n):.9f}s")

    x = 0

    print(f"{x:>6} in list took {timed(lambda: x in my_list, n):.9f}s")
    print(f"{x:>6} in set  took {timed(lambda: x in my_set , n):.9f}s")


if __name__ == "__main__":
    main()

