import os, pygame
from pygame.locals import *
from pygame.compat import geterror
import tetromino
import canvas

HUD_COLOR=(185,185,185)
HUD_SIDE=50
HUD_BOTTOM=40
HEIGHT=660+HUD_BOTTOM
WIDTH=300+2*HUD_SIDE
  
def main():
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('Tetris')
    pygame.mouse.set_visible(0)
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    
    #draw HUD
    pygame.draw.rect(background, HUD_COLOR , [0,0,HUD_SIDE,HEIGHT])
    pygame.draw.rect(background, HUD_COLOR , [WIDTH-HUD_SIDE,0,HUD_SIDE,HEIGHT])
    pygame.draw.rect(background, HUD_COLOR , [0,HEIGHT-HUD_BOTTOM,WIDTH,HUD_BOTTOM])
    
    clock = pygame.time.Clock()
    tetro=tetromino.Tetromino()
    pygame.sprite.RenderPlain((tetro))
    
    #draw canvas
    can=canvas.Canvas()
    can.nexttet()
    def drawcur():
        for i in range(len(can.current.shape)):
            for j in range(len(can.current.shape[i])):
                if can.current.shape[i][j]==1:
                    pygame.draw.rect(background, can.current.color, [(j+can.s[1])*30+HUD_SIDE,(i+can.s[0])*30,30,30])
                    
    def drawgrid():
        for i in range(len(can.grid)):
            for j in range(len(can.grid[i])):
                if can.grid[i][j]!=0:
                    pygame.draw.rect(background, can.colors[can.grid[i][j]], [j*30+HUD_SIDE,i*30,30,30])
                else:
                    pygame.draw.rect(background, (0,0,0), [j*30+HUD_SIDE,i*30,30,30])
                
    def drawScore():
        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render(str(can.score), 1, (255, 255, 255))
            textpos = text.get_rect(centerx=background.get_width()/2)
            background.blit(text, textpos)
    
    going = True
    
    ck=0
    to_drop = False
    end = False
    
    while going:
        clock.tick(60)
        ck+=1

        #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    going = False
                elif event.key == K_RIGHT:
                    can.move_right()
                elif event.key == K_LEFT:
                    can.move_left()
                elif event.key == K_UP:
                    can.current.rotate_clock(can.grid, can.s)
                elif event.key == K_SPACE:
                    can.drop_cur()
        
        if (ck+1)%20==0:
            to_drop = True
        
        if ck%20==0:
            if to_drop:
                can.drop()
                can.checkclear()
                to_drop=False
        
        #allsprites.update()

        #Draw Everything
        screen.blit(background, (0, 0))
        drawgrid()
        drawcur()
        drawScore()
        if can.lose():
            going = False
        #allsprites.draw(screen)
        pygame.display.flip()
    
    while not end:
        for event in pygame.event.get():
            if event.type == QUIT:
                end = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    end = True
    
    pygame.quit()
    
if __name__=="__main__":
    main()