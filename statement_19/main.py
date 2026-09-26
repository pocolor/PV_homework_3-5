#!./.venv/bin/python3


def main() -> None:
    my_list = ["foo", "foo", "foo"]
    my_set = set(my_list)

    previous_list = my_list
    new_list = list(my_set)

    print(my_list)
    print(my_set)

    print(previous_list)
    print(new_list)

if __name__ == "__main__":
    main()

