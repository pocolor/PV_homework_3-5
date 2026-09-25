#!./.venv/bin/python3

from pprint import pprint
from collections.abc import MutableSequence, Iterable
import sys


def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


class DictList(MutableSequence):
    def __init__(self, iterable: Iterable = None):
        self._dict = dict()

        if iterable is None:
            return

        if not isinstance(iterable, Iterable):
            raise TypeException

        self._dict = dict(enumerate(iterable))

    def __getitem__(self, index):
        if isinstance(index, slice):
            raise NotImplemented

        return self._dict[self._sanit_index(index)]

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            raise NotImplemented

        self._dict[self._sanit_index(index)] = value

    def __delitem__(self, index):
        raise NotImplemented

    def __len__(self):
        return len(self._dict)

    def __iter__(self):
        return iter(self._index_gen())

    def __str__(self):
        return str(list(self))

    def __repr__(self):
        return str(self)

    def _index_gen(self):
        for i in range(len(self)):
            yield self[i]

    def _sanit_index(self, index):
        if index < 0:
            index += len(self)

        if index < 0 or index >= len(self):
            raise IndexError

        return index

    def append(self, element):
        self._dict[len(self)] = element

    def clear(self):
        self._dict.clear()

    def copy(self):
        return DictList(iter(self))

    def count(self, element):
        counter = 0
        for e in self:
            if e == element:
                counter += 1
        return counter

    def extend(self, iterable):
        self._dict = dict(enumerate((*self, *iterable)))

    def index(self, element, start = 0, stop = sys.maxsize):
        for i in range(start, clamp(stop, 0, len(self))):
            if self[i] == element:
                return i

        raise ValueError

    def insert(self, index, value):
        raise NotImplemented


def main() -> None:

    my_list = ["foo", "bar", "baz"]
    my_dict = DictList(my_list)

    
    def print_both() -> None:
        pprint(my_list)
        pprint(my_dict)

    
    print_both()

    my_list.append("foo")
    my_dict.append("foo")

    print_both()

    print(my_list[1])
    print(my_dict[1])

    print_both()

    my_list[-1] = 0
    my_dict[-1] = 0

    print_both()


if __name__ == "__main__":
    main()

