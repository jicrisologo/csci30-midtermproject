#!/usr/bin/env python3

from guitarstring import GuitarString
from stdaudio import play_sample
import sys
import pygame

if __name__ == '__main__':
    pygame.init()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))

    CONCERT_A = 440
    CONCERT_C = CONCERT_A * (1.059463**3)
    string_A = GuitarString(CONCERT_A)
    string_C = GuitarString(CONCERT_C)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key = event.unicode
                if key == 'a':
                    string_A.pluck()
                elif key == 'c':
                    string_C.pluck()

        sample = string_A.sample() + string_C.sample()
        play_sample(sample)

        string_A.tick()
        string_C.tick()
