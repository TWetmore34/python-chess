# stores info abt current state of game and determines valid moves

class GameState():
    def __init__(self):
        # multi-layer list. each el has two characterss. first is color, second is piece
        # '--' is emply space
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wK', 'wQ', 'wB', 'wN', 'wR']
        ]
        self.whiteToMove = True
        self.moveLog = []