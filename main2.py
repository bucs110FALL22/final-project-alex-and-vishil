import pygame
import os
import random
import math

def set_output_window_position():
    x = 100
    y = 0
    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x, y)


set_output_window_position()

pygame.init()
surface = pygame.display.set_mode((400, 400))


display_size = surface.get_size()
x_display_size = display_size[0]
y_display_size = display_size[1]
diameter = x_display_size*2/3
radius = diameter / 2
center = [x_display_size / 2, y_display_size / 2]

board_color = 'white'
board_lines_color = 'green'
player1_hit_color = 'red'
player1_miss_color = 'pink'
player1_score = 0
player2_hit_color = 'blue'
player2_miss_color = 'light blue'
player2_score = 0
user_box_side = 25
user_box_margin = 25
current_player = 0
dart_radius = 5


# PART A
def draw_dartboard():
    pygame.draw.circle(surface, board_color, center, radius)
    pygame.draw.line(
        surface,
        board_lines_color, 
        (center[0]-radius, center[1]),
        (center[0]+radius, center[1]),
        width=2
    )
    pygame.draw.line(
        surface,
        board_lines_color, 
        (center[0], center[1]-radius),
        (center[0], center[1]+radius),
        width=2
    )

    pygame.display.flip()


def draw_dart_strike(x_pos, y_pos, dart_color):
    pygame.draw.circle(surface, dart_color, (x_pos, y_pos), dart_radius)
    pygame.display.flip()


pygame.display.set_caption('PART A')
draw_dartboard()

# PART B
pygame.display.set_caption('PART B')
for i in range(10):
    x_dart = random.randrange(x_display_size)
    y_dart = random.randrange(y_display_size)
    distance_from_center = math.hypot(center[0]-x_dart, center[1]-y_dart)
    is_in_circle = distance_from_center <= radius 
    if is_in_circle:
        draw_dart_strike(x_dart, y_dart, 'green')
    else:
        draw_dart_strike(x_dart, y_dart, 'red')

wait_time = 2000
pygame.time.wait(wait_time)

# PART C
box1 = (user_box_margin, user_box_margin, user_box_side, user_box_side)
box2 = (x_display_size - user_box_margin - user_box_side, user_box_margin, user_box_side, user_box_side)

def draw_boxes():
    global box1
    global box2
    pygame.draw.rect(surface, player1_hit_color, box1)
    pygame.draw.rect(surface, player2_hit_color, box2)
    pygame.display.flip()

def is_point_in_box(box_rect, x, y):
    x_box = box_rect[0]
    y_box = box_rect[1]
    width_box = box_rect[2]
    height_box = box_rect[3]
    in_box = x > x_box and x < x_box + width_box and y < y_box + height_box and y > y_box
    return in_box

def input_user_color_selection():
    pygame.display.set_caption('Dartboard - choose a player!')
    stop = False
    while not stop:
        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT
            ):  # Close your program if the user wants to quit.
                raise SystemExit
            elif event.type == pygame.MOUSEBUTTONUP:
                x_mouse = event.pos[0]
                y_mouse = event.pos[1]
                global current_player
                if is_point_in_box(box1, x_mouse, y_mouse):
                    current_player = 1
                    print('User selected Player1')
                    stop = True
                elif is_point_in_box(box2, x_mouse, y_mouse):
                    current_player = 2  
                    print('User selected Player2')
                    stop = True
                else:
                    print('User clicked but did not select yet.')



def shoot_dart(hit_color, miss_color):
    x_dart = random.randrange(x_display_size)
    y_dart = random.randrange(y_display_size)
    distance_from_center = math.hypot(center[0]-x_dart, center[1]-y_dart)
    is_in_circle = distance_from_center <= radius 

    if is_in_circle:
        draw_dart_strike(x_dart, y_dart, hit_color)
    else:
        draw_dart_strike(x_dart, y_dart, miss_color)
    return is_in_circle
     
surface.fill('black')
draw_dartboard()
draw_boxes()
input_user_color_selection()
      
wait_time_between_shots = 500
for i in range(10):
    if shoot_dart(player1_hit_color, player1_miss_color):
        player1_score = player1_score + 1
        print('Player1 Hit:' + str(player1_score))
    else:
        print('Player1 Miss:' + str(player1_score))
    
    pygame.time.wait(wait_time_between_shots)
    
    if shoot_dart(player2_hit_color, player2_miss_color):
        player2_score = player2_score + 1
        print('Player2 Hit:' + str(player2_score))
    else:
        print('Player2 Miss:' + str(player2_score))
        
    pygame.time.wait(wait_time_between_shots) 


print('Player1 score:' + str(player1_score))
print('Player2 score:' + str(player2_score))
print('You selected Player' + str(current_player))
        
if player1_score > player2_score:
    print('Player1 wins!')
    if current_player == 1:
        print('You WON!!!')
    elif current_player ==2:
        print('You Lost!!!')
elif player1_score == player2_score:
    print('It is a Tie!!!')
    
else:
    print('Player2 wins!')
    if current_player == 2:
        print('You WON!!!')
    elif current_player == 1:
        print('You Lost!!!') 
   
        
# END
wait_time = 2000
pygame.time.wait(wait_time)
print('The End!')
surface.fill('black')
