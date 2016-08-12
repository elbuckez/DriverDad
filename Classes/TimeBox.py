import pygame, sys
from InputBox import *
from pygame.locals import *

class TimeBox(InputBox):

    def __init__( self, width, height, xcoordinate, ycoordinate, fill_colour, highlight, application ):
        InputBox.__init__(  self, width, height, xcoordinate, ycoordinate, fill_colour, highlight, application )
        self.font = pygame.font.SysFont("arial", 15)
        
    def update_text( self, letter, application ):
        if letter == "delete":
            self.text = self.text[:-1].upper()
        elif letter == "enter":
            self.selected = False
        elif letter == "space":
            self.text += " "
        else:
            if len( self.text ) < 2:
                if letter in ("0","1","2","3","4","5","6","7","8","9"):
                                self.text += letter.upper()
        textrender = self.font.render( self.text.upper(), 1, application.colour )
        application.display.blit( textrender, self.shape )