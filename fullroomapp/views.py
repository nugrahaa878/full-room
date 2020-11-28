from django.shortcuts import render, redirect
from .forms import RoomDataForm
from .models import RoomData

import random
import fullroomapp.engine

# SAMPLE MAP (For Testing Purposes)
SAMPLE_MAP = [[0,0,0,1,1], 
              [0,1,1,0,0], 
              [0,1,1,1,0], 
              [0,0,0,0,0],
              [1,0,0,0,0]]

def index(request):
    # if request.method == 'POST':
    #     width = int(request.POST['x-width'])
    #     length = int(request.POST['y-length'])
    #     healthy = int(request.POST['healthy'])
    #     sick = int(request.POST['sick'])

    #     if guard(width) and guard(length) and guard(healthy) and guard(sick):
    #         board = solve_board(base_board_generator(width, length), healthy, sick)
    #         return render(request, 'index.html', {'map': board})
        
    #     return render(request, 'index.html', {'err_msg': 'Number values must be within range 1-50'})

    roomdata_form = RoomDataForm(request.POST or None)

    if request.method == "POST":
        if roomdata_form.is_valid():
            roomdata_form.save()

            return redirect('generate')

    context = {
        'roomdata_form': roomdata_form
    }

    return render(request, 'index.html', context)

def generateMap(request):
    data = RoomData.objects.last()
    mapWidth = data.width
    mapLength = data.length
    mapHealthy = data.healthy
    mapSick = data.sick
    mapRoom = base_board_generator(mapWidth, mapLength)

    for item in mapRoom:
        for item2 in item:
            print(item2, end=" ")
        print()
    
    if request.method == "POST":    
        board = solve_board(mapRoom, mapHealthy, mapSick)
        return redirect('home')

    return render(request, 'generate.html')

def guard(guarded_int):
    return guarded_int > 0 and guarded_int <= 50

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
