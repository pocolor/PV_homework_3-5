#!./.venv/bin/python3

import time


def timed(func):
    start = time.perf_counter()
    func()
    end = time.perf_counter()
    return end - start


def main() -> None:
    my_list = list(range(1000))
    print(f"{timed(lambda: my_list[-1] in my_list) * 1_000_000:7.3f} micro seconds")
    print(f"{timed(lambda: "foo" in my_list) * 1_000_000:7.3f} micro seconds")

    my_list = list(range(10_000))
    print(f"{timed(lambda: my_list[-1] in my_list) * 1_000_000:7.3f} micro seconds")
    print(f"{timed(lambda: "foo" in my_list) * 1_000_000:7.3f} micro seconds")

    my_list = list(range(100_000))
    print(f"{timed(lambda: my_list[-1] in my_list) * 1_000:7.3f}ms")
    print(f"{timed(lambda: "foo" in my_list) * 1_000:7.3f}ms")

    my_list = list(range(1_000_000))
    print(f"{timed(lambda: my_list[-1] in my_list) * 1_000:7.3f}ms")
    print(f"{timed(lambda: "foo" in my_list) * 1_000:7.3f}ms")


if __name__ == "__main__":
    main()

