# current gamestate
import pygame as p
import ChessEngine

width = height = 512
dimension = 8 #8x8 board
SQ_SIZE = height // dimension
max_fps = 15 #set for animations

# initialize a global dict of images
images = {}

def loadImages():
    pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 
    'wR', 'wN', 'wB', 'wK', 'wQ','bP', 'wP'],

    for piece in pieces[0]:
        # we can access img with images dictionary now
        images[piece] = p.transform.scale(p.image.load('images/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))


# main driver for game. handlw user input and graphics
def main():
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    clicked = False
    last = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        drawGameState(screen, gs)
        # handle clicks
        if p.mouse.get_pressed()[0] and not clicked:
            last = handleClickOne(gs.board, clicked, False)
            clicked = True
        elif p.mouse.get_pressed()[0] and clicked:
            last = handleClickOne(gs.board, clicked, last)
            clicked = False

        clock.tick(max_fps)
        p.display.flip()


# manages graphics for game state
def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

# draws board sqaures
def drawBoard(screen):
    colors = [p.Color('white'), p.Color('gray')]
    for r in range(dimension):
        for c in range(dimension):
            color = colors[(r + c) % 2]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


# draws pieces based on gs
def drawPieces(screen, board):
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if piece != '--':
                screen.blit(images[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def handleClickOne(board, clicked, last):
    pos = p.mouse.get_pos()
    x = int(pos[0] / SQ_SIZE)
    y = int(pos[1] / SQ_SIZE)
    lastInput = [y, x]
    print(last, clicked)
    if clicked and last:
        board[y][x] = board[last[0]][last[1]]
        board[last[0]][last[1]] = '--'
    
    if board[y][x] == '--':
        return []
    else:
        return lastInput



if __name__ == '__main__':
    main()