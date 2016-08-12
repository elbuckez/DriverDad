from colours import *

#SETTINGS

#Application Settings
screen_height = 600
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
intro_ygap = 20 
intro_fill = WHITE
intro_highlight = BLACK

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
input_bx_ygap = 35
input_bx_fill = GREY
input_box_highlight = WHITE

#Button Settings
button_w = input_bx_w/2
button_h = 30
button_x = input_bx_x + 0.5 * button_w
button_y = input_bx_y + 140
button_fill = RED
button_highlight = BLUE




