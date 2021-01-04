from config import *
from piece import *
class Knight(Piece):
    def find_next_moves(self, board):
        x_offset = [-1,-2,-2,-1,1,2,2,1]
        y_offset = [-2,-1,1,2,2,1,-1,-2]
        next_pos = []
        for i,j in zip(x_offset, y_offset):
            temp_i = self.curr_pos[0]-i
            temp_j = self.curr_pos[1]-j
            if temp_i < HEIGHT and temp_i >= 0 and temp_j < WIDTH and temp_j >= 0:
                if board[temp_i][temp_j]==EMPTY_CELL or (board[temp_i][temp_j]!=EMPTY_CELL and board[temp_i][temp_j].color != self.color):
                    next_pos.append((temp_i, temp_j))
        return next_pos
