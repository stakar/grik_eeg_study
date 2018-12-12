import pygame
from random import shuffle

class SimpleRectangle(object):

        def __init__(self, freqs, win_size=(800, 800), position=(0, 0),
                     stim_size=(800, 800), colors=((255, 255, 255), (0, 0, 0)),
                     image=('1','2','3','4')):

            self.freqs = freqs
            self.win_size = win_size
            self.position = position
            self.stim_size = stim_size
            self.colors = colors
            self.image = image


        def display_stimuli(self,colors,size,pos,freq,image):

            okno = self.window
            okno.blit(image, pos)
            pygame.display.flip()
            self.clock.tick(int(freq*2.))

            pygame.draw.rect(self.window, colors[1], pos+size)
            pygame.display.flip()
            self.clock.tick(int(freq*2.))

        def start_display(self):

            self.window = pygame.display.set_mode(self.win_size, 0, 32)
            self.clock = pygame.time.Clock()
            pygame.init()
            state=StateSimulator()
            bod1 = pygame.image.load('bod1.jpg')
            bod2 = pygame.image.load('bod2.jpg')
            bod3 = pygame.image.load('bod3.jpg')
            cont = pygame.image.load('control.jpg')
            list_of_stim = [bod1,bod2,bod3,cont]*5
            vocab = {bod1:1,bod2:2,bod3:3,cont:4}
            shuffle(list_of_stim)
            start_ticks = pygame.time.get_ticks()

            while True:
                seconds = (pygame.time.get_ticks() - start_ticks) / 1000
                for n in range(20):
                    if seconds < (5+(10*n)):
                        state.value = 0
                    elif seconds < (10+(10*n)):
                        state.value = vocab[list_of_stim[n]],
                        self.display_stimuli(self.colors,self.stim_size,self.position,self.freqs[0],
                                             list_of_stim[n])
                    elif seconds > 210:
                        pygame.quit()

class StateSimulator(object):
    def __init__(self):
        self.value=0

projekt=SimpleRectangle([10,15])
projekt.start_display()
