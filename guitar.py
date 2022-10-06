from guitarstring import GuitarString
from stdaudio import play_sample
import sys
import pygame

if __name__ == '__main__':
    pygame.init()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))


    class GuitarStrings:
        def __init__(self, y):
            self.y = y
            self.freq = GuitarString(440 * (1.059463 ** (self.y - 12)))

    keyList = []
    keyboard = "q2we4r5ty7u8i9op"

    for i in range(16):
        keyList.append(GuitarStrings(i))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key = event.unicode
                if key in keyboard:
                    keyList[keyboard.index(key)].freq.pluck()

        sample = 0
        for s in keyList:
            sample += s.freq.sample()
        play_sample(sample)

        for x in keyList:
            x.freq.tick()

