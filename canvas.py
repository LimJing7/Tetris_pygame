import pygame
import tetromino

nCOL=10
nROW=22



class Canvas(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.grid=[[0 for i in range(nCOL)] for j in range(nROW)]
    def nexttet(self):
        """ call the next tetromino"""
        self.current=tetromino.Tetromino()
        r=len(self.current.shape)       #current tet's rows
        c=len(self.current.shape[0])    #current tet's cols
        self.s=[0,nCOL/2-c/2]           #the start of the tetra
        #
    def drop(self):
        """drop current tet"""
        if self.current.check_bot(self.grid, self.s):
            self.s[0]+=1
        else:
            self.add()
            self.nexttet()
        if self.s[0]+len(self.current.shape)<nROW:
            self.s[0]+=1
    def move_left(self):
        """move current left"""
        if self.s[1]>0:
            self.s[1]-=1
    def move_right(self):
        """move current right"""
        if self.s[1]+len(self.current.shape[0])<nCOL:
            self.s[1]+=1
    def add(self):
        """add current to the grid"""
        for i in range(len(self.current.shape)):
            for j in range(len(self.current.shape[i])):
                if self.current.shape[i][j]==1:
                    self.grid[self.s[0]+i][self.s[1]+j]=self.current.number
        # for row in self.grid:
            # print row
    def checkclear(self):
        """check for filled rows"""
        for row in range(self.grid):
            if self.grid[row].count(0)==0:
                self.clear(row)
        self.drop_rows()
    def clear(self, linenumber):
        """clear a particular row"""
        self.grid[linenumber]=[0 for i in range(nCOL)]
    def drop_rows(self):
        """drop rows above filled rows"""
        pass
    
        