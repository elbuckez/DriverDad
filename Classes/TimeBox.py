import pygame, sys
from InputBox import *
from pygame.locals import *

class TimeBox(InputBox):

    def __init__( self, dimensions, colours, application, type ):
        InputBox.__init__(  self, dimensions, colours, application )
        self.font = pygame.font.SysFont("arial", 15)
        self.type = type
        
    def update_text( self, letter, application ):
        if letter == "delete":
            self.text = self.text[:-1].upper()
        elif letter == "enter":
            self.selected = False
        elif letter == "space":
            self.text += " "
        elif letter == "tab":
            self.tab( application )
        else:
            self.handle_text_input( letter, application )
        textrender = self.font.render( self.text.upper(), 1, application.colour )
        application.display.blit( textrender, self.shape )\

    def handle_text_input( self, letter, application ):
        valid = False
        if len( self.text ) < 2:
            if self.type == "HOUR":
                if len( self.text ) == 1:
                    if self.text == "2":
                        if letter in ("0", "1", "2", "3"):
                            valid = True
                    elif self.text in ( "3","4","5","6","7","8","9"):
                        valid = False
                    else:
                        if letter in ("0","1","2","3","4","5","6","7","8","9"):
                            valid = True
                else:
                    if letter in ("0","1","2","3","4","5","6","7","8","9"):
                            valid = True

            elif self.type == "MINUTE":
                if len( self.text ) == 0:
                    if letter in ("0","1","2","3","4","5"):
                        valid = True
                else:
                    valid = True

            else:
                assert( "NO VALID TYPE SET FOR TIME BOX")
        elif len( self.text ) == 2:
            self.clear()
            self.handle_text_input( letter, application )
        if valid == True:
            self.text += letter.upper()
            if self.type == "HOUR" and ( len( self.text ) == 2 or self.text in ( "3","4","5","6","7","8","9") ):
                self.tab( application )