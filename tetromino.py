import random
import pygame
import canvas


class Tetromino(pygame.sprite.Sprite):
    shape_names=['i','o','t','l','j','s','z']
    colors=['tur','yellow','purple','blue','brown','green','red']
    shapes=[[[1,1,1,1]],
            [[1,1],
             [1,1]],
            [[0,1,0],
             [1,1,1]],
            [[1,1,1],
             [1,0,0]],
            [[1,1,1],
             [0,0,1]],
            [[0,1,1],
             [1,1,0]],
            [[1,1,0],
             [0,1,1]]]
    next=random.randint(0,6)
    number=0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.shape_name=Tetromino.shape_names[Tetromino.next]
        self.color=Tetromino.colors[Tetromino.next]
        self.shape=Tetromino.shapes[Tetromino.next]
        self.number=Tetromino.number
        Tetromino.number+=1
        Tetromino.next=random.randint(0,6)
    def rotate_clock(self):
        self.shape=zip(*self.shape[::-1])
    def rotate_anti(self):
        self.shape=(zip(*self.shape)[::-1])
    def check_bot(self, can_grid, start):
        i,j=*start
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                #can_grid[i,j]
    def __str__(self):
        return self.shape_name
	
def main():
    for i in range(10):
        tetra=Tetromino()
        print str(tetra) +":" + str(tetra.shape)

if __name__=="__main__":
    main()