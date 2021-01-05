BLACK = 'Black'
WHITE = 'White'
WIDTH = 8
HEIGHT = 8
EMPTY_CELL = 'empty'
NO_ONE_KILLED = -1
NO_LAST_MOVE = [-1,-1,-1,-1]

#GUI
BORDER = 20
CELL_WID = 50
CELL_HEI = 50

#ICONS
ICONS = {
        'Rook':{WHITE:'./icons/white/rook.png', BLACK:'./icons/black/rook.png'},
        'Knight':{WHITE:'./icons/white/knight.png', BLACK:'./icons/black/knight.png'},
        'Bishop':{WHITE:'./icons/white/bishop.png', BLACK:'./icons/black/bishop.png'},
        'King':{WHITE:'./icons/white/king.png', BLACK:'./icons/black/king.png'},
        'Queen':{WHITE:'./icons/white/queen.png', BLACK:'./icons/black/queen.png'},
        'Pawn':{WHITE:'./icons/white/pawn.png', BLACK:'./icons/black/pawn.png'},
        EMPTY_CELL:'./icons/white_bg.png'
        }

KILLED_FILL_ORDER = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)]
KILLED_START = {BLACK:(440, 20), WHITE:(440,320)}   
