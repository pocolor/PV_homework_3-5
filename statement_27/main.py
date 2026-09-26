#!./.venv/bin/python3


def main() -> None:
    set1 = set()
    set2 = set()

    set1.add("foo")
    set1.add("foo")
    set2.add("foo")

    print(set1)
    print(set2)


if __name__ == "__main__":
    main()

