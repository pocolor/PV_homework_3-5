#!./.venv/bin/python3


def main() -> None:
    a = list()
    b = a

    print(a is b)

    a.append("foo")

    print(b)


if __name__ == "__main__":
    main()

