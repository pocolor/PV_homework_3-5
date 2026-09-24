#!./.venv/bin/python3

from pprint import pprint


def main() -> None:
    my_list = ["foo", "bar", "baz"]

    def print_list_with_indeces(_list: list) -> None:
        pprint(list(enumerate(_list)))

    print_list_with_indeces(my_list)
    my_list.pop(0)
    print_list_with_indeces(my_list)


if __name__ == "__main__":
    main()

