import random
import pygame
import canvas

TUR = (175, 238, 238)
YEL = (255, 255,   0)
PUR = (153, 102, 204)
BLU = (  0,   0, 255)
BRO = (150,  75,   0)
GRN = (  0, 255,   0)
RED = (255,   0,   0)

class Tetromino(pygame.sprite.Sprite):
    shape_names=['i','o','t','l','j','s','z']
    colors=[TUR, YEL, PUR, BLU, BRO, GRN, RED]
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
    def rotate_clock(self, can_grid, start):
        nShape=zip(*self.shape[::-1])
        if self.check_overlap(can_grid, start, nShape):
            self.shape=nShape
    def rotate_anti(self, can_grid, start):
        nShape=(zip(*self.shape)[::-1])
        if self.check_overlap(can_grid, start, nShape):
            self.shape=nShape
    def check_bot(self, can_grid, start):
        """
        returns true if tetromino has not hit anything
        """
        i,j=start
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                if self.shape[row][col]==1:
                    try:
                        if self.shape[row+1][col] == 0:
                            try:
                                if can_grid[i+row+1][j+col]!=0:
                                    return False
                            except IndexError:
                                return False
                    except IndexError:
                        try:
                            if can_grid[i+row+1][j+col]!=0:
                                return False
                        except IndexError:
                            return False
        return True
    def check_left(self, can_grid, start):
        """
        returns true if tetromino has not hit anything
        """
        i,j=start
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                if self.shape[row][col]==1:
                    if col-1 < 0:
                        if j+col-1 <0:
                            return False
                        elif can_grid[i+row][j+col-1]!=0:
                                return False
                    else:
                        if self.shape[row][col-1] == 0:
                            if j+col-1 <0:
                                return False
                            elif can_grid[i+row][j+col-1]!=0:
                                    return False
        return True
    def check_right(self, can_grid, start):
        """
        returns true if tetromino has not hit anything
        """
        i,j=start
        for row in range(len(self.shape)):
            for col in range(len(self.shape[row])):
                if self.shape[row][col]==1:
                    try:
                        if self.shape[row][col+1] == 0:
                            try:
                                if can_grid[i+row][j+col+1]!=0:
                                    return False
                            except IndexError:
                                return False
                    except IndexError:
                        try:
                            if can_grid[i+row][j+col+1]!=0:
                                return False
                        except IndexError:
                            return False
        return True
    def check_overlap(self, can_grid, start, shape):
        """
        returns true if tetromino has not hit anything
        """
        i,j=start
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col]==1:
                    try:
                        if can_grid[i+row][j+col]!=0:
                            return False
                    except IndexError:
                        return False
        return True
    def __str__(self):
        return self.shape_name
	
def main():
    for i in range(10):
        tetra=Tetromino()
        print str(tetra) +":" + str(tetra.shape)

if __name__=="__main__":
    main()