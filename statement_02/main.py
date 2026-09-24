#!./.venv/bin/python3

from pprint import pprint


def main() -> None:
    my_list = list()
    my_set = set()


    def add_to_both(element) -> None:
        my_list.append(element)
        my_set.add(element)


    class MyType:
        def __repr__(self) -> str:
            return "MyType"


    add_to_both(1)
    add_to_both(1.0)
    add_to_both(1.5)
    add_to_both("foo")
    add_to_both(MyType())
    add_to_both(int)
    add_to_both(print)
    add_to_both(None)

    pprint(my_list)
    pprint(my_set)


if __name__ == "__main__":
    main()

