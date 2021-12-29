"""Conway\'s Game of Life."""


# ---------------------- Exercise 1 ------------------------
def board(n):
    """
    Kataskeuastis board (pinaka paixnidiou).
    Kataskeuazei anaparastasi pinaka paixnidiou me n x n kelia, opou
    kanena keli den einai zwntano.
    Epistrefei apaparastasi pinaka paixnidiou, h opoia einai
    ena le3iko (dict) me n*n stoixeia.
    Ka8e keli antistoixei se ena stoixeio me key to tuple (i,j), opou
    i o ari8mos grammis kai j o ari8mos stilis pou brisketai to keli.
    (H ari8misi grammwn kai sthlwn einai apo 0 ews n-1. To panw aristera keli
    brisketai sto (0,0).)
    H timi (value) tou stoixeiou einai True 'h False analoga
    ean to keli einai zwntano 'h oxi.

     Examples:
    >>> game = board(3)
    >>> len(game)
    9
    >>> game == {(0, 0): False, (0, 1): False, (0, 2): False, (1, 0): False, (1, 1): False, (1, 2): False, (2, 0): False, (2, 1): False, (2, 2): False}
    True
    >>> game[2,1]
    False

    :param n: Board's dimension.
    :return:
    """

    dictionary = {}
    i, j = 0, 0
    for item in range(n * n):
        dictionary[(i, j)] = False
        j += 1
        if j == n:
            i += 1
            j = 0
    return dictionary


# ---------------------- Exercise 2 ------------------------
def is_alive(board, p):
    """
    Checks if a specific cell is alive.

     Example:
    >>> is_alive(board(4), (3,2))
    False

    :param board: The game's board.
    :param p: Cell's position (tuple in (i,j) form).
    :return: True if the cell is alive, False otherwise.
    """

    return board[p]


def set_alive(board, p, alive):
    """
    Adds or removes life to/from a cell. Cell becomes active if the alive variable is True. If it is false,
    cell dies.

     Examples:
    >>> game = board(4)
    >>> is_alive(game, (3,2))
    False
    >>> set_alive(game, (3,2), True)
    >>> is_alive(game, (3,2))
    True
    >>> set_alive(game, (3,2), False)
    >>> is_alive(game, (3,2))
    False

    :param board: The game's board.
    :param p: Cell's position (tuple in (i,j) form).
    :param alive: Boolean value, True or False.
    """

    board[p] = alive


def get_size(board):
    """
    Game board's size.

     Examples:
    >>> get_size(board(4))
    4
    >>> get_size(board(10))
    10

    :param board: The game's board.
    :return: n if the board has n x n dimensions.
    """

    from math import sqrt
    return int(sqrt(len(board)))


# ---------------------- Exercise 3 ------------------------
def copy_board(board):
    """
    Board's copy.

     Examples:
    >>> game = board(10)
    >>> set_alive(game, (4,7), True)
    >>> game2 = copy_board(game)
    >>> game2 is game
    False
    >>> is_alive(game2, (4,7))
    True

    :param board: The game's board.
    :return: A new board which is a copy of the current one.
    """

    return board.copy()


# ---------------------- Exercise 4 ------------------------
def get_iterator(board):
    """
    Iterator gia sarwsi stoixeiwn pinaka paixnidiou.
    Epistrefei iterator pou dinei ta kelia tou board arxizontas apo
    ta kelia tis grammis 0: (0,0), (0,1), (0,2),..., meta akolou8oun ta
    kelia tis grammis 1: (1,0), (1,1), (1,2),... ktl. mexri na e3antli8oun
    ola ta kelia. Gia ka8e keli, o iterator epistrefei tin 8esi tou kai
    logiki timi True 'h False analogws ean einai zwntano 'h oxi.

     Examples:
    >>> game = board(3)
    >>> set_alive(game, (2, 1), True)
    >>> for cell in get_iterator(game):
    ...     print(cell)
    ...
    ((0, 0), False)
    ((0, 1), False)
    ((0, 2), False)
    ((1, 0), False)
    ((1, 1), False)
    ((1, 2), False)
    ((2, 0), False)
    ((2, 1), True)
    ((2, 2), False)

    :param board: The game's board.
    :return: A new board which is a copy of the current one.
    """

    a = list(board.items())
    a.sort()
    iterator = iter(a)
    return iterator


# ---------------------- Exercise 5 ------------------------
def print_board(board):
    s = 0
    for item in get_iterator(board):
        s = s + 1

        if item[1] == True:
            print(chr(11035), end='')
        else:
            print(chr(11036), end='')
        if s == get_size(board):
            print('\n', end='')
            s = 0


# ---------------------- Exercise 6 ------------------------
def neighbors(p):
    newset = set
    s = p[1] - 1

    for i in range(8):
        if i < 3:
            newset = newset.union({(p[0] - 1, s)})
            s = s + 1
        elif i == 3:
            s = p[1] - 1
            newset = newset.union({(p[0], p[1] - 1)})

        elif i == 4:
            newset = newset.union({(p[0], p[1] + 1)})

        else:
            newset = newset.union({(p[0] + 1, s)})
            s = s + 1

    return newset


# ---------------------- Exercise 7 ------------------------
def place_blinker(board, p=(0, 0)):
    """
    Blinker placement. Places 3 living organisms on the board table,
    in adjacent cells of the same column, starting at position
    p and moving on to the following lines.

     Examples:

    >>> game = board(5)
    >>> place_blinker(game)
    >>> print_board(game)
    ⬛⬜⬜⬜⬜
    ⬛⬜⬜⬜⬜
    ⬛⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜
    >>> place_blinker(game, (1,2))
    >>> print_board(game)
    ⬛⬜⬜⬜⬜
    ⬛⬜⬛⬜⬜
    ⬛⬜⬛⬜⬜
    ⬜⬜⬛⬜⬜
    ⬜⬜⬜⬜⬜
    >>> place_blinker(game, (4,4))
    >>> print_board(game)
    ⬛⬜⬜⬜⬜
    ⬛⬜⬛⬜⬜
    ⬛⬜⬛⬜⬜
    ⬜⬜⬛⬜⬜
    ⬜⬜⬜⬜⬛

    :param board: The game's board.
    :param p: Starting Cell position (tuple (i,j) with default value (0,0))
    """

    s = p[0]
    for i in range(3):
        set_alive(board, (s, p[1]), True)
        s = s + 1
        if s == get_size(board):
            break


def place_glider(board, p=(0, 0)):
    """
    Glider placement. Places 5 living organisms on the board table in glider scheme, starting at position p (see
    examples below). Note that the cell at position p is not alive.

     Examples:
    >>> game = board(7)
    >>> place_glider(game)
    >>> print_board(game)
    ⬜⬜⬛⬜⬜⬜⬜
    ⬛⬜⬛⬜⬜⬜⬜
    ⬜⬛⬛⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬜
    >>> place_glider(game, (3,3))
    >>> print_board(game)
    ⬜⬜⬛⬜⬜⬜⬜
    ⬛⬜⬛⬜⬜⬜⬜
    ⬜⬛⬛⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬛⬜
    ⬜⬜⬜⬛⬜⬛⬜
    ⬜⬜⬜⬜⬛⬛⬜
    ⬜⬜⬜⬜⬜⬜⬜

   :param board: The game's board.
   :param p: Starting Cell position (tuple (i,j) with default value (0,0))
   """

    if p[1] + 2 < get_size(board) and p[0] + 2 < get_size(board):
        set_alive(board, p, False)
        set_alive(board, (p[0], p[1] + 2), True)
        set_alive(board, (p[0] + 1, p[1]), True)
        set_alive(board, (p[0] + 1, p[1] + 2), True)
        set_alive(board, (p[0] + 2, p[1] + 1), True)
        set_alive(board, (p[0] + 2, p[1] + 2), True)
    else:
        print('Neighbors of this specific cell were less than 5 so the board will remain the same')


# ---------------------- Exercise 8 ------------------------
def tick(board):
    """
    Changes the board table by moving to the next generation, according to the
    Game of Life rules.

     Examples:
    >>> game = board(6)
    >>> place_glider(game)
    >>> place_blinker(game, (3,4))
    >>> print_board(game)
    ⬜⬜⬛⬜⬜⬜
    ⬛⬜⬛⬜⬜⬜
    ⬜⬛⬛⬜⬜⬜
    ⬜⬜⬜⬜⬛⬜
    ⬜⬜⬜⬜⬛⬜
    ⬜⬜⬜⬜⬛⬜
    >>> tick(game)
    >>> print_board(game)
    ⬜⬛⬜⬜⬜⬜
    ⬜⬜⬛⬛⬜⬜
    ⬜⬛⬛⬛⬜⬜
    ⬜⬜⬜⬛⬜⬜
    ⬜⬜⬜⬛⬛⬛
    ⬜⬜⬜⬜⬜⬜

    :param board: The game's board.
    """

    copied_dict = copy_board(board)
    for item in copied_dict.keys():
        copied_dict[item] = False

    counter = 0
    for key in board.keys():
        for item in neighbors(key):
            if item[0] >= get_size(board) or item[0] < 0 or item[1] >= get_size(board) or item[1] < 0:
                continue
            else:
                if is_alive(board, item) == True:
                    counter = counter + 1
        if is_alive(board, key) == True:
            if counter == 2 or counter == 3:
                set_alive(copied_dict, key, True)
        else:
            if counter == 3:
                set_alive(copied_dict, key, True)
        counter = 0

    for key in copied_dict.keys():
        board[key] = copied_dict[key]


# ---------------------- Exercise 9 ------------------------

if __name__ == '__main__':
    """Starts the game for a specific initial setting, for 100 generations.
    The game board is displayed at each step. Leaves 3 blank lines between consecutive tables.
    """

    # Initial board
    game = board(10)
    place_blinker(game, (1, 2))
    place_glider(game, (2, 4))

    from time import sleep

    for i in range(100):
        tick(game)
        print_board(game)
        sleep(0.3)
        print('\n' + '\n' + '\n')
