#!./.venv/bin/python3


def main() -> None:
    mut_collection = list()

    my_tuple = (mut_collection,)

    print(my_tuple)

    my_tuple[0].append("foo")

    print(my_tuple)


if __name__ == "__main__":
    main()

