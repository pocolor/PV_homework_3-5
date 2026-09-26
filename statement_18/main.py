#!./.venv/bin/python3


def main() -> None:
    my_tuple = "foo", "bar", "baz"
    my_list = list(my_tuple)

    my_list[1] = "noot"
    my_tuple[1] = "noot"


if __name__ == "__main__":
    main()

