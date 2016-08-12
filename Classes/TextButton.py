import pygame, sys
from pygame.locals import *
from TextBox import *

class TextButton(TextBox):
    
    def __init__( self, width, height, xcoordinate, ycoordinate, text, base_colour, highlight, application ):
        TextBox.__init__( self, width, height, xcoordinate, ycoordinate, base_colour, highlight, text, application )
        
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
        print("IN BUTTON SELECT")
        self.click()
        self.recolour()
        
    def deselect( self ):
        self.selected = False
        self.unhighlight()
        
        
