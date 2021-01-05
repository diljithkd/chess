from config import *
from piece import *
class Pawn(Piece):
    def find_next_moves(self, board):
        next_pos = []
        a,b = self.curr_pos
        if self.color == BLACK:
            if a==0:
                return next_pos
            else:
                if board[a-1][b]==EMPTY_CELL:
                    next_pos.append((a-1,b))
                if b > 0 and board[a-1][b-1] != EMPTY_CELL and board[a-1][b-1].color != self.color:
                    next_pos.append((a-1,b-1))
                if b < HEIGHT-1 and board[a-1][b+1] != EMPTY_CELL and board[a-1][b+1].color != self.color:
                    next_pos.append((a-1,b+1))
            if a==6 and board[4][b]==EMPTY_CELL:
                next_pos.append((4,b))
        else:
            if a==HEIGHT-1:
                return next_pos
            else:
                if board[a+1][b]==EMPTY_CELL:
                    next_pos.append((a+1,b))
                if b > 0 and board[a+1][b-1] != EMPTY_CELL and board[a+1][b-1].color != self.color:
                    next_pos.append((a+1,b-1))
                if b < HEIGHT-1 and board[a+1][b+1] != EMPTY_CELL and board[a+1][b+1].color != self.color:
                    next_pos.append((a+1,b+1))
            if a==1and board[3][b]==EMPTY_CELL:
                next_pos.append((3,b))
        return next_pos
