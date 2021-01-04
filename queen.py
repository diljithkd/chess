from config import *
from piece import *
class Queen(Piece):
    def find_next_moves(self):
        delta = [-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]
        poss = []
        for i in delta:
            for j in delta:
                if(not(i==0 and j==0) and (i==j or i+j == 0 or i==0 or j==0) and self.curr_pos[0] + i >=0 and self.curr_pos[0] + i <8 and self.curr_pos[1] + j >=0 and self.curr_pos[1] + j <8):
                    poss.append((self.curr_pos[0] +i , self.curr_pos[1]+j ))            
        return poss
