#!./.venv/bin/python3


def main() -> None:
    my_list = []

    my_list.append(("foo", 1))
    my_list.append(("bar", 4))
    my_list.append(("baz", 0))

    for k, v in my_list:
        if k == "bar":
            print(f"{k=}, {v=}")


if __name__ == "__main__":
    main()

