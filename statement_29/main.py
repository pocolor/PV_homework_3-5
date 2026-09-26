#!./.venv/bin/python3


def main() -> None:
    my_tuple = 0, 1
    my_dict = {my_tuple: "foo"}

    print(my_dict)
    print(my_dict[0, 1])


if __name__ == "__main__":
    main()

