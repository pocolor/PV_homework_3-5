#!./.venv/bin/python3

import time


def time_incremental_size(collection, collection_add_fn) -> None:
    n = 1000

    for i in range(n + 1):
        start = time.perf_counter()
        
        found = n in collection

        end = time.perf_counter()

        if len(collection) % 100 == 0:
            print(f"{type(collection)} len = {len(collection):>4}, search time = {(end - start) * 1_000_000:.3f} micro seconds")

        collection_add_fn(i)


def main() -> None:
    my_list = list()
    my_set = set()

    time_incremental_size(my_list, lambda e: my_list.append(e))
    time_incremental_size(my_set , lambda e: my_set.add(e))


if __name__ == "__main__":
    main()

