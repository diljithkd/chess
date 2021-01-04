from config import *
from piece import *
class Rook(Piece):
    def find_next_moves(self,board):
        next_pos = []
        a,b = self.curr_pos
        while a<WIDTH and b<HEIGHT and (board[a][b]==EMPTY_CELL or board[a][b]==self):
            if (a!= self.curr_pos[0] or b!=self.curr_pos[1]):
                next_pos.append((a,b))
            a = a+1
        if a<WIDTH and b<HEIGHT and board[a][b].color != self.color:
            next_pos.append((a,b))
        a,b = self.curr_pos
        while a>=0 and b<HEIGHT and (board[a][b]==EMPTY_CELL or board[a][b]==self):
            if (a!= self.curr_pos[0] or b!=self.curr_pos[1]):
                next_pos.append((a,b))
            a = a-1
        if a>=0 and b<HEIGHT and board[a][b].color != self.color:
            next_pos.append((a,b))
        a,b = self.curr_pos
        while a<WIDTH and b<HEIGHT and (board[a][b]==EMPTY_CELL or board[a][b]==self):
            if (a!= self.curr_pos[0] or b!=self.curr_pos[1]):
                next_pos.append((a,b))
            b = b+1
        if a<WIDTH and b<HEIGHT and board[a][b].color != self.color:
            next_pos.append((a,b))
        a,b = self.curr_pos
        while a<WIDTH and b>=0 and (board[a][b]==EMPTY_CELL or board[a][b]==self):
            if (a!= self.curr_pos[0] or b!=self.curr_pos[1]):
                next_pos.append((a,b))
            b = b-1
        if a<WIDTH and b>=0 and board[a][b].color != self.color:
            next_pos.append((a,b))
        return next_pos
