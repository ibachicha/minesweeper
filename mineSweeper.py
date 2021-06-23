import random
import time


def createMineSweeperBoard(boardSize, mines):
    """
    Generates a mineSweeper board with all 0 values.
    """
    MS_Board = [[0 for row in range(boardSize)] for col in range(boardSize)]
    return addMines(MS_Board, boardSize, mines)


def createPlayerBoard(boardSize):
    """
    Generate blank player board on 8x8 grid (or grid according to boardSize).
    """
    player_Board = [['-' for row in range(boardSize)] for column in range(boardSize)]
    return player_Board


def addMines(MS_Board, boardSize, mines):
    """
    Creates random mines and adds them to the mineSweeper board. Adds a value of 1
    to all of the mine's neighbors. '*' denotes a mine.
    """
    for num in range(mines):
        row = random.randint(0, boardSize - 1)
        col = random.randint(0, boardSize - 1)
        MS_Board[row][col] = '*'

        # Right Side Neighbor Squares
        if (1 <= row <= boardSize - 1) and (0 <= col <= boardSize - 2) and MS_Board[row - 1][col + 1] != '*':
            MS_Board[row - 1][col + 1] += 1
        if (0 <= row <= boardSize - 1) and (0 <= col <= boardSize - 2) and MS_Board[row][col + 1] != '*':
            MS_Board[row][col + 1] += 1
        if (0 <= row <= boardSize - 2) and (0 <= col <= boardSize - 2) and MS_Board[row + 1][col + 1] != '*':
            MS_Board[row + 1][col + 1] += 1

        # Left Side Neighbor Squares
        if (1 <= row <= boardSize - 1) and (1 <= col <= boardSize - 1) and MS_Board[row - 1][col - 1] != '*':
            MS_Board[row - 1][col - 1] += 1
        if (0 <= row <= boardSize - 1) and (1 <= col <= boardSize - 1) and MS_Board[row][col - 1] != '*':
            MS_Board[row][col - 1] += 1
        if (0 <= row <= boardSize - 2) and (1 <= col <= boardSize - 1) and MS_Board[row + 1][col - 1] != '*':
            MS_Board[row + 1][col - 1] += 1

        # Top & Bottom Center Neighbor Squares
        if (1 <= row <= boardSize - 1) and (0 <= col <= boardSize - 1) and MS_Board[row - 1][col] != '*':
            MS_Board[row - 1][col] += 1
        if (0 <= row <= boardSize - 2) and (0 <= col <= boardSize - 1) and MS_Board[row + 1][col] != '*':
            MS_Board[row + 1][col] += 1

    return MS_Board


def check4_win(coveredSquares, mines):
    """
    Check if puzzle is solved. A solved puzzle is
    defined by having the amount of covered squares left equal to the
    amount of mines in the puzzle. This indicates only mines are uncovered.
    """
    if coveredSquares != mines:
        return False
    return True


def gameLost(mineSweeperBoard, score, startGameTimer):
    """
    Prints results of game to screen when it's a lose.
    """
    print('')
    print('')
    displayBoard(mineSweeperBoard)
    print('')
    print('BOOM!!!')
    print('You hit a mine. Game Over!')
    print('')
    print('Final score: ', score)
    endGameTimer = time.time()
    finalTimer = endGameTimer - startGameTimer
    gameTime = convertSec(finalTimer)
    print('Your game lasted for', *gameTime, sep=' ')


def gameWon(playerBoard, score, startGameTimer):
    """
    Prints results of game to screen when it's a win.
    """
    print('')
    print('')
    displayBoard(playerBoard)
    print('')
    print('Minesweeper Solved!')
    print('')
    print('Final score: ', score)
    endGameTimer = time.time()
    finalTimer = endGameTimer - startGameTimer
    gameTime = convertSec(finalTimer)
    print('Your game lasted for', *gameTime, sep=' ')


def convertSec(sec):
    """
    Convert game clock time from seconds to
    seconds, minutes, hours
    """
    sec = sec % (24 * 3600)
    hour = (str(sec // 3600)[:-2])  # format to remove decimal places

    sec %= 3600
    minutes = (str(sec // 60)[:-2])

    sec %= 60
    seconds = round(sec, 2)  # round to 2 decimal places

    return hour, 'hours', minutes, 'minutes', 'and', seconds, 'seconds.'


def mineSweeper():
    """
    Creates an instance of the game.
    """

    startGameTimer = time.time()
    # Note -- board size cannot be > 9. Board formatting will be off if it is
    boardSize = 8
    mines = 10
    score = 0
    coveredSquare_Counter = boardSize * boardSize
    # Gives board functions their variables.
    mineSweeperBoard = createMineSweeperBoard(boardSize, mines)
    playerBoard = createPlayerBoard(boardSize)
    displayBoard(playerBoard)
    while True:
        try:
            if check4_win(coveredSquare_Counter, mines) == False:
                print('Current Score: ', score)
                print('')
                print('Enter the row & column you wish to select (1-' + str(boardSize) + ')')
                inputRow = input('Select Row: ')
                inputCol = input('Select Column: ')
                row = int(inputRow)
                col = int(inputCol)
                if 0 < row < (boardSize + 1) and 0 < col < (boardSize + 1) or row is None or col is None:
                    row -= 1
                    col -= 1
                    if mineSweeperBoard[col][row] == '*':  # Game is lost
                        gameLost(mineSweeperBoard, score, startGameTimer)
                        return False
                    elif playerBoard[col][row] != '-':  # Square isn't open
                        print('That square has already been chosen. Please choose another!')
                    else:
                        coveredSquare_Counter -= 1 # place it
                        playerBoard[col][row] = mineSweeperBoard[col][row]
                        displayBoard(playerBoard)
                        score += 1
                else:
                    print('Incorrect values. Please insure the row & column are between 1-' + str(boardSize))
            else:
                gameWon(playerBoard, score, startGameTimer)  # Game is won
                return False
        except ValueError:
            print('Looks like you missed an input. Please try again!')


def displayBoard(board):
    """
    Displays board with proper formatting.
    """
    length = (len(board))
    print('  ' + ('   '.join(str(a) for a in range(1, length + 1)) + '  '))
    print(' ' + (('--' * length) * 2))
    count = 0
    for row in board:
        count += 1
        print('| ' + (' | '.join(str(cell) for cell in row)) + (' |  ' + str(count)))
    print(' ' + (('--' * length) * 2))


if __name__ == "__main__":
    mineSweeper()
