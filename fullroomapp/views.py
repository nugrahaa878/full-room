from django.shortcuts import render, redirect
from .forms import RoomDataForm
from .models import RoomData

import random
import fullroomapp.engine


def index(request):
    roomdata_form = RoomDataForm(request.POST or None)

    if request.method == "POST":
        if roomdata_form.is_valid():
            roomdata_form.save()
            request.session['user_map'] = request.POST['boardMap'].split(',')
            print(request.session['user_map'])
            return redirect('generate')

    context = {
        'roomdata_form': roomdata_form
    }

    return render(request, 'index.html', context)

def generateMap(request):
    data = RoomData.objects.last()
    mapHealthy = data.healthy
    mapSick = data.sick

    if request.method == "POST":    
        [board, remaining_people] = solve_board(request.session['map_result'], mapHealthy, mapSick)
        request.session['map_result'] = board
        request.session['remaining_people'] = remaining_people
        return redirect('result')

    mapWidth = data.width
    mapLength = data.length
    mapRoom = base_board_generator(mapWidth, mapLength)

    if request.session['user_map'] != None:
        request.session['map_result'] = nest_list(request.session['user_map'],mapLength, mapWidth)
        request.session['user_map'] = None
    else:
        request.session['map_result'] = mapRoom

    # debug
    for item in request.session['map_result']:
        for item2 in item:
            print(item2, end=" ")
        print()

    context = {
        'random_map': request.session['map_result']
    }

    return render(request, 'generate.html', context)

def result(request):
    mymap = request.session.get('map_result')
    remaining_people = request.session.get('remaining_people')
    print("Ini map result :")

    # debug
    for row in mymap:
        for i in row:
            print(i, end=" ")
        print()

    context = {
        'map': mymap,
        'remaining_people': remaining_people
    }

    return render(request, 'result.html', context)


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

def nest_list(list1,rows, columns):    
    result=[]               
    start = 0
    end = columns
    for i in range(rows): 
        result.append(list1[start:end])
        start +=columns
        end += columns
    return result
