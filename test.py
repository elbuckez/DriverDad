
from Resources.colours import *
from Resources.text import *

def generateText( destination, start_point, cost, start_time, current_date, fuel_cost ):
    header = "\t \t \t \t" + start_point.upper() + " ---> " + destination.upper() + "\t \t " + current_date + "\n"
    start_line = start_title + "\t " + start_point + "\n"
    destination_line = destination_title + "\t " + destination + "\n""
    text_to_display = header + start_line + destination_line
    return text_to_display

def write_to_text_file( text_to_display ):
    filepath = "Users/Archie/Documents/Coding/Python/DriverDad/Resources"
    file = open("journey.txt","w")
    file.write( text_to_display )

def main():
    run = True
    text_to_display = ""
    while ( run ):
        if run:
            text_to_display = generateText( "Folkestone", "Germany", 100, 12.54, "12.05.1991", 100 )
            run = False;
    write_to_text_file( text_to_display )
main()