#!./.venv/bin/python3


def main() -> None:
    list1 = [0, 1, 2]
    my_set = set(list1)
    list2 = sorted(list(my_set))

    print(list1)
    print(list2)


if __name__ == "__main__":
    main()

