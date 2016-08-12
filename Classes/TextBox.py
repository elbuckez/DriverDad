import pygame, sys
from pygame.locals import *

class TextBox(object):

    def __init__( self, width, height, xcoordinate, ycoordinate, fill_colour, highlight, text, application ):
        self.width = width
        self.height = height
        self.x = xcoordinate
        self.y = ycoordinate
        self.fill = fill_colour
        self.font = application.get_font()
        self.text = text
        self.highlight = highlight
        self.base_highlight = highlight
        self.base_colour = fill_colour
        
    def draw( self, application ):
        self.rect = pygame.draw.rect( application.display, self.fill, ( self.x, self.y, self.width, self.height), 0)
        textrender = self.font.render( self.text.upper(), 1, self.highlight )
        self.shape = textrender.get_rect()
        self.shape.center = self.rect.center
        application.display.blit( textrender, self.shape )
        
        
        