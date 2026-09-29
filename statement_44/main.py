#!./.venv/bin/python3

import time

def timed(func):
    start = time.perf_counter()
    func()
    end = time.perf_counter()
    return end - start


def main() -> None:
    my_list = list(range(1_000_000))

    print(f"{timed(lambda: my_list[100_001]) * 1_000_000:7.3f} micro seconds")
    print(f"{timed(lambda: 100_000 in my_list) * 1_000_000:7.3f} micro seconds")


if __name__ == "__main__":
    main()

