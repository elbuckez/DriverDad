from pygame.locals import *
import pygame, string

class KeyboardClass:
    def __init__( self ):
        self.letter_typed = ""
        self.shift_pressed = False
        
    def handle_key_up_event( self, event ):
        if event.key == 304:
            self.shift_pressed = False
            return
        return

    def handle_key_down_event( self, event ):
        print( event.key )
        self.letter_typed = ""
        if event.key in [8, 9, 13, 32]:
            self.handle_operational_keydown( event.key );
            return
        if event.key == 304:
            self.shift_pressed = True
            return
        if event.key == 97:
            self.letter_typed = "a"
            return
        elif event.key == 101:
            self.letter_typed = "e"
            return
        elif event.key == 105:
            self.letter_typed = "i"
            return
        elif event.key == 111:
            self.letter_typed = "o"   
            return
        elif event.key == 117:
            self.letter_typed = "u"
            return
            
        elif event.key == 114:
            self.letter_typed = "r"
            return
        elif event.key == 115:
            self.letter_typed = "s"
            return
        elif event.key == 116:
            self.letter_typed = "t"
            return
        elif event.key == 109:
            self.letter_typed = "m"
            return
        elif event.key == 110:
            self.letter_typed = "n"
            return
        elif event.key == 100:
            self.letter_typed = "d"
            return
        elif event.key == 108:
            self.letter_typed = "l"
            return
               
        elif event.key == 98:
            self.letter_typed = "b"
            return
        elif event.key == 99:
            self.letter_typed = "c"
            return
        elif event.key == 102:
            self.letter_typed = "f"
            return
        elif event.key == 103:
            self.letter_typed = "g"
            return
        elif event.key == 104:
            self.letter_typed = "h"
            return
        elif event.key == 106:
            self.letter_typed = "j"
            return
        elif event.key == 107:
            self.letter_typed = "k"
            return
        elif event.key == 112:
            self.letter_typed = "p"
            return
            
        elif event.key == 113:
            self.letter_typed = "q"
            return
        elif event.key == 118:
            self.letter_typed = "v"
            return
        elif event.key == 119:
            self.letter_typed = "w"
            return
        elif event.key == 120:
            self.letter_typed = "x"
            return
        elif event.key == 121:
            self.letter_typed = "y"
            return
        elif event.key == 122:
            self.letter_typed = "z"
            return
        
        elif event.key == 46:
            self.letter_typed = "."
            return
        elif event.key == 47:
            self.letter_typed = "?"
            return
        elif event.key == 48:
            self.letter_typed = "0"
            return
        elif event.key == 49:
            self.letter_typed = "1"
            return
        elif event.key == 50:
            self.letter_typed = "2"
            return
        elif event.key == 51:
            self.letter_typed = "3"
            return
        elif event.key == 52:
            self.letter_typed = "4"
            return
        elif event.key == 53:
            self.letter_typed = "5"
            return
        elif event.key == 54:
            self.letter_typed = "6"
            return
        elif event.key == 55:
            self.letter_typed = "7"
            return
        elif event.key == 56:
            self.letter_typed = "8"
            return
        elif event.key == 57:
            self.letter_typed = "9"
            return
  
    def handle_operational_keydown( self, key ):
        if key == 8:
            if self.shift_pressed == True:
                self.letter_typed = "clear"
                return
            self.letter_typed = "delete"
            return
        elif key == 9:
            self.letter_typed = "tab"
            return
        elif key == 13:
            self.letter_typed = "enter"
            return
        elif key == 32:
            self.letter_typed = "space"
            return