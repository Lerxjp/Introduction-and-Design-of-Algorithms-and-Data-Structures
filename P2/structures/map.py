from typing import Any
from structures.entry import Entry
from structures.util import hash
from structures.dynamic_array import DynamicArray


class Map:
    """
    An implementation of the Map ADT.
    The provided methods consume keys and values via the Entry type.
    """

    def __init__(self) -> None:
        """
        Construct the map.
        You are free to make any changes you find suitable in this function
        to initialise your map.
        """
        self._primes = [5, 11, 17, 31, 59, 157, 269, 541, 1087,
                        2131, 4289, 8627, 17327, 36109, 73079,
                        154823, 309259, 603791, 1097897, 2089273,
                        4084931, 8090651, 15485863]
        self._prime_index = 0
        self._capacity = self._primes[self._prime_index]
        self._buckets = DynamicArray()
        self._buckets.allocate(self._capacity, None)
        self._size = 0
        self._deleted_marker = Entry(None, None)

    def _resize(self) -> None:
        load_factor = self._size / self._capacity
        if load_factor > 0.75:
            self._grow()
        elif load_factor < 0.2 and self._prime_index > 0:
            self._shrink()

    def _grow(self) -> None:
        if self._prime_index < len(self._primes) - 1:
            self._prime_index += 1

    def _shrink(self) -> None:
        if self._prime_index > 0:
            self._prime_index -= 1

    def insert(self, entry: Entry) -> Any | None:
        """
        Associate value v with key k for efficient lookups. If k already exists
        in your map, you must return the old value associated with k. Return
        None otherwise. (We will not use None as a key or a value in our tests).
        Time complexity for full marks: O(1*)
        """
        self._resize()
        index = hash(entry._key) % self._capacity

        if self._buckets.get_at(index) is None:
            new_bucket = DynamicArray()
            self._buckets.set_at(index, new_bucket)

        bucket = self._buckets.get_at(index)

        # Check if the key already exists, and if so, update the value
        for i in range(bucket.get_size()):
            existing_entry = bucket.get_at(i)
            if existing_entry._key == entry._key:
                old_value = existing_entry._value
                bucket.set_at(i, entry)  # Update the existing entry
                return old_value  # Don't increment size for updates

        # If the key is new, append it and increment the size
        bucket.append(entry)
        self._size += 1  # Only increment size for new keys
        return None

    def insert_kv(self, key: Any, value: Any) -> Any | None:
        """
        A version of insert which takes a key and value explicitly.
        Handy if you wish to provide keys and values directly to the insert
        function. It will return the value returned by insert, so keep this
        in mind. You can modify this if you want, as long as it behaves.
        Time complexity for full marks: O(1*)
        """
        entry = Entry(key, value)
        return self.insert(entry)

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        For convenience, you may wish to use this as an alternative
        for insert as well. However, this version does _not_ return
        anything. Can be used like: my_map[some_key] = some_value
        Time complexity for full marks: O(1*)
        """
        self.insert_kv(key, value)

    def remove(self, key: Any) -> None:
        """
        Remove the key/value pair corresponding to key k from the
        data structure. Don't return anything.
        Time complexity for full marks: O(1*)
        """
        self._resize()
        index = hash(key) % self._capacity
        bucket = self._buckets.get_at(index)

        if bucket is not None:
            for i in range(bucket.get_size()):
                entry = bucket.get_at(i)
                if entry._key == key:
                    bucket.remove_at(i)  # Remove the entry
                    self._size -= 1  # Decrement size when a key is removed
                    return

    def find(self, key: Any) -> Any | None:
        """
        Find and return the value v corresponding to key k if it
        exists; return None otherwise.
        Time complexity for full marks: O(1*)
        """

        index = hash(key) % self._capacity
        bucket = self._buckets.get_at(index)

        if bucket is not None:
            for i in range(bucket.get_size()):
                entry = bucket.get_at(i)
                if entry._key == key:
                    return entry._value

    def __getitem__(self, key: Any) -> Any | None:
        """
        For convenience, you may wish to use this as an alternative
        for find()
        Time complexity for full marks: O(1*)
        """
        return self.find(key)

    def get_size(self) -> int:
        """
        Time complexity for full marks: O(1)
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Time complexity for full marks: O(1)
        """
        return self._size == 0
