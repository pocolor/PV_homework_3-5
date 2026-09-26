#!./.venv/bin/python3


def main() -> None:
    my_list = [0, 1, 2]
    my_tuple = my_list, "foo", "bar"

    my_tuple_id = id(my_tuple)
    my_list_id = id(my_list)
    my_tuple_list_id = id(my_tuple[0])

    my_list.append(10)

    print(f"new tuple: {my_tuple_id != id(my_tuple)}")
    print(f"new list: {my_list_id != id(my_list)}")
    print(f"new tuple list: {my_tuple_list_id != id(my_tuple[0])}")


if __name__ == "__main__":
    main()

