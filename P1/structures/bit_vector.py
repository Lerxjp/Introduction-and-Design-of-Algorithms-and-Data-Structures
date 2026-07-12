from typing import Any

from structures.dynamic_array import DynamicArray


class BitVector:
    """
    A compact storage for bits that uses DynamicArray under the hood.
    Each element stores up to 64 bits, making BitVector 64 times more memory-efficient
    for storing bits than plain DynamicArray.
    """

    BITS_PER_ELEMENT = 64

    def __init__(self) -> None:
        """
        We will use the dynamic array as our data storage mechanism
        """
        self._data = DynamicArray()  # Dynamic array to store teh data
        self._size = 0
        self._flipped = False  # Flag to indicate whether the bits are flipped
        self.reversed = False  # Flag to indicate whether the bits are reversed

    def __str__(self) -> str:
        """
        A helper that allows you to print a BitVector type
        via the str() method.
        """
        bit_string = ""
        for i in range(self._size):
            bit_string += str(self.get_at(i))
        return bit_string

    def __resize(self) -> None:
        self._data._capacity *= 2
        # creates a new array
        new_arr = [None] * self._capacity
        # Copies elements into the new array
        for i in range(self._size // 64):
            new_arr[i] = self._data[i]
        self._data = new_arr
        

    def get_at(self, index: int) -> int | None:
        """
        Get bit at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index < 0 or index >= self._size:
            return None
        
        if self.reversed:
            index = self.get_size() - 1 - index
        
        bit = (self._data[index // 64] >> index % 64) & 1
            
        if self._flipped:
            return 1 - bit
        return bit

    def __getitem__(self, index: int) -> int | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        if index < 0 or index >= self._size:
            return None
        return self.get_at(index)

    def set_at(self, index: int) -> None:
        """
        Set bit at the given index to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index < 0 or index >= self._size:
            return

        if self.reversed:
            index = self.get_size() - 1 - index
        
        curr = self._data[index // 64]
        
        if self._flipped:
            # bitwise and the NOT of (left shift or the bits position)
            curr = self._data[index // 64] & (~(1 << index % 64))
        else:
            # bitwise and the left shift or the bits position
            curr =self._data[index // 64] | (1 << index % 64)
            
        self._data[index // 64] = curr

    def unset_at(self, index: int) -> None:
        """
        Set bit at the given index to 0.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if index < 0 or index >= self._size:
            return

        if self.reversed:
            index = self.get_size() - 1 - index

        curr = self._data[index // 64]

        if self._flipped:
            # bitwise OR the left shift of the bit position to set the bit to 1
            curr = curr | (1 << index % 64)
        else:
            # bitwise AND the NOT of the left shift of the bit position to clear the bit
            curr = curr & (~(1 << index % 64))
        
        self._data[index // 64] = curr

    def __setitem__(self, index: int, state: int) -> None:
        """
        Set bit at the given index.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if state == 0:
            self.unset_at(index)
        else:
            self.set_at(index)

    def append(self, state: int) -> None:
        """
        Add a bit to the back of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """       
        self.__resize()
        if state == 0:
            self._data.append(state)
        else:
            self._data.append(1)
        self._size += 1

    def prepend(self, state: Any) -> None:
        """
        Add a bit to the front of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        self.__resize()
        if state == 0:
            self._data.prepend(state)
        else:
            self._data.prepend(1)
        self._size += 1

    def reverse(self) -> None:
        """
        Reverse the bit-vector.
        Time complexity for full marks: O(1)
        """
        self.reversed = not self.reversed

    def flip_all_bits(self) -> None:
        """
        Flip all bits in the vector.
        Time complexity for full marks: O(1)
        """
        self._flipped = not self._flipped

    def shift(self, dist: int) -> None:
        """
        Make a bit shift.
        If dist is positive, perform a left shift by `dist`.
        Otherwise perform a right shift by `dist`.
        Time complexity for full marks: O(N)
        """
        pass

    def rotate(self, dist: int) -> None:
        """
        Make a bit rotation.
        If dist is positive, perform a left rotation by `dist`.
        Otherwise perform a right rotation by `dist`.
        Time complexity for full marks: O(N)
        """
        pass

    def get_size(self) -> int:
        """
        Return the number of *bits* in the list
        Time complexity for full marks: O(1)
        """
        return self._size