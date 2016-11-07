from colours import *

#SETTINGS

#Application Settings
screen_height = 1000
screen_width = 800
fps = 100
background_colour = LIGHT_GREY
title = "Driver Dale"
margin = 50
divide = 10

#Introduction Settings
intro_w = screen_width - 2 * margin
intro_h = 25
intro_x = margin
intro_y = 15
intro_dimensions = [ intro_w, intro_h, intro_x, intro_y ]
intro_ygap = 20 

intro_fill = WHITE
intro_highlight = BLACK
intro_colours = [intro_fill, intro_highlight]


#Display Box Settings
display_bx_w = (screen_width - margin) * 1/3
display_bx_h = 25
display_bx_x = margin
display_bx_y = 150
display_bx_ygap = 35
display_bx_fill = YELLOW
display_bx_highlight = RED

#Input Box Settings
input_bx_w = display_bx_w * 2 - margin
input_bx_h = 25
input_bx_x = margin + display_bx_w + divide
input_bx_y = display_bx_y
input_dimensions = [input_bx_w, input_bx_h, input_bx_x, input_bx_y]
input_bx_ygap = 35

input_bx_fill = GREY
input_box_highlight = WHITE
input_colours = [input_bx_fill, input_box_highlight]

#Generic Button Settings
button_w = input_bx_w/4.2
button_h = 30
submit_button_x = input_bx_x + input_bx_w*0.5
submit_button_y = input_bx_y + 140
clear_button_x = input_bx_x + input_bx_w * 0.75
clear_button_y = submit_button_y
button_fill = RED
button_highlight = BLUE

#Print Button Settings
print_button_w = button_w * 2
print_button_h = 100
print_button_x = submit_button_x
print_button_y = 700
print_button_fill = BLACK
print_button_highlight = WHITE
print_button_run_colour = GREEN

submit_button_text = "SUBMIT"
clear_button_text = "CLEAR"
print_button_text = "PRINT"


# PRINT PREVIEW
pp_w = 450
pp_h = 600
pp_colour = BLUE
pp_text = "PRINT PREVIEW"
pp_highlight = WHITE
pp_x = 50
pp_y = 340


