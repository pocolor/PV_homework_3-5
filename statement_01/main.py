#!./.venv/bin/python3

from pprint import pprint


def main() -> None:
    my_set = set()
    my_list = list()

    def insert_element_unique(element) -> None:
        # O(1)
        my_set.add(element)

        # O(n)
        if element not in my_list:
            my_list.append(element)


    insert_element_unique("foo")
    insert_element_unique("bar")
    insert_element_unique("baz")

    insert_element_unique("foo")
    insert_element_unique("baz")

    pprint(my_set)
    pprint(my_list)


if __name__ == "__main__":
    main()

