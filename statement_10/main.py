#!./.venv/bin/python3

import time
from collections.abc import Callable


def timed(func: Callable[[], None]) -> float:
    start = time.perf_counter()

    func()

    end = time.perf_counter()

    return end - start


def main() -> None:
    my_list = list(range(1_000_000))
    my_set = set(my_list)

    print(f"10      in list took {timed(lambda: 10 in my_list) * 1000:0.6f}ms")
    print(f"100     in list took {timed(lambda: 100 in my_list) * 1000:0.6f}ms")
    print(f"1000    in list took {timed(lambda: 1000 in my_list) * 1000:0.6f}ms")
    print(f"10_000  in list took {timed(lambda: 10_000 in my_list) * 1000:0.6f}ms")
    print(f"100_000 in list took {timed(lambda: 100_000 in my_list) * 1000:0.6f}ms")
    print(f"999_999 in list took {timed(lambda: 999_999 in my_list) * 1000:0.6f}ms")

    
    print(f"10      in set  took {timed(lambda: 10 in my_set) * 1000:0.6f}ms")
    print(f"100     in set  took {timed(lambda: 100 in my_set) * 1000:0.6f}ms")
    print(f"1000    in set  took {timed(lambda: 1000 in my_set) * 1000:0.6f}ms")
    print(f"10_000  in set  took {timed(lambda: 10_000 in my_set) * 1000:0.6f}ms")
    print(f"100_000 in set  took {timed(lambda: 100_000 in my_set) * 1000:0.6f}ms")
    print(f"999_999 in set  took {timed(lambda: 999_999 in my_set) * 1000:0.6f}ms")


if __name__ == "__main__":
    main()

