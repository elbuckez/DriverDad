import pygame, sys
from pygame.locals import *
from TextBox import *

class DisplayBox:
    
    def __init__( self, width, height, colour, text_to_display, text_colour, xcoordinate, ycoordinate, application ):
        self.width = width
        self.height = height
        self.colour = colour
        self.text_to_display = text_to_display
        self.text_colour = text_colour
        self.xcoordinate = xcoordinate
        self.ycoordinate = ycoordinate
        self.font = application.get_font()
       
    def draw( self, surface ):
        rect = pygame.draw.rect( surface.display, self.colour, (self.xcoordinate, self.ycoordinate, self.width, self.height), 0)
        textrender = self.font.render( self.text_to_display, 1, self.text_colour )
        shape = textrender.get_rect()
        shape.center = ( rect.center )
        surface.display.blit( textrender, shape )
        
        
        
        
        