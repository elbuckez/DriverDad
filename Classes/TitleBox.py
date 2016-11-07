import pygame, sys
from pygame.locals import *
from TextBox import *

class TitleBox(TextBox):

    def __init__( self, width, height, xcoordinate, ycoordinate, fill_colour, text, highlight, application ):
        TextBox.__init__( self, [width, height, xcoordinate, ycoordinate], [fill_colour, highlight], text, application )
    
    def update_text( self, letter, surface ):
        self.text += letter
        textrender = self.font.render( self.text.upper(), 1, application.colour )
        surface.display.blit( textrender, shape )
        
    def clear( self ):
        self.text = ""
        
        