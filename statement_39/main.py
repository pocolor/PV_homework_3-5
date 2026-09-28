#!./.venv/bin/python3


def main() -> None:
    if "foo" in ["foo", "bar", "baz"]:
        print("in search in list")

    if "foo" in {"foo", "bar", "baz"}:
        print("in search in set")


if __name__ == "__main__":
    main()

