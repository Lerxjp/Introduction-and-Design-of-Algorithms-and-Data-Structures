from typing import Any


class DynamicArray:
    def __init__(self) -> None:
        self._capacity = 1
        self._size = 0
        self._array = [None] * self._capacity
        self.reversed = False

    def __str__(self) -> str:
        """
        A helper that allows you to print a DynamicArray type
        via the str() method.
        """
        return str(self._array[:self._size])

    def __resize(self) -> None:
        # Doubles the array capacity
        self._capacity *= 2
        # creates a new array
        new_arr = [None] * self._capacity
        # Copies elements into the new array
        for i in range(self._size):
            new_arr[i] = self._array[i]
        self._array = new_arr

    def get_at(self, index: int) -> Any | None:
        """
        Get element at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """


        if 0 <= index < self._size:
            if self.reversed:
                return self._array[self._size - 1 - index]
            else:
                return self._array[index]
        return None

    def __getitem__(self, index: int) -> Any | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        return self.get_at(index)

    def set_at(self, index: int, element: Any) -> None:
        """
        Get element at the given index.
        Do not modify the list if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if 0 <= index < self._size:
            if self.reversed:
                self._array[self._size - 1 - index] = element
            else:
                self._array[index] = element

    def __setitem__(self, index: int, element: Any) -> None:
        """
        Same as set_at.
        Allows to use square brackets to index elements.
        """
        self.set_at(index, element)

    def append(self, element: Any) -> None:
        """
        Add an element to the back of the array.
        Time complexity for full marks: O(1*) (* means amortized)
        """
        if self._size == self._capacity:
            self.__resize()

        self._array[self._size] = element
        self._size += 1


    def prepend(self, element: Any) -> None:
        """
        Add an element to the front of the array.
        Time complexity for full marks: O(1*)
        """
        if self._size == self._capacity:
            self.__resize()

        # Shifts elements to the right for new elements to be placed in teh array
        for i in range(self._size, 0, -1):
            self._array[i] = self._array[i - 1]
        self._array[0] = element
        self._size += 1

    def reverse(self) -> None:
        """
        Reverse the array.
        Time complexity for full marks: O(1)
        """
        self.reversed = not self.reversed
        

    def remove(self, element: Any) -> None:
        """
        Remove the first occurrence of the element from the array.
        If there is no such element, leave the array unchanged.
        Time complexity for full marks: O(N)
        """
        for i in range(self._size):
            if self._array[i] == element:
                self.remove_at(i)
                return

    def remove_at(self, index: int) -> Any | None:
        """
        Remove the element at the given index from the array and return the removed element.
        If there is no such element, leave the array unchanged and return None.
        Time complexity for full marks: O(N)
        """
        # Adjusts array index incase of reversal
        if 0 <= index < self._size:
            if self.reversed == True:
                index = self._size - 1 - index
            removed_element = self._array[index]
            
            # Shifts elements to teh left
            for i in range(index, self._size - 1):
                self._array[i] = self._array[i + 1]
            # clears the last element in the array
            self._array[self._size - 1] = None
            self._size -= 1
            return removed_element
        return None

    def is_empty(self) -> bool:
        """
        Boolean helper to tell us if the structure is empty or not
        Time complexity for full marks: O(1)
        """
        return self._size == 0

    def is_full(self) -> bool:
        """
        Boolean helper to tell us if the structure is full or not
        Time complexity for full marks: O(1)
        """
        return self._size == self._capacity

    def get_size(self) -> int:
        """
        Return the number of elements in the list
        Time complexity for full marks: O(1)
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the total capacity (the number of slots) of the list
        Time complexity for full marks: O(1)
        """
        return self._capacity

    def sort(self) -> None:
        """
        Sort elements inside _array based on < comparisons using merge sort.
        Time complexity for full marks: O(NlogN)
        """
        self._merge_sort(0, self._size - 1)

    def _merge_sort(self, left: int, right: int) -> None:
        if left < right:
            middle = (left + right) // 2
            self._merge_sort(left, middle)
            self._merge_sort(middle + 1, right)
            self._merge(left, middle, right)

    def _merge(self, left: int, middle: int, right: int) -> None:
        # Create temporary arrays for the left and right halves.
        left_copy = self._array[left:middle + 1]
        right_copy = self._array[middle + 1:right + 1]
        # Indices for iterating through the temporary arrays.
        left_index = 0
        right_index = 0
        sorted_index = left

        # Merge the temporary arrays back into the original array.
        while left_index < len(left_copy) and right_index < len(right_copy):
            if left_copy[left_index] <= right_copy[right_index]:
                self._array[sorted_index] = left_copy[left_index]
                left_index += 1
            else:
                self._array[sorted_index] = right_copy[right_index]
                right_index += 1
            sorted_index += 1

        # Copy any remaining elements from the left temporary array.
        while left_index < len(left_copy):
            self._array[sorted_index] = left_copy[left_index]
            left_index += 1
            sorted_index += 1

        # Copy any remaining elements from the right temporary array.
        while right_index < len(right_copy):
            self._array[sorted_index] = right_copy[right_index]
            right_index += 1
            sorted_index += 1