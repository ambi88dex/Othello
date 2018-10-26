import numpy as np

class State:
    def __init__(self):
        self.BLACK = 1
        self.WHITE = -1
        self.UNMARKED = 0
        self.PLAYER1 = 1
        self.PLAYER2 = -1
        self.N = 8
        self.state = np.zeros([self.N,self.N],dtype='int')
        self.valid_player_moves = [set(), set()]
        self.row_occupied_indices = [[0, 0] for _ in range(self.N)]
        self.col_occupied_indices = [[0, 0] for _ in range(self.N)]
        self.valid_player_moves = [set(),set()]


    def initialise(self):
        '''
        The user always puts the black key on the board
        '''
        self.state[3][3] = self.WHITE
        self.state[3][4] = self.BLACK 
        self.state[4][3] = self.BLACK 
        self.state[4][4] = self.WHITE
        self.ID = self.PLAYER1
        self.row_occupied_indices[3][0] = 3
        self.row_occupied_indices[3][1] = 4
        self.col_occupied_indices[3][0] = 3
        self.col_occupied_indices[3][1] = 4

    def checkState(self, x, y):
        ret = []
        if self.row_occupied_indices[x][0] == y + 1:
            if self.state[x][self.row_occupied_indices[x][0]] == -self.ID and self.state[x][self.row_occupied_indices[x][1]] == self.ID:
                ret.append(1)
            else:
                ret.append(0)
        elif self.row_occupied_indices[x][1] == y - 1:
            if self.state[x][self.row_occupied_indices[x][1]] == -self.ID and self.state[x][self.row_occupied_indices[x][0]] == self.ID:
                ret.append(-1)
            else:
                ret.append(0)
        return ret

    def vertical_update(self, x, y):
            yy = y - 1
            # upper values get updated in the column
            while yy > -1 and self.state[x][yy] == - self.ID:
                yy -= 1
            if yy != -1 and self.state[x][yy] == self.ID:
                for i in range(yy+1, y):
                    self.state[x][i] = self.ID

            yy = y + 1
            # lower values get updated in the column
            while yy < self.N and self.state[x][yy] == - self.ID:
                yy += 1
            if yy < self.N and self.state[x][yy] == self.ID:
                for i in range(y+1, yy):
                    self.state[x][i] = self.ID

    def horizontal_update(self, x, y,leftmost = True):
            if leftmost:
                    pass

    def play_move(self, x, y):
        idx = (self.ID + 1)//2
        cs = self.checkState(x, y)
        if cs[0] != 0:
            self.state[x][y] = self.ID
            if cs[0] == 1:
                if [x,y] in self.valid_player_moves[idx]:
                    self.valid_player_moves[idx].remove([x, y])
                if y != 0:
                    self.valid_player_moves[1 - idx].add([x,y - 1])
                elif self.row_occupied_indices[x][1] != self.N - 1:
                    self.valid_player_moves[1 - idx].add([x, self.row_occupied_indices[x][1] + 1])
                self.row_occupied_indices[x][0] -= 1
            else:
                if [x,y] in self.valid_player_moves[idx]:
                    self.valid_player_moves[idx].remove([x, y])
                if y != self.N - 1:
                    self.valid_player_moves[1 - idx].add([x, y + 1])
                elif self.row_occupied_indices[x][0] != 0:
                    self.valid_player_moves[1 - idx].add([x, self.row_occupied_indices[x][0] - 1])
                self.row_occupied_indices[x][1] += 1
            self.horizontal_update(x, y)
            self.ID = -self.ID



        if cs[1] !=0:
            self.state[x][y] = self.ID
            self.horizontal_update(x, y)
            self.ID = -self.ID


    def __str__(self):
        ret = ""
        for i in self.state:
            temp = " ".join(list(map(str, i)))
            ret += temp
            ret += "\n"
        return ret
    
    def __repr__(self):
        return self.__str__


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
