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
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    load_images() # only once before the while loop!
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
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