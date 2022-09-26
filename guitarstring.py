#!/usr/bin/env python3

class GuitarString:
    def __init__(self, frequency: float):
        '''
        Create a guitar string of the given frequency, using a sampling rate of 24000 Hz
        '''
        # TO-DO: implement this

    def make_from_array(self, init: list[int]):
        '''
        Create a guitar string whose size and initial values are given by the array `init`
        '''
        # TO-DO: implement this

    def pluck(self):
        '''
        Set the buffer to white noise
        '''
        # TO-DO: implement this

    def tick(self):
        '''
        Advance the simulation one time step by applying the Karplus--Strong update
        '''
        # TO-DO: implement this

    def sample(self) -> float:
        '''
        Return the current sample
        '''
        # TO-DO: implement this

    def time(self) -> int:
        '''
        Return the number of ticks so far
        '''
        # TO-DO: implement this
