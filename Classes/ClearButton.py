from TextButton import *

class ClearButton( TextButton ):

    def __init__( self, dimensions, colours, text, application ):
        TextButton.__init__( self, dimensions, colours, text, application )


    def press( self, input_boxes, print_button, print_preview ):
        for i in input_boxes:
            i.clear()
        print_button.disable()
        print_preview.disable()