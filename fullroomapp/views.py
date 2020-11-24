from django.shortcuts import render
import random
import fullroomapp.engine

# SAMPLE MAP (For Testing Purposes)
SAMPLE_MAP = [[0,0,0,1,1], 
              [0,1,1,0,0], 
              [0,1,1,1,0], 
              [0,0,0,0,0],
              [1,0,0,0,0]]

def index(request):
    if request.method == 'POST':
        board = solve_board(base_board_generator(int(request.POST['x-width']),
                int(request.POST['y-length'])), int(request.POST['healthy']),
                int(request.POST['sick']))

        return render(request, 'index.html', {'map': board})

    return render(request, 'index.html')

# Base board generator
def base_board_generator(width, length):
    return set_invalid_tiles([['_' for i in range(width)] for j in range(length)])

# Sets invalid tiles by setting their value to #
def set_invalid_tiles(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if (random.randint(0, 1) == 1):
                board[x][y] = '#'
    return board

# For board/board preview asynchronous calls
def board_preview(request):
    if request.method == 'POST':
        board = base_board_generator(int(request.POST['x-width']),
                int(request.POST['y-length']))
        return board
    
    return ["Invalid length and/or width!"]

# To solve the board
def solve_board(board, healthy_people, sick_people):
    return fullroomapp.engine.solve_for_healthy(board, healthy_people, sick_people)
