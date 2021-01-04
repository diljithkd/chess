from config import *
from piece import *
class Rook(Piece):
    def find_next_moves(self):
        delta = [-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7]
        poss = []
        for i in delta:
            if(self.curr_pos[0] + i >=0 and self.curr_pos[0] + i <8):
                poss.append((self.curr_pos[0]+i,self.curr_pos[1]))
        for i in delta:
            if(self.curr_pos[1] + i >=0 and self.curr_pos[1] + i <8):
                poss.append((self.curr_pos[0],self.curr_pos[1] +i))
        return poss
