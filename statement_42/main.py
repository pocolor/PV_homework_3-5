#!./.venv/bin/python3

import time


def timed(func):
    start = time.perf_counter()
    func()
    end = time.perf_counter()
    return end - start


def main() -> None:
    n = 500_000
    print(f"{n=:>7} search in list took={timed(lambda: n in list(range(n + 1)))      * 10e3:7.3f} micro seconds")
    print(f"{n=:>7} append to list took={timed(lambda: list(range(n + 1)).append(n)) * 10e3:7.3f} micro seconds")
    print(f"{n=:>7} pop  from list took={timed(lambda: list(range(n + 1)).pop())     * 10e3:7.3f} micro seconds")

    n *= 2
    print(f"{n=:>7} search in list took={timed(lambda: n in list(range(n + 1)))      * 10e3:7.3f} micro seconds")
    print(f"{n=:>7} append to list took={timed(lambda: list(range(n + 1)).append(n)) * 10e3:7.3f} micro seconds")
    print(f"{n=:>7} pop  from list took={timed(lambda: list(range(n + 1)).pop())     * 10e3:7.3f} micro seconds")


if __name__ == "__main__":
    main()

