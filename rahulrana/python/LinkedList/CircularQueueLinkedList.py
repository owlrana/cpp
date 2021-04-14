# Implementing a truly circular queue using a linked list

class CircularQueue:
    """Queue implementation using circularly linked list."""

    class _Node:
        """Lightweight, non public class for storing a singly linked node."""
        __slots__ = '_element', '_next' # to streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        """Create an empty queue."""
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        Raise exception if the queue is empty.
        """
        if self._size == 0:
            raise Exception("CIRCULAR QUEUE IS EMPTY!")
        head = self._tail._next
        return head._element

    def dequeue(self):
        """Remove and return the first element of the queue. (FIFO)
        Raise exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception("CIRCULAR QUEUE IS EMPTY!")
        old_head = self._tail._next
        if self._size == 1: # removing the only element that is present
            self._tail = None # Queue becomes empty
        else:
            self._tail._next = old_head._next # Remove reference from old head (skip it)
        self._size -= 1
        return old_head._element

    def enqueue(self, e):
        """Insert a new element to the back of the queue."""
        newest = self._Node(e, None) # node will be the new tail node
        if self.is_empty():
            newest._next = newest # initialize circularly
        else:
            newest._next = self._tail._next # new node points to the head
            self._tail._next = newest # old tail's nextx should now point to the new node
        self._tail = newest # new node becomes the new tail
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next # old head becomes the new tail

    def __str__(self):
        """Print the contents of the linked list through print() function"""
        if self.is_empty():
            raise Exception('LINKED QUEUE IS EMPTY!!')
        lst = []
        header = self._tail # assign header to head so real head doesn't change
        for i in range(len(self)): # iterate till the header is at the end
            header = header._next # make header the next value of the node, and iterate again
            lst.append(header._element) # store the value of Node's Element in lst
        return str(lst)

if __name__ == "__main__":
    LinkedList = CircularQueue()
    LinkedList.enqueue(5)
    LinkedList.enqueue(6)
    LinkedList.enqueue(7)
    LinkedList.enqueue(8)
    print(LinkedList)
    LinkedList.dequeue()
    print(LinkedList)