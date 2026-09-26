#!./.venv/bin/python3


def main() -> None:
    a = 10

    my_dict = {"a_val": a, "a_id": id(a)}

    print(a)
    print(id(a))
    print(my_dict)


if __name__ == "__main__":
    main()

