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
    # poweline bar vars
    POWERLINE_HEIGHT = 10
    POWERLINE_MODE = MODE
    POWERLINE_LOC = (0, WINDOW_HEIGHT-POWERLINE_HEIGHT)
    POWERLINE_CUR_COORD = "(0,0)"
    POWERLINE_COLOR = (211,211,211)

    screen = pg.display.set_mode(SCREEN_DIM, pg.SCALED)
    while 1:
        # normal mode behaviour
        mode_text = FONT.render(POWERLINE_MODE, True, (0,0,0))
        # display powerline
        pwline_surf = pg.Surface((WINDOW_WIDTH,POWERLINE_HEIGHT))
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
                print(event.unicode, K_COLON)
                if event.unicode == ":":
                    print("pushed colon...")
                    MODE = "TEXT"
                    POWERLINE_MODE = ""
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
