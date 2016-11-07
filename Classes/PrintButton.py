from TextButton import *
from PrintPreview import *

class PrintButton( TextButton ):

    def __init__( self, dimensions, colours, text, application ):
        TextButton.__init__( self, dimensions, [colours[0], colours[1]], text, application )
        self.enabled = False
        self.disabled_colour = self.base_colour
        self.enabled_colour = self.highlight
        self.run_colour = colours[2]
    
    def enable( self ):
        self.select()
        self.enabled = True
        
    def disable( self ):
        print ( "PRINT DISABLE")
        self.deselect()
        self.enabled = False

    def run( self, boxes ):
        self.fill = self.run_colour
        


class NextJobButton( TextButton ):

    def __init__( self, width, height, xcoordinate, ycoordinate, text, base_colour, highlight, application ):
        TextButton.__init__( self, width, height, xcoordinate, ycoordinate, text, base_colour, highlight, application )