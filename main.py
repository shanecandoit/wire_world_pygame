import pygame
import pygame as pg

# consts
black  = (0, 0, 0)
blue   = (0, 0, 255)
red    = (255, 0, 0)
yellow = (255, 255, 0)
grey   = (128, 128, 128)
white  = (255, 255, 255)
empty = black
head  = blue
tail  = red
wire  = yellow

scale = 10

# setup
ok = pygame.init()
if not ok:
    print("Pygame failed to initialize")
    exit()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("wire world")

more = True

cells = {}

cells[ (0,0) ] = yellow

mouse_drag = False

while more:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            more = False

        # keyboard
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                more = False
        
        # mouse
        if event.type == pg.MOUSEBUTTONDOWN:
            buttons = pg.mouse.get_pressed()
            #print('mousedown', buttons)
            if buttons[0]:
                x, y = pg.mouse.get_pos()
                x = x // scale
                y = y // scale
                cells[ (x,y) ] = yellow
                mouse_drag = True

        elif event.type == pg.MOUSEBUTTONUP:
            buttons = pg.mouse.get_pressed()
            print('mouseup', buttons)

            if not buttons[0]:
                mouse_drag = False
            
        elif event.type == pg.MOUSEMOTION:
            if mouse_drag:
                x, y = pg.mouse.get_pos()
                x = x // scale
                y = y // scale
                cells[ (x,y) ] = yellow

    # clear screen
    screen.fill(black)

    # draw ui
    pg.draw.rect(screen, grey, (0, 600-100, 800, 600))


    # next turns cells
    # double buffer
    ncells = {}

    for pos in cells:
        col = cells[pos]
        # print('cell', pos, col)
        if col == wire:
            pg.draw.rect(screen, 
                        col, 
                        (pos[0]*scale, pos[1]*scale, scale, scale))
        
    # Draw
    pg.display.flip()
