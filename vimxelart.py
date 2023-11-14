import sys
import pygame as pg
from pygame.locals import *

#TODO create a window
#TODO have a MODE status in the corner
#TODO have a pallete
#TODO have a canvas size
#TODO tile system ?
#TODO zoom in and out
#TODO layers?
#TODO Safe image

pg.init()
pg.font.init()

WINDOW_HEIGHT = 200
WINDOW_WIDTH = 320
SCREEN_DIM = (WINDOW_WIDTH,WINDOW_HEIGHT)


# general stuff
FONT = pg.font.Font("./font.ttf", 8)
MODE = "NORMAL"
# poweline bar vars
POWERLINE_HEIGHT = 10
POWERLINE_MODE = MODE
POWERLINE_LOC = (0, WINDOW_HEIGHT-POWERLINE_HEIGHT)
POWERLINE_CUR_COORD = "(0,0)"
POWERLINE_COLOR = (211,211,211)

def draw_cursor(pos:tuple, size:int=1):
    pass

def run_command(command:str):
    if command == "q":
        pg.quit()
        sys.exit()
#I wonder if i can do this shit without classes
#classes are so much bloat and horrible shit
#they are useful for a library but this is something
#thats not supposed to be called
def main():
    pg.init()
    pg.font.init()

    WINDOW_HEIGHT = 200
    WINDOW_WIDTH = 320
    SCREEN_DIM = (WINDOW_WIDTH,WINDOW_HEIGHT)


    # general stuff
    FONT = pg.font.Font("./font.ttf", 8)
    MODE = "NORMAL"
    SCALE = 6
    # poweline bar vars
    POWERLINE_HEIGHT = 10
    POWERLINE_MODE = MODE
    POWERLINE_LOC = (0, WINDOW_HEIGHT-POWERLINE_HEIGHT)
    POWERLINE_CUR_COORD = "(0,0)"
    POWERLINE_COLOR = (211,211,211)
    pwline_surf = pg.Surface((WINDOW_WIDTH,POWERLINE_HEIGHT))

    # canvas area
    # for now just for 16x16 canvas
    CANVAS_DIM = (16,16)
    CANVAS_POS = (20, 20)
    canvas_surf = pg.Surface(CANVAS_DIM)
    # cursor
    CUR_POS_X = 0
    CUR_POS_Y = 0

    # color stuff
    CURRENT_COLOR = (255,255,255)
    TRANSPARENT_COLOR = (0,0,0)

    screen = pg.display.set_mode(SCREEN_DIM, pg.SCALED)
    while 1:
        # render canvas   
        
        canvas_surf = pg.transform.scale(
            canvas_surf,
            tuple(SCALE*x for x in CANVAS_DIM)
        )
        
        screen.blit(canvas_surf, CANVAS_POS)
             
        ## render cursor
        cursor_surf = pg.Surface(canvas_surf.get_size(), pg.SRCALPHA, 32)
        cursor_surf = cursor_surf.convert_alpha()
        cursor_surf.fill((0, 0, 0, 0))
        pg.draw.rect(
            cursor_surf, 
            (255,255,255), 
            (CUR_POS_X*SCALE, CUR_POS_Y*SCALE, 1*SCALE, 1*SCALE),
            1
        )
        screen.blit(cursor_surf, CANVAS_POS)
        
        # normal mode behaviour
        mode_text = FONT.render(POWERLINE_MODE, True, (0,0,0))
        # display powerline
        
        pwline_surf.fill(POWERLINE_COLOR)
        pwline_surf.blit(mode_text, (0,1))
        screen.blit(pwline_surf, POWERLINE_LOC)
        for event in pg.event.get():
            # General behaviour
            if event.type == QUIT:
                # when closing the program
                pg.quit()
                sys.exit()
            # Normal mode behaviour
            if MODE == "NORMAL" and event.type == pg.KEYDOWN:
                if event.unicode == ":":
                    MODE = "TEXT"
                    POWERLINE_MODE = ""
                elif event.key == K_j:
                    if CUR_POS_Y < CANVAS_DIM[0]-1:
                        CUR_POS_Y+=1
                elif event.key == K_k:
                    if CUR_POS_Y > 0:
                        CUR_POS_Y-=1
                elif event.key == K_l:
                    if CUR_POS_X < CANVAS_DIM[1]-1:
                        CUR_POS_X+=1
                elif event.key == K_h:
                    if CUR_POS_X > 0:
                        CUR_POS_X-=1
                elif event.key == K_d:
                    pg.draw.rect(
                        canvas_surf,
                        CURRENT_COLOR,
                        (CUR_POS_X*SCALE, CUR_POS_Y*SCALE, 1*SCALE, 1*SCALE)
                    )
                elif event.key == K_e:
                    pg.draw.rect(
                        canvas_surf,
                        TRANSPARENT_COLOR,
                        (CUR_POS_X*SCALE, CUR_POS_Y*SCALE, 1*SCALE, 1*SCALE)
                    )
            # Text mode behaviour
            if MODE == "TEXT" and event.type == pg.KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(POWERLINE_MODE)>2:
                        POWERLINE_MODE = POWERLINE_MODE[:-1]
                    else:
                        MODE = "NORMAL"
                        POWERLINE_MODE = "NORMAL"
                elif event.key == K_RETURN:
                    run_command(POWERLINE_MODE[1:])
                else:
                    POWERLINE_MODE += event.unicode

            
        pg.display.update()


if __name__=='__main__':
    main()
