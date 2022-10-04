from guitarstring import GuitarString
from stdaudio import play_sample
import sys
import pygame

if __name__ == '__main__':
    pygame.init()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))


    class Keys:
        def __init__(self, y: int):
            self.y = y

        def freq(self):
            return GuitarString(440 * 1.059463 ** (self.y - 12))
            

    keyList = []
    keyboard = "q2we4r5ty7u8i9op"

    for i in range(16):
        keyList.append(Keys(i))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key = event.unicode
                for x in keyboard:
                    if key == x:
                        keyList[keyboard.index(x)].freq().pluck()

                        print(keyboard.index(x))                    # to check if the key pressed corresponds to the correct index
                        print(keyList[keyboard.index(x)].freq())    # to check if the freq() method works

        sample = 0
        for key in keyList:
            sample += key.freq().sample()
        play_sample(sample)

        for x in keyList:
            x.freq().tick()
