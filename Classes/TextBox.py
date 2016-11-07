import pygame, sys
from pygame.locals import *

class TextBox(object):

    def __init__( self, dimensions, colours, text, application ):
        self.width = dimensions[ 0 ]
        self.height = dimensions[ 1 ]
        self.x = dimensions[ 2 ]
        self.y = dimensions[ 3 ]

        self.fill = colours[ 0 ]
        self.highlight = colours[ 1 ]

        self.base_colour = self.fill
        self.base_highlight = self.highlight
        

        self.font = application.get_font()
        self.text = text
        
        
        
    def draw( self, application ):
        self.rect = pygame.draw.rect( application.display, self.fill, ( self.x, self.y, self.width, self.height), 0)
        textrender = self.font.render( self.text.upper(), 1, self.highlight )
        self.shape = textrender.get_rect()
        self.shape.center = self.rect.center
        application.display.blit( textrender, self.shape )
        
        
        