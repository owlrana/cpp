class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    #----- nested _Nodek Class -----
    class _Node:
        """Lightweight, non-public class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    #----- queue methods -----
    def __init__(self):
        """Create an empty Queue"""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return length of the Linked queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            print("LINKED QUEUE IS EMPTY!")
        return self._head._element

    def dequeue(self):
        """Remove adn return the first element of the queue.
        Raise Empty if the queue is empty
        """
        if self.is_empty():
            print("LINKED QUEUE IS EMPTY!")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty(): # Special case if the queue is now empty
            self._tail = None # The head removed was the tail, need to assign as None now
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None) # Node will be new tail node
        if self.is_empty():
            self._head = newest # special case, if the linked queue was previously empty
        else:
            self._tail._next = newest
        self._tail = newest # update reference to tail node
        self._size += 1