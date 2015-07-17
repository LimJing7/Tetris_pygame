import pygame
import tetromino

nCOL=10
nROW=22



class Canvas(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.grid=[[0 for i in range(nCOL)] for j in range(nROW)]
        self.colors=[(0,0,0)]
        self.rCleared = 0
        self.score = 0
    def nexttet(self):
        """ call the next tetromino"""
        self.current=tetromino.Tetromino()
        r=len(self.current.shape)       #current tet's rows
        c=len(self.current.shape[0])    #current tet's cols
        self.s=[0,nCOL/2-c/2]           #the start of the tetra
    def drop(self):
        """drop current tet"""
        if self.current.check_bot(self.grid, self.s):
            self.s[0]+=1
        else:
            self.add()
            self.nexttet()
    def move_left(self):
        """move current left"""
        if self.current.check_left(self.grid, self.s):
            self.s[1]-=1
    def move_right(self):
        """move current right"""
        if self.current.check_right(self.grid, self.s):
            self.s[1]+=1
    def drop_cur(self):
        """drop current block all the way"""
        while self.current.check_bot(self.grid, self.s):
            self.s[0]+=1
    def add(self):
        """add current to the grid"""
        for i in range(len(self.current.shape)):
            for j in range(len(self.current.shape[i])):
                if self.current.shape[i][j]==1:
                    self.grid[self.s[0]+i][self.s[1]+j]=self.current.number
        self.colors.append(self.current.color)
        # for row in self.grid:
            # print row
    def checkclear(self):
        """check for filled rows"""
        for row in range(len(self.grid)):
            if self.grid[row].count(0)==0:
                self.clear(row)
                self.rCleared+=1
                self.score += self.rCleared
    def clear(self, linenumber):
        """clear a particular row"""
        self.grid.pop(linenumber)
        self.grid = [[0 for i in range(nCOL)]] + self.grid
    
    def lose(self):
        """check for game over condition"""
        if self.grid[0].count(0)!=nCOL:
            return True