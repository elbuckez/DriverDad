import sys
sys.path.append('documents/Coding/Python/DriverDad')

#import the classes we need
from Classes.Application import *
from Classes.CashInputBox import *
from Classes.ClearButton import *
from Classes.DisplayBox import *
from Classes.InputBox import *
from Classes.Keyboard import *
from Classes.PrintButton import *
from Classes.PrintPreview import *
from Classes.SubmitButton import *
from Classes.TextBox import *
from Classes.TextButton import *
from Classes.TimeBox import *
from Classes.TitleBox import *
from Classes.WebsiteParser import *

# import the resources we need
from Resources.colours import *
from Resources.events import *
from Resources.settings import *
from Resources.text import *



def main():
    global Driver, Keyboard, Submit, Print, Clear, Preview
    pygame.init()
    Driver = Application( screen_width, screen_height, fps, title, background_colour)
    Submit = SubmitButton( [button_w, button_h, submit_button_x, submit_button_y], [button_fill, button_highlight], submit_button_text, Driver )
    Clear = ClearButton( [button_w, button_h, clear_button_x, clear_button_y], [button_fill, button_highlight], clear_button_text, Driver )
    Print = PrintButton( [print_button_w, print_button_h, print_button_x, print_button_y], [print_button_fill, print_button_highlight, print_button_run_colour], print_button_text, Driver)
    Preview = PrintPreview( pp_w, pp_h, pp_colour, pp_text, pp_highlight, pp_x, pp_y, Driver)
    buttons = [ Submit, Clear, Print ]
    WebTrawler = WebsiteParser()
    ui_elements = init_ui_elements()
    Keyboard = KeyboardClass()
    
    while True:
        Driver.run()
        eventhandler()
        draw_ui( ui_elements )
        pygame.display.update()
        Driver.fpsclock.tick( Driver.fps )
    

def eventhandler():
    for event in pygame.event.get():
        if event.type == QUIT:
            Driver.close()
        elif event.type == KEYUP:
            Keyboard.handle_key_up_event( event )
        elif event.type == KEYDOWN:
            Keyboard.handle_key_down_event( event )              
            box = get_selected_box( Driver.input_boxes )
            if box:
                box.update_text( Keyboard.letter_typed, Driver )
 
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            check_inputs( Driver.input_boxes, pos )

def draw_ui( ui_elements ):
    for i in ui_elements:
        for j in i:
            j.draw( Driver )
    Submit.draw( Driver )
    if Print.enabled == True:
        Print.draw( Driver )
    Clear.draw( Driver )
    if Preview.enabled == True:
        Preview.draw( Driver )

def check_inputs( boxes, pos ):
    for i in boxes:
        if i.rect.collidepoint(pos):
            i.select()
        else:
            i.deselect()
    if Print.enabled == True:
        if Print.rect.collidepoint(pos) and Print.enabled == True:
            Print.run( boxes )
    
    if Submit.rect.collidepoint(pos):
        Submit.press( boxes, Driver, Preview )
        Print.enable()
    elif Clear.rect.collidepoint(pos):
        Clear.press( boxes, Print, Preview )
        Print.disable()

            
def get_selected_box( boxes ):
    for i in boxes:
        if i.selected == True:
            return i

def init_ui_elements():
    Intro1 = TextBox( intro_dimensions, intro_colours, introduction1,  Driver )  
    Intro2 = TextBox( [intro_w, intro_h, intro_x, Intro1.y + intro_ygap], intro_colours, introduction2, Driver )  
    Intro3 = TextBox( [intro_w, intro_h, intro_x, Intro2.y + intro_ygap], intro_colours, introduction3,  Driver ) 
    intro_boxes = [ Intro1, Intro2, Intro3 ]
    
    StartPoint = TitleBox( display_bx_w, display_bx_h, display_bx_x, display_bx_y, display_bx_fill, start_title, display_bx_highlight, Driver)
    Destination = TitleBox( display_bx_w, display_bx_h, display_bx_x, StartPoint.y + display_bx_ygap, display_bx_fill, destination_title, display_bx_highlight, Driver)
    PickUpTime = TitleBox( display_bx_w, display_bx_h, display_bx_x, Destination.y + display_bx_ygap, display_bx_fill, pick_up_title, display_bx_highlight, Driver)
    PickUpTimeHour = TitleBox( input_bx_w/4, display_bx_h, input_bx_x, PickUpTime.y, display_bx_fill, "Hour: ", display_bx_highlight, Driver )
    PickUpTimeMin = TitleBox( input_bx_w/4, display_bx_h, input_bx_x + input_bx_w*0.5, PickUpTime.y, display_bx_fill, "Minutes: ", display_bx_highlight, Driver )
    Cost = TitleBox( display_bx_w, display_bx_h, display_bx_x, PickUpTime.y + display_bx_ygap, display_bx_fill, cost_title, display_bx_highlight, Driver)
    title_boxes = [ StartPoint, Destination, PickUpTime, PickUpTimeHour, PickUpTimeMin, Cost ]
    
    IB_StartPoint = InputBox( input_dimensions, input_colours, Driver  )
    IB_Destination = InputBox( [input_bx_w, input_bx_h, input_bx_x, IB_StartPoint.y + input_bx_ygap], input_colours, Driver  )
    IB_PickUpHours = TimeBox( [input_bx_w/4, input_bx_h, input_bx_x + input_bx_w * 0.25, IB_Destination.y + input_bx_ygap], input_colours, Driver, "HOUR"  )
    IB_PickUpMinutes = TimeBox( [input_bx_w/4, input_bx_h, input_bx_x + input_bx_w * 0.75, IB_PickUpHours.y], input_colours, Driver, "MINUTE" )
    IB_Cost = CashInputBox( [input_bx_w, input_bx_h, input_bx_x, IB_PickUpHours.y + input_bx_ygap], input_colours, Driver  )
    input_boxes = [ IB_StartPoint, IB_Destination, IB_PickUpHours, IB_PickUpMinutes, IB_Cost ]
    
    Driver.input_boxes = input_boxes
    return [ intro_boxes, title_boxes, Driver.input_boxes ]
             
#MAIN TRICK      
if __name__ == '__main__':
    main()