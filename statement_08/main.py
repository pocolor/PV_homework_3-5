#!./.venv/bin/python3

from pprint import pprint


def main() -> None:
    my_list = ["foo", "bar", "baz"]
    my_set = {"foo", "bar", "baz"}

    my_list.append("foo")
    my_set.add("foo")

    pprint(my_list)
    pprint(my_set)

    my_list[1] = "noot"
    my_set[1] = "noot"


if __name__ == "__main__":
    main()

