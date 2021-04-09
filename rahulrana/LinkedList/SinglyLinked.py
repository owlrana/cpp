# Singly Linked List

class LinkedStack():
    """LIFO Stack implementation using a singly linked list for storage."""

    #----- nested _Node Class -----
    class _Node:
        """Lightweight, non-public class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    #----- stack methods -----
    def __init__(self):
        """Create an empty stack."""
        self._head = None
        self._size = 0
    
    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size 
    
    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, element):
        """Add element "element" to the top of the stack"""
        self._head = self._Node(element, self.head)
        self._size += 1

    def top(self):
        """Return (but no remove) the top element of the stack.
        Raise exception Empty if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty!")
        return self._head.__element

    def pop(self):
        """Remove and return the element from the top of the stack.
        Raise exception Empty if the stack is empty.
        """
        if self.is_empty():
            raise Empty("Stack is empty!")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer