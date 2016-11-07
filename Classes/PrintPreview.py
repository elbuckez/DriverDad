import pygame, sys
from pygame.locals import *
from DisplayBox import *
from Resources.text import *

class PrintPreview(DisplayBox):
    
    def __init__( self, width, height, colour, text_to_display, text_colour, xcoordinate, ycoordinate, application ):
        DisplayBox.__init__( self, width, height, colour, text_to_display, text_colour, xcoordinate, ycoordinate, application )
        self.enabled = False
       
    def enable( self ):
        self.enabled = True

    def disable( self ):
        self.enabled = False
        print( "PP DISABLE")

    def generateText( self, destination, start_point, cost, start_time, current_date, fuel_cost ):
        header = "\t \t \t \t" + start_point.upper() + " ---> " + destination.upper() + "\t \t " + current_date + "\n"
        start_line = start_title + "\t " + start_point + "\n"
        destination_line = destination_title + "\t " + destination + "\n""
        self.text_to_display = header + start_line + destination_line

    def write_to_text_file( self ):
        filepath = "Users/Archie/Documents/Coding/Python/DriverDad/Resources"
        file = open("journey.txt","w")
        file.write( self.text_to_display )