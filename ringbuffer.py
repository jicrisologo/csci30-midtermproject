#!/usr/bin/env python3

class RingBuffer: #this can definitely still be optimized :(
    def __init__(self, capacity: int):
        '''
        Create an empty ring buffer, with given max capacity
        '''
        
        self.data = [None] * capacity
        self.head = 0 #insertion point
        self.tail = 0 #deletion point
        
        self.MAX_CAP = capacity # UPDATE: for consistency, also have an attribute "self.MAX_CAP" to store the max capacity

        self.items = 0


    def size(self) -> int: 
        '''
        Return number of items currently in the buffer
        '''
        return self.items


    def is_empty(self) -> bool:
        '''
        Is the buffer empty (size equals zero)?
        '''
        for x in self.data:
            if x is not None:
                return False
        return True

        
    def is_full(self) -> bool:
        '''
        Is the buffer full (size equals capacity)?
        '''
        if self.size() == self.MAX_CAP:
            return True
        else:
            return False


    def enqueue(self, x: float):
        '''
        Add item `x` to the end
        '''
        if self.size() == self.MAX_CAP:
            raise RingBufferFull
        
        self.data[self.head] = x
        
        self.head += 1
        if self.head == self.MAX_CAP:
            self.head = 0

        self.items += 1


    def dequeue(self) -> float:
        '''
        Return and remove item from the front
        '''
        if self.size() == 0:
            raise RingBufferEmpty
        
        popped = self.data[self.tail]
        self.data[self.tail] = None
        
        self.tail += 1
        if self.tail == self.MAX_CAP:
            self.tail = 0

        self.items -= 1

        return popped


    def peek(self) -> float:
        '''
        Return (but do not delete) item from the front
        '''
        if self.size() == 0:
            raise RingBufferEmpty
        
        return self.data[self.tail]





class RingBufferFull(Exception):
    pass

class RingBufferEmpty(Exception):
    pass
