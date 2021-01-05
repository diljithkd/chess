from config import *
from bishop import *
from king import *
from knight import *
from pawn import *
from queen import *
from rook import *
import copy
class Board:
  def __init__(self):
    self.board = [[EMPTY_CELL]*HEIGHT for _ in range(WIDTH)]
    self.board_vis = [[EMPTY_CELL]*HEIGHT for _ in range(WIDTH)]
    self.killed_pieces = []
    self.last_move = NO_LAST_MOVE
    self.last_move_killed = NO_ONE_KILLED
    self.king = {WHITE:King(WHITE,0,3),BLACK:King(BLACK,7,3)}
    self.opponent = {WHITE:BLACK, BLACK:WHITE}
    self.pieces = [Rook(WHITE,0,0),
                   Knight(WHITE,0,1),
                   Bishop(WHITE,0,2),
                   self.king[WHITE],
                   Queen(WHITE,0,4),
                   Bishop(WHITE,0,5),
                   Knight(WHITE,0,6),
                   Rook(WHITE,0,7),
                   Pawn(WHITE,1,0),
                   Pawn(WHITE,1,1),
                   Pawn(WHITE,1,2),
                   Pawn(WHITE,1,3),
                   Pawn(WHITE,1,4),
                   Pawn(WHITE,1,5),
                   Pawn(WHITE,1,6),
                   Pawn(WHITE,1,7),
                   Rook(BLACK,7,0),
                   Knight(BLACK,7,1),
                   Bishop(BLACK,7,2),
                   self.king[BLACK],
                   Queen(BLACK,7,4),
                   Bishop(BLACK,7,5),
                   Knight(BLACK,7,6),
                   Rook(BLACK,7,7),
                   Pawn(BLACK,6,0),
                   Pawn(BLACK,6,1),
                   Pawn(BLACK,6,2),
                   Pawn(BLACK,6,3),
                   Pawn(BLACK,6,4),
                   Pawn(BLACK,6,5),
                   Pawn(BLACK,6,6),
                   Pawn(BLACK,6,7)]

  def place_pieces(self):
    self.board = [[EMPTY_CELL]*HEIGHT for _ in range(WIDTH)]
    self.board_vis = [[EMPTY_CELL]*HEIGHT for _ in range(WIDTH)]
    for i in self.pieces:
      a,b = i.curr_pos
      self.board[a][b] = i
      self.board_vis[a][b] = i.color

  def undo_last_move(self):
    if self.last_move_killed != NO_ONE_KILLED:
      self.killed_pieces.remove(self.last_move_killed)
      self.pieces.append(self.last_move_killed)
    if self.last_move != NO_LAST_MOVE:
      a,b,c,d = self.last_move
      self.move(c,d,a,b)
    else:
      #print('No Undo available')
      pass
    self.last_move = NO_LAST_MOVE
    self.last_move_killed = NO_ONE_KILLED

  def kill_piece(self, piece):
    if piece in self.pieces:
      self.pieces.remove(piece)
      self.killed_pieces.append(piece)

  def revive_piece(self, piece):
    if piece in self.killed_pieces:
      self.killed_pieces.remove(piece)
      self.pieces.append(piece)

  def show_board(self):
    self.place_pieces()
    for i in self.board_vis:
      print(i)
    print('{} pieces alive and {} pieces dead'.format(len(self.pieces), len(self.killed_pieces)))
    print('Last Move from ({},{}) to ({},{}) and it killed {}'.format(self.last_move[0],self.last_move[1],self.last_move[2],self.last_move[3],self.last_move_killed))
    print('--------------------------------------------------------')

  def is_checked(self, color):
    #print(self.king[color].curr_pos)
    for piece in self.pieces:
        if piece.color != color:
            postns = piece.find_next_moves(self.board)
            #print(postns, self.king[color].curr_pos)
            if self.king[color].curr_pos in postns:
                return True
    return False

  def is_check_mate(self, color):
    for piece in self.pieces:
      if piece.color == color:
        postns = piece.find_next_moves(self.board)
        if postns != []:
          for i in postns:
            (src_x, src_y),(dest_x,dest_y) = piece.curr_pos, i
            kill_flag = False
            if self.board[dest_x][dest_y] != EMPTY_CELL and self.board[dest_x][dest_y].color != piece.color:
              #print('killing', self.board[dest_x][dest_y])
              self.kill_piece(self.board[dest_x][dest_y])
              kill_flag = self.board[dest_x][dest_y]
            piece.move(dest_x, dest_y)
            self.place_pieces()
            if self.is_checked(piece.color) == False:
              piece.move(src_x, src_y)
              self.place_pieces()
              if kill_flag:
                #print('reviving', kill_flag)
                self.revive_piece(kill_flag)
                #self.place_pieces()
                self.show_board()
              #print(src_x, src_y,dest_x,dest_y)
              return False
            else:
              piece.move(src_x, src_y)
              self.place_pieces()
              if kill_flag:
                self.revive_piece(kill_flag)
                #self.place_pieces()
    return True
                

  def move(self, src_x, src_y, dest_x, dest_y):
    #print('Move piece from ({},{}) to ({},{})'.format(src_x, src_y, dest_x, dest_y))
    piece = self.board[src_x][src_y]
    postns = piece.find_next_moves(self.board)
    if self.king[self.opponent[piece.color]].curr_pos in postns:
      postns.remove(self.king[self.opponent[piece.color]].curr_pos)
    #print('Possible Moves :', postns)
    prev_move = self.last_move
    prev_kill = self.last_move_killed
    kill_flag = False
    if (dest_x, dest_y) in postns:
      if self.board[dest_x][dest_y] != EMPTY_CELL and self.board[dest_x][dest_y].color != piece.color:
        self.last_move_killed = self.board[dest_x][dest_y]
        self.kill_piece(self.board[dest_x][dest_y])
        kill_flag = self.board[dest_x][dest_y]
      else:
        self.last_move_killed = NO_ONE_KILLED
      piece.move(dest_x, dest_y)
      self.place_pieces()
      self.last_move = [src_x, src_y, dest_x, dest_y]
      if self.is_checked(piece.color):
        #print('This move is not possible beacuse king is checked')
        self.last_move = prev_move
        self.last_move_killed = prev_kill
        piece.move(src_x, src_y)
        self.place_pieces()
        if kill_flag:
          self.revive_piece(kill_flag)
          #self.place_pieces()
        return False,'King under check'
    else:
      pass
      #print('move not possible')
      return False,'Not a valid move'
    self.show_board()
    return True,''
