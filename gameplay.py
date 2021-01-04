from config import *
from board import *
class Game:
  def __init__(self):
    self.board = Board()
    self.board.show_board()

  def flip_color(self, color):
    if color == WHITE:
      return BLACK
    else:
      return WHITE

  def within_dim(self,a,b):
    if a>=0 and a<WIDTH and b>=0 and b<HEIGHT:
      return True
    else:
      return False

  def start_game(self):
    curr_color = WHITE
    temp_color = WHITE
    while True:
      if self.board.is_checked(curr_color):
        print('checking check mate')
        if self.board.is_check_mate(curr_color):
            print('check mate')
            break
      while temp_color == curr_color:
        print('Move by {}'.format(curr_color))
        a,b,c,d = [int(x) for x in input()]
        print(a,b,c,d)
        if a<0 or a>=WIDTH or b<0 or b>=HEIGHT:
          continue
        if self.within_dim(a,b) and self.board.board[a][b] == EMPTY_CELL:
          continue
        if self.within_dim(a,b) and self.board.board[a][b].color != temp_color:
          continue
        if self.within_dim(a,b) and self.board.board[a][b].color == temp_color:
          if self.board.move(a,b,c,d)==True:
            temp_color = self.flip_color(temp_color)
      curr_color = temp_color

g = Game()
g.start_game()
    
