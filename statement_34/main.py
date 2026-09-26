#!./.venv/bin/python3

import sys


def main() -> None:
    my_list = list(range(1_000_000))
    my_set = set(my_list)
    my_dict = dict(enumerate(range(1_000_000)))

    print(sys.getsizeof(my_list))
    print(sys.getsizeof(my_set))
    print(sys.getsizeof(my_dict))


if __name__ == "__main__":
    main()

