#!./.venv/bin/python3

from pprint import pprint
import math


class A:
    ...


async def cortn():
    ...


def gen():
    yield 0


def main() -> None:
    my_list = [0, 0.5, True, "foo", None, ..., str, print, math, A, A(), cortn, cortn(), gen, gen()]
    my_set = set(my_list)

    #pprint(my_list)
    #pprint(my_set)
    
    found_all = True
    for e in my_list:
        if e not in my_set:
            found_all = False
            print(f"{e} not in set")

    if found_all:
        print("all elements in list were found in set")


if __name__ == "__main__":
    main()

