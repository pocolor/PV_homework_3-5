#!./.venv/bin/python3

from pprint import pprint


def main() -> None:
    my_list = ["foo", "bar", "baz"]
    my_set = {"foo", "bar", "baz"}

    pprint(my_list)
    pprint(my_set)


if __name__ == "__main__":
    main()

