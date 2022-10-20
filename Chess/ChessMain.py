"""
This is our main driver file. It will be responsible for handling user input and displaying the current GameState object.
"""

import pygame as p
import ChessEngine

p.init() # initialise the game
WIDTH = HEIGHT = 512 # 400 is another option (consider getting higher res images later)
DIMENSION = 8 # dimensions 8x8
SQ_SIZE = HEIGHT // DIMENSION # square size
MAX_FPS = 30 # for animations at the end
IMAGES = {}

'''
We want to just load in the images one time - its an expensive operation.
Initialize a global dictionary of images. This will be called exactly once in the main
'''

def load_images():
    pieces = ["wP","wR","wN","wB","wK","wQ","bP","bR","bN","bB","bK","bQ"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("Chess/Assests/" + piece + ".png"), (SQ_SIZE,SQ_SIZE))
    # now we can access an IMAGE by calling "IMAGES['wp']".

'''
The main driver for our code. This will handle user input and updating graphics.
'''

def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    #screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    valid_moves = gs.get_valid_moves()
    move_made = False # flag variable for when a move is made (that's when we update valid_moves, rather than every frame)
    load_images() # only once before the while loop!
    running = True
    sq_selected = () # no square is selected, keep tack of the last click of the user (tuple: row,col)
    player_clicks = [] # keep track of player clicks (two tuples: e.g. [(6,5),(4,4)])

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

            # mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # (x,y) location of mouse
                col = location[0]//SQ_SIZE 
                row = location[1]//SQ_SIZE
                if sq_selected == (row,col): # user clicked same square twice
                    sq_selected = () # deselect
                    player_clicks = [] # clear player clicks
                else:
                    sq_selected = (row,col)
                    player_clicks.append(sq_selected) # append for both 1st and 2nd click
                if len(player_clicks) == 2: # after second click
                    move = ChessEngine.Move(player_clicks[0],player_clicks[1],gs.board)
                    print(move.get_chess_notation())
                    if move in valid_moves:
                        gs.make_move(move)
                        move_made = True # changing the flag so we can update valid_moves list
                    sq_selected = () # reset user clicks
                    player_clicks = []

            # key handler
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: # z is our undo key
                    gs.undo_move()
                    move_made = True

        if move_made:
            validMoves = gs.get_valid_moves() # updating the valid_moves list
            move_made = False  # resetting the flag back to false
        draw_game_state(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Responsible for all the graphics within a current game state.
'''
def draw_game_state(screen,gs):
    draw_board(screen) # draw squares on the board
    # add in piece highlighting or move suggestions here
    draw_pieces(screen,gs.board) # draw pieces on top of those squares

'''
Draw the squares on the board.
'''
def draw_board(screen):
    colors = [p.Color('white'),p.Color('light blue')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))
            

'''
Draw the pieces on the board using the current GameState.board
'''
def draw_pieces(screen,board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": #not empty
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))


if __name__ == "__main__":
    main()