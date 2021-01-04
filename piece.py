from config import *
class Piece:
  def __init__(self,color,pos_x,pos_y):
    self.curr_pos = (pos_x,pos_y)
    self.color = color
  def move(self,new_pos_x,new_pos_y):
    self.curr_pos = (new_pos_x,new_pos_y)
    
