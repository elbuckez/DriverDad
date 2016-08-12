import sys
sys.path.append('documents/Coding/Python/DriverDad')

#import the classes we need
from Classes.Application import *
from Classes.CashInputBox import *
from Classes.DisplayBox import *
from Classes.InputBox import *
from Classes.Keyboard import *
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
    global Driver, Keyboard
    pygame.init()
    Driver = Application( screen_width, screen_height, fps, title, background_colour)
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
            check_inputs( Driver.input_boxes, Driver.buttons, pos )

def draw_ui( ui_elements ):
    for i in ui_elements:
        if isinstance( i, list ):
            for j in i:
                j.draw( Driver )
        else:
            i.draw(Driver)

def check_inputs( boxes, buttons, pos ):
    list = boxes + buttons
    for i in list:
        if i.rect.collidepoint(pos):
            i.select()
        else:
            i.deselect()
            
def get_selected_box( boxes ):
    for i in boxes:
        if i.selected == True:
            return i

def init_ui_elements():
    SubmitButton = TextButton( button_w, button_h, button_x, button_y, "SUBMIT", button_fill, button_highlight, Driver)
    
    Intro1 = TextBox( intro_w, intro_h, intro_x, intro_y, intro_fill, intro_highlight, introduction1,  Driver )  
    Intro2 = TextBox( intro_w, intro_h, intro_x, Intro1.y + intro_ygap, intro_fill, intro_highlight, introduction2, Driver )  
    Intro3 = TextBox( intro_w, intro_h, intro_x, Intro2.y + intro_ygap, intro_fill, intro_highlight, introduction3,  Driver ) 
    intro_boxes = [ Intro1, Intro2, Intro3 ]
    
    StartPoint = TitleBox( display_bx_w, display_bx_h, display_bx_x, display_bx_y, display_bx_fill, start_title, display_bx_highlight, Driver)
    Destination = TitleBox( display_bx_w, display_bx_h, display_bx_x, StartPoint.y + display_bx_ygap, display_bx_fill, destination_title, display_bx_highlight, Driver)
    PickUpTime = TitleBox( display_bx_w, display_bx_h, display_bx_x, Destination.y + display_bx_ygap, display_bx_fill, pick_up_title, display_bx_highlight, Driver)
    PickUpTimeHour = TitleBox( input_bx_w/4, display_bx_h, input_bx_x, PickUpTime.y, display_bx_fill, "Hour: ", display_bx_highlight, Driver )
    PickUpTimeMin = TitleBox( input_bx_w/4, display_bx_h, input_bx_x + input_bx_w*0.5, PickUpTime.y, display_bx_fill, "Minutes: ", display_bx_highlight, Driver )
    Cost = TitleBox( display_bx_w, display_bx_h, display_bx_x, PickUpTime.y + display_bx_ygap, display_bx_fill, cost_title, display_bx_highlight, Driver)
    title_boxes = [ StartPoint, Destination, PickUpTime, PickUpTimeHour, PickUpTimeMin, Cost ]
    
    IB_StartPoint = InputBox( input_bx_w, input_bx_h, input_bx_x, input_bx_y, input_bx_fill, input_box_highlight, Driver  )
    IB_Destination = InputBox( input_bx_w, input_bx_h, input_bx_x, IB_StartPoint.y + input_bx_ygap, input_bx_fill, input_box_highlight, Driver  )
    IB_PickUpHours = TimeBox( input_bx_w/4, input_bx_h, input_bx_x + input_bx_w * 0.25, IB_Destination.y + input_bx_ygap, input_bx_fill, input_box_highlight, Driver  )
    IB_PickUpMinutes = TimeBox( input_bx_w/4, input_bx_h, input_bx_x + input_bx_w * 0.75, IB_PickUpHours.y, input_bx_fill, input_box_highlight, Driver )
    IB_Cost = CashInputBox( input_bx_w, input_bx_h, input_bx_x, IB_PickUpHours.y + input_bx_ygap, input_bx_fill, input_box_highlight, Driver  )
    input_boxes = [ IB_StartPoint, IB_Destination, IB_PickUpHours, IB_PickUpMinutes, IB_Cost ]
    
    Driver.input_boxes = input_boxes
    Driver.buttons = [SubmitButton]
    return [ intro_boxes, title_boxes, Driver.input_boxes, Driver.buttons ]
             
#MAIN TRICK      
if __name__ == '__main__':
    main()