from __future__ import annotations
from collections.abc import Iterator
from typing import Any


class Node:
    """
    A simple type to hold data and a next pointer
    """

    def __init__(self, data: Any) -> None:
        self._data = data  # This is the payload data of the node
        self._next = None  # This is the "next" pointer to the next Node
        self._prev = None  # This is the "previous" pointer to the previous Node

    def set_data(self, data: Any) -> None:
        self._data = data

    def get_data(self) -> Any:
        return self._data

    def set_next(self, node: Node) -> None:
        self._next = node

    def get_next(self) -> Node | None:
        return self._next

    def set_prev(self, node: Node) -> None:
        self._prev = node

    def get_prev(self) -> Node | None:
        return self._prev


class DoublyLinkedList:
    """
    Your doubly linked list code goes here.
    """

    def __init__(self) -> None:
        self._head = None #This is the head pointer for the first node
        self._tail = None #This is the tail pointer for the last node
        self._size = 0
        self.reversed = False #This is the flag for whether the list is reversed

    def __str__(self) -> str:
        """
        A helper that allows you to print a DoublyLinkedList type
        via the str() method.
        """
        list_str = "[HEAD] "
        cur = self.__get_head_node()
        # handle special head print
        if cur is not None:
            list_str += str(cur.get_data())
        cur = cur.get_next(self.is_reversed())
        # Loops across the LL
        while cur is not None:
            list_str += "<->" + str(cur.get_data())
            cur = cur.get_next(self.is_reversed())
        list_str += " [TAIL]"
        return list_str
    
    def _iterate(self) -> Iterator[Node]:
        """
        We can use a special "iterate" generator to walk the correct direction
        depending on whether our linked list is reverse or not
        """
        cur = None
        if self._reversed:
            cur = self._tail
        else:
            cur = self._head
        while cur is not None:
            yield cur
            cur = cur.get_next(self.is_reversed())

    """
    Simple Getters and Setters below
    """

    def is_reversed(self) -> bool:
        """
        Return whether we are current in reversed mode or not.
        """
        return self._reversed   

    def get_size(self) -> int:
        """
        Return the size of the list.
        Time complexity for full marks: O(1)
        """
        return self._size

    def get_head(self) -> Any | None:
        """
        Return the leftmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """

        cur = None
        if self.is_reversed():
            cur = self._tail
        else:
            cur = self._head
        
        if cur is not None:
            return cur.get_data()
        
        return None

    def set_head(self, data: Any) -> None:
        """
        Replace the leftmost node in the list.
        Time complexity for full marks: O(1)
        """
        cur = None
        if self.is_reversed():
            cur = self._tail
        else:
            cur = self._head
        
        if cur is not None:
            cur.set_data(data)

    def get_tail(self) -> Any | None:
        """
        Return the rightmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        cur = None
        if self.is_reversed():
            cur = self._head
        else:
            cur = self._tail

        if cur is not None:
            return cur.get_data()
        return None

    def set_tail(self, data: Any) -> None:
        """
        Replace the rightmost node in the list.
        Time complexity for full marks: O(1)
        """
        cur = None
        if self.is_reversed():
            cur = self._head
        else:
            cur = self._tail

        if cur is not None:
            cur.set_data(data)

    """
    More interesting functionality now.
    """

    def insert_to_front(self, data: Any) -> None:
        """
        Insert a node to the front of the list
        Time complexity for full marks: O(1)
        """
        node = Node(data)
        if self.is_reversed():
            cur = self._tail
            if cur is not None:
                cur.set_next(node, False)
                node.set_prev(cur, False)
            else:
                self._head = node
            self._tail = node
            self._size += 1
        else:
            cur = self._head
            if cur is not None:
                node.set_next(cur, False)
                cur.set_prev(node, False)
            else:
                self._tail = node
            self._head = node
            self._size += 1
        

    def insert_to_back(self, data: Any) -> None:
        """
        Insert a node to the back of the list
        Time complexity for full marks: O(1)
        """
        node = Node(data)
        if self.is_reversed() == True:
            cur = self._tail
            if cur is not None:
                cur.set_next(node, False)
                node.set_prev(cur, False)
            else:
                self._head = node
            self._tail = node
            self._size += 1
        else:
            cur = self._head
            if cur is not None:
                node.set_next(cur, False)
                cur.set_prev(node, False)
            else:
                self._tail = node
            self._head = node
            self._size += 1

    def remove_from_front(self) -> Any | None:
        """
        Remove and return the front element
        Time complexity for full marks: O(1)
        """
        if self._size == 0:
            return None
        
        cur = self.__get_head_node()
        
        if self._size == 1:
            self._head = None
            self._tail = None
            self._size = 0
            return cur.get_data()

        # Need to replace the "head"
        if self.is_reversed():
            self._tail = cur.get_next(True)
            self._tail.set_prev(None, True)
        else:
            self._head = cur.get_next(False)
            self._head.set_prev(None, False)
        self._size -= 1
        return cur.get_data()

    def remove_from_back(self) -> Any | None:
        """
        Remove and return the back element
        Time complexity for full marks: O(1)
        """
        if self._size == 0:
            return None

        cur = self.__get_tail_node()
        
        if self._size == 1:
            self._head = None
            self._tail = None
            self._size = 0
            return cur.get_data()

        # Need to replace the "tail"
        if self.is_reversed():
            self._head = cur.get_prev(True)
            self._head.set_next(None, True)
        else:
            self._tail = cur.get_prev(False)
            self._tail.set_next(None, False)
        self._size -= 1
        return cur.get_data()

    def find_element(self, elem: Any) -> Any | bool:
        """
        Looks at the data inside each node of the list and returns True
        if a match is found; False otherwise.
        Time complexity for full marks: O(N)
        """
        for cur in self._iterate():
            if cur.get_data() == elem:
                return True
        return False

    def find_and_remove_element(self, elem: Any) -> Any | bool:
        """
        Looks at the data inside each node of the list; if a match is
        found, this node is removed from the linked list, and True is returned.
        False is returned if no match is found.
        Time complexity for full marks: O(N)
        """
        # 1. Search and get a reference on the first match
        ref = None
        for cur in self._iterate():
            if cur.get_data() == elem:
                ref = cur
                break
        # Not found - easy peasy
        if ref is None:
            return False
        # Case: head is tail => single element list
        if self.get_size() == 1:
            self._head = None
            self._tail = None
            self._size = 0
            return True 
        # OK: A "regular" case then
        nxt = cur.get_next(self.is_reversed())
        prv = cur.get_prev(self.is_reversed())
        # Easy case: In the middle of two nodes
        if prv is not None and nxt is not None:
            self._size -= 1
            prv.set_next(nxt, self.is_reversed())
            nxt.set_prev(prv, self.is_reversed())
            return True
        # Trickier case: At one end of the list.
        head = self._head
        tail = self._tail
        # mind-bender: If we have a "non-reversed" list and we want to
        # delete the head, OR we have a "reversed" list and we want to
        # delete the tail, we must call "remove_from_front"
        if (cur is head and not self.is_reversed()) or \
           (cur is tail and self.is_reversed()):
            self.remove_from_front()
            
        # Otherwise, we remove from the logical back
        else:
            self.remove_from_back()
        return True

    def reverse(self) -> None:
        """
        Reverses the linked list
        Time complexity for full marks: O(1)
        """
        if self.is_reversed():
            self._reversed = False
        else:
            self._reversed = True