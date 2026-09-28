#!./.venv/bin/python3

import random
import time


def main() -> None:
    my_dict = dict.fromkeys(range(1_000_000), 1)

    for _ in range(1_000_000):
        my_dict[random.randint(0, 999_999)] += 1

    start = time.perf_counter()

    found = 1234 in my_dict
    count = my_dict[1234]

    end = time.perf_counter()

    print(f"1234 {found=}, {count=}, took={end - start:0.6f}s")


if __name__ == "__main__":
    main()

