from TextButton import *

class SubmitButton( TextButton ):

    def __init__( self, dimensions, colours, text, application ):
        TextButton.__init__( self, dimensions, colours, text, application )

    def press( self, input_boxes, application, print_preview ):
        print_preview.enable()