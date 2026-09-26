#!./.venv/bin/python3


def main() -> None:
    collection0 = [0, 1, 2]
    collection1 = {0, 1, 2}

    print(type(collection0) == type(collection1))


if __name__ == "__main__":
    main()

