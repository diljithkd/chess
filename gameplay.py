from config import *
from board import *
from tkinter import *  
from PIL import ImageTk,Image
import cv2
import itertools

    
class Game:
  def __init__(self):
    self.board = Board()
    self.board.show_board()
    self.curr_turn = WHITE
    self.icon_selected = (-1,-1)
    self.rect_boxs = []
    self.victory = None
    self.check = None
    self.root = Tk()
    self.canvas = Canvas(self.root, width = 860, height = 440)  
    self.canvas.pack()
    self.canvas.bind("<Button-1>", self.motion)
    self.draw_canvas()

  def draw_border(self,a,b,c,d,piece):
    #self.canvas.delete(ALL)
    for i in self.rect_boxs:
      self.canvas.delete(i)
    t = self.canvas.create_rectangle(a,b,c,d, fill='gray', outline='red', stipple="gray50")
    self.rect_boxs.append(t)
    postns = piece.find_next_moves(self.board.board)
    for i in postns:
      x,y = i
      t = self.canvas.create_rectangle(BORDER+y*CELL_WID, BORDER+x*CELL_HEI, BORDER+y*CELL_WID+CELL_WID, BORDER+x*CELL_HEI+CELL_HEI, fill='gray', outline='red', stipple="gray50")
      self.rect_boxs.append(t)
    self.canvas.mainloop()

  def motion(self, event):
    x, y = event.x-BORDER, event.y-BORDER
    #print(x,y)
    if x<=0 or x>=8*CELL_WID or y<=0 or y>=8*CELL_WID:
      #print('outside the range')
      return
    x,y = int(y/CELL_WID), int(x/CELL_HEI)
    #print(self.board.board[x][y])
    if self.board.board[x][y] == EMPTY_CELL or (self.board.board[x][y] != EMPTY_CELL and self.board.board[x][y].color != self.curr_turn):
      if self.icon_selected != (-1,-1):
        a,b = self.icon_selected
        self.icon_selected = (-1,-1)
        flag, msg = self.board.move(a,b,x,y)
        if flag:
          self.curr_turn = self.flip_color(self.curr_turn)
          if self.board.is_check_mate(self.curr_turn):
                self.victory = self.flip_color(self.curr_turn)
          elif self.board.is_checked(self.curr_turn):
            self.check = 'Check!!'
        else:
          #print('NOT MOVED', msg)
          pass
    elif self.board.board[x][y] != EMPTY_CELL and self.board.board[x][y].color == self.curr_turn:
      #print('icon selected')
      self.icon_selected = (x,y)
      #print(self.icon_selected)
      self.draw_border(BORDER+y*CELL_WID, BORDER+x*CELL_HEI, BORDER+y*CELL_WID+CELL_WID, BORDER+x*CELL_HEI+CELL_HEI, self.board.board[x][y])
    self.draw_canvas()
      
  def draw_canvas(self):
    board = self.board.board
    img = ImageTk.PhotoImage(Image.open("./icons/black/rook.png"))
    images = []
    self.canvas.delete(ALL)
    self.canvas.create_text(2*BORDER+8*CELL_WID+4*CELL_WID,BORDER+2*CELL_WID+int(CELL_HEI/2),fill="darkblue",font="Arial 15 ",
                        text="{}'s Turn!".format(self.curr_turn))
    for i in range(8):
      for j in range(8):
        if board[i][j] != EMPTY_CELL:
          img = ImageTk.PhotoImage(Image.open(ICONS[type(board[i][j]).__name__][board[i][j].color]))
        else:
          img = ImageTk.PhotoImage(Image.open(ICONS[EMPTY_CELL]))
        self.canvas.create_image(BORDER+j*CELL_WID, BORDER+i*CELL_HEI, anchor=NW, image=img)
        images.append(img)
    for i in range(9):
      self.canvas.create_line(20, BORDER+i*CELL_WID, 420, BORDER+i*CELL_WID)
      self.canvas.create_line(BORDER+i*CELL_WID, 20, BORDER+i*CELL_WID, 420)
    curr_ind = {BLACK:0, WHITE:0}
    for i in self.board.killed_pieces:
      img = ImageTk.PhotoImage(Image.open(ICONS[type(i).__name__][i.color]))
      images.append(img)
      pos = KILLED_FILL_ORDER[curr_ind[i.color]]
      curr_ind[i.color] = curr_ind[i.color] + 1
      x1,y1 = KILLED_START[i.color]
      y2,x2 = pos
      #print(pos, KILLED_START[i.color],x2+x1*CELL_WID,y2+y1*CELL_WID)
      self.canvas.create_image(x1+x2*CELL_WID,y1+y2*CELL_WID,anchor=NW, image=img)
    if self.victory != None:
      self.canvas.create_text(2*BORDER+8*CELL_WID+4*CELL_WID,BORDER+3*CELL_WID+int(CELL_HEI/2),fill="darkblue",font="Arial 15 ",
                        text="{} Won!!!".format(self.victory))
      self.canvas.create_rectangle(0,0,440,440,fill='red', outline='red', stipple="gray50")
    elif self.check != None:
      self.canvas.create_text(2*BORDER+8*CELL_WID+4*CELL_WID,BORDER+3*CELL_WID+int(CELL_HEI/2),fill="darkblue",font="Arial 15 ",
                        text="Check!!!")
      self.check = None
      x,y = self.board.king[self.curr_turn].curr_pos
      self.canvas.create_rectangle(BORDER+y*CELL_WID, BORDER+x*CELL_HEI, BORDER+y*CELL_WID+CELL_WID, BORDER+x*CELL_HEI+CELL_HEI, fill='gray', outline='red', stipple="gray50")
    self.root.mainloop()

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
    self.draw_canvas()

g = Game()
g.start_game()
    
