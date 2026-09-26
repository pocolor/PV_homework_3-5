#!./.venv/bin/python3

from pprint import pprint


def main() -> None:
    set1 = set()
    set2 = set()

    set1.add("foo")
    set1.add("bar")
    set1.add("baz")

    set2.add("bar")
    set2.add("baz")
    set2.add("foo")

    pprint(set1)
    pprint(set2)
    pprint(set1 == set2)


if __name__ == "__main__":
    main()

