#!./.venv/bin/python3

from pprint import pprint
from sortedcontainers import SortedSet


def main() -> None:
    my_list = ["foo", "bar", "baz"]
    my_treeset = SortedSet(my_list)

    pprint(my_list)
    pprint(my_treeset)


if __name__ == "__main__":
    main()

