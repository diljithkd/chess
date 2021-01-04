from config import *
from piece import *
class King(Piece):
    def find_next_moves(self, board):
        x_offset = [0,-1,-1,-1,0,1,1,1]
        y_offset = [-1,-1,0,1,1,1,0,-1]
        all_pos = []
        for i,j in zip(x_offset, y_offset):
            i1 = self.curr_pos[0] + i
            j1 = self.curr_pos[1] + j
            if i1>=0 and i1<HEIGHT and j1>=0 and j1<WIDTH and (board[i1][j1]==EMPTY_CELL or (board[i1][j1]!=EMPTY_CELL and board[i1][j1].color!=self.color)):
                all_pos.append((i1,j1))
        return all_pos
