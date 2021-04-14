from LinkedList.DoublyLinkedList import *

class LinkedQueue(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Exception("Doubly Linked Queue is Empty!")
        return self._header._next._element # real item just after the header

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Exception("Doubly Linked Queue is Empty!")
        return self._trailer._previous._element # real item just before the trailer

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next) #after header

    def insert_last(self, e):
        """Add an element to the last of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer) # just before the trailer

    def delete_first(self):
        """Remove and return the element from the front of the deque."""
        if self.is_empty():
            raise Exception("Doubly Linked List is Empty!")
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove and return the element from the back of the deque."""
        if self.is_empty():
            raise Exception("Doubly Linked List is Empty!")
        return self._delete_node(self._trailer._prev)