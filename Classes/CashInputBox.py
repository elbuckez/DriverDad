import pygame, sys
from TextBox import *
from pygame.locals import *
from InputBox import *

class CashInputBox(InputBox):

        def __init__( self, dimensions, colours, application ):
                InputBox.__init__( self, dimensions, colours, application )
                self.text = "$"
                self.font = pygame.font.SysFont("arial", 15)
                
        def update_text( self, letter, application ):
                if letter == "delete":
                        if len( self.text ) != 1:
                                self.backspace()
                elif letter in ("0","1","2","3","4","5","6","7","8","9",".", "enter","tab"):
                        super( CashInputBox, self ).update_text( letter, application )

        def clear( self ):
                self.text = "$"