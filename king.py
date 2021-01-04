from config import *
from piece import *
class King(Piece):
    def find_next_moves(self):
        delta = [-1,0,1]
        poss = []
        for i in delta:
            for j in delta:
                if(not(i==0 and j==0) and self.curr_pos[0] + i >=0 and self.curr_pos[0] + i <8 and self.curr_pos[1] + j >=0 and self.curr_pos[1] + j <8):
                    poss.append((self.curr_pos[0] +i , self.curr_pos[1]+j ))
        return poss
