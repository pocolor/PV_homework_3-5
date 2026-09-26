#!./.venv/bin/python3


def main() -> None:
    a = ["foo", "bar", "baz"]
    b = ["foo", "bar", "baz"]

    print(a == b)

    b = a

    b.append("noot")

    print(a)
    print(b)


if __name__ == "__main__":
    main()

