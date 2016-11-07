import pygame, sys
from TextBox import *
from pygame.locals import *

class InputBox(TextBox):

    def __init__( self, dimensions, colours, application ):
        TextBox.__init__( self, dimensions, colours, "", application )
        self.selected = False
        self.font = pygame.font.SysFont( "monaco", 25 )
    
    def draw( self, surface ):
        if ( self.selected == True ):
            colour = self.highlight
            self.text_colour = self.fill
        else:
            colour = self.fill
            self.text_colour = self.highlight
        self.rect = pygame.draw.rect( surface.display, colour, (self.x, self.y, self.width, self.height), 0)
        textrender = self.font.render( self.text, 1, self.text_colour )
        self.shape = textrender.get_rect()
        self.shape.center = self.rect.center
        self.rect
        surface.display.blit( textrender, self.shape )
    
    def update_text( self, letter, application ):
        if letter == "delete":
            self.backspace()
        elif letter == "clear":
            self.clear()
        elif letter == "enter":
            self.selected = False
        elif letter == "space":
            self.text += " "
        elif letter == "tab":
            self.tab( application )
        elif ( len( self.text ) < 38 ):
            self.text += letter.upper()
        else:
            return
        textrender = self.font.render( self.text.upper(), 1, application.colour )
        application.display.blit( textrender, self.shape )
    
    def backspace( self ):
        self.text = self.text[:-1]
        
    def clear( self ):
        self.text = ""
        
    def submit_pressed( self ):
        return self.text
        
    def select( self ):
        self.selected = True
        
    def deselect( self ):
        self.selected = False

    def tab( self, application ):
        j = -1
        for i in application.input_boxes:
            j += 1
            if i == self:
                if j >= (len(application.input_boxes) - 1):
                    application.input_boxes[0].select()
                    application.input_boxes[j].deselect()
                else:
                    application.input_boxes[j + 1].select()
                    application.input_boxes[j].deselect()
            