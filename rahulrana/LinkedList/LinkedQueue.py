class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    #----- nested _Node Class -----
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
        """Remove and return the first element of the queue.
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

    def __str__(self):
        """Print the contents of the linked list through print() function"""
        if self.is_empty():
            return 'Exception: LIST IS EMPTY!!'
        lst = []
        header = self._head # assign header to head so real head doesn't change
        for i in range(len(self)): # iterate till the header is at the end
            lst.append(header._element) # store the value of Node's Element in lst
            header = header._next # make header the next value of the node, and iterate again
        return str(lst)

    def remove(self, index):
        """Removes the given index from the linked list."""
        if self.is_empty():
            return 'Exception: LIST IS EMPTY!!'
        if len(self) < index:
            return 'Exception: ILLEGAL INDEX NUMBER GIVEN!'
        if index == 0:
            if len(self) == 1:
                self._head = None
                self._tail = None
                self._size -= 1
                return
            self._head = self._head._next
            self._size -= 1
            return
        header = self._head # assign header to head so real head doesn't change
        for i in range(index - 1): # iterate till the header is at the end
            header = header._next # make header the next value of the node, and iterate again
        header._next = header._next._next
        if index == (len(self) + 1):
            self._tail = header
        self._size -= 1
        return

if __name__ ==  "__main__":
    linked_list = LinkedQueue()
    linked_list.enqueue(5)
    linked_list.enqueue(6)
    linked_list.enqueue(10)
    linked_list.enqueue(12)
    linked_list.enqueue(20) # testing push()
    print(linked_list) # testing print()
    linked_list.dequeue() # testing pop()
    print(linked_list)
    print(linked_list.first()) # testing top()
    linked_list.remove(2) # testing remove()
    print(linked_list)
    
    # other functions were tested while using the above ones as they already use them under the hood