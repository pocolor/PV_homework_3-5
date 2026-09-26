#!./.venv/bin/python3


def main() -> None:
    collection1 = [set() for _ in range(3)]
    collection2 = [set() for _ in range(3)]

    print(collection1 == collection2)

    collection2[0].add("foo")

    print(collection1 == collection2)


if __name__ == "__main__":
    main()

