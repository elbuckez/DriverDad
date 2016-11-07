import pygame, sys
from pygame.locals import *
from TextBox import *

class TextButton(TextBox):
    
    def __init__( self, dimensions, colours, text, application ):
        TextBox.__init__( self, dimensions, colours, text, application )
        
    def recolour( self ):
        self.fill = self.base_highlight
        self.highlight = self.base_colour
    
    def unhighlight( self ):
        self.highlight = self.base_highlight
        self.fill = self.base_colour
        print("QUICK")
        
    def click( self ):
        print("HERE")
        
    def select( self ):
        self.recolour()
        
    def deselect( self ):
        self.selected = False
        self.unhighlight()
        
        
