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
        self._head = self._Node(element, self._head)
        self._size += 1

    def top(self):
        """Return (but no remove) the top element of the stack.
        Raise exception Empty if the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty!")
        return self._head._element

    def pop(self):
        """Remove and return the element from the top of the stack.
        Raise exception Empty if the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty!")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def __str__(self):
        """Print the contents of the linked list through print() function"""
        if self.is_empty():
            raise Exception('Exception: LIST IS EMPTY!!')
        lst = []
        header = self._head # assign header to head so real head doesn't change
        for i in range(len(self)): # iterate till the header is at the end
            lst.append(header._element) # store the value of Node's Element in lst
            header = header._next # make header the next value of the node, and iterate again
        return str(lst)

    def remove(self, index):
        """Removes the given index from the linked list."""
        if self.is_empty():
            raise Exception('Exception: LIST IS EMPTY!!')
        if len(self) < index:
            return 'Exception: ILLEGAL INDEX NUMBER GIVEN!'
        if index == 0:
            if len(self) == 1:
                self._head = None
                self._size -= 1
                return
            self._head = self._head._next
            self._size -= 1
            return
        header = self._head # assign header to head so real head doesn't change
        for i in range(index - 1): # iterate till the header is at the end
            header = header._next # make header the next value of the node, and iterate again
        header._next = header._next._next
        self._size -= 1
        return

if __name__ ==  "__main__":
    linked_list = LinkedStack()
    linked_list.push(5)
    linked_list.push(6)
    linked_list.push(10)
    linked_list.push(12)
    linked_list.push(20) # testing push()
    print(linked_list) # testing print()
    linked_list.pop() # testing pop()
    print(linked_list)
    print(linked_list.top()) # testing top()
    linked_list.remove(3) # testing remove()
    print(linked_list)

    # other functions were tested while using the above ones as they already use them under the hood