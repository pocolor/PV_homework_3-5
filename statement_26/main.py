#!./.venv/bin/python3


def main() -> None:
    mut_obj = set()

    my_list = [mut_obj] * 10

    print(my_list)

    mut_obj.add("foo")

    print(my_list)


if __name__ == "__main__":
    main()

