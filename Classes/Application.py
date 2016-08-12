import pygame, sys
from pygame.locals import *

class Application:
    
    def __init__( self, width, height, fps, title, colour ):
        self.height = height
        self.width = width
        self.fps = fps
        self.title = title
        self.colour = colour
        self.display = pygame.display.set_mode(( self.width, self.height ))
        self.font = pygame.font.SysFont( "arial", 10 )
        self.fpsclock = pygame.time.Clock()
        self.xmargin = 15
        self.ymargin = 15
        self.number_of_text_boxes = 0
        pygame.display.set_caption( self.title )
        self.buttons = []
        self.input_boxes = []
    
    def run( self ):
        self.display.fill( self.colour )
    
    def get_font( self ):
        return self.font
    
    def close(self):
        pygame.quit()
        sys.exit() 
    