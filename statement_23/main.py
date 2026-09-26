#!./.venv/bin/python3


def main() -> None:
    my_str = "abc"
    my_list = list(my_str)

    print(my_str[0])
    print(my_list[0])

    print(my_str[-1])
    print(my_list[-1])

    #print(my_str[100])
    #print(my_list[100])

    #my_str[0] = "z"
    my_list[0] = "z"


if __name__ == "__main__":
    main()

