#!/usr/bin/env python3

from ringbuffer import *
import math #idk if this is allowed
import random #idk if this is allowed


ENERGY_DECAY_FACTOR = 0.996 #temporary, remove whenever this isnt needed anymore


class GuitarString:
    def __init__(self, frequency: float):
        '''
        Create a guitar string of the given frequency, using a sampling rate of 24000 Hz
        '''
        self.capacity = math.ceil(24000 / frequency)
        self.buffer = RingBuffer(self.capacity)
        self.ticks = 0

        for _ in range(self.capacity):
            self.buffer.enqueue(0)


    @classmethod
    def make_from_array(cls, init: list[int]):
        '''
        Create a guitar string whose size and initial values are given by the array `init`
        '''
        # create GuitarString object with placeholder freq
        stg = cls(1000)

        stg.capacity = len(init)
        stg.buffer = RingBuffer(stg.capacity)
        for x in init:
            stg.buffer.enqueue(x)
        return stg


    def pluck(self):
        '''
        Set the buffer to white noise
        '''
        for _ in range(self.capacity):
            self.buffer.dequeue()
            self.buffer.enqueue( random.uniform(-0.5, 0.5) )


    def tick(self):
        '''
        Advance the simulation one time step by applying the Karplus--Strong update
        '''

        self.ticks += 1
        
        f1 = self.buffer.dequeue()
        f2 = self.buffer.peek()

        self.buffer.enqueue( (f1 + f2) / 2 * ENERGY_DECAY_FACTOR )
        

    def sample(self) -> float:
        '''
        Return the current sample
        '''
        return self.buffer.peek()


    def time(self) -> int:
        '''
        Return the number of ticks so far
        '''
        return self.ticks
