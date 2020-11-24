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
        map = solve_map_healthy(base_map_generator(int(request.POST['x-width']),
                int(request.POST['y-length'])), int(request.POST['healthy']))

        return render(request, 'index.html', {'map': map})

    return render(request, 'index.html')

# Base map generator
def base_map_generator(width, length):
    return set_invalid_tiles([['_' for i in range(width)] for j in range(length)])

# Sets invalid tiles by setting their value to #
def set_invalid_tiles(map):
    for x in range(len(map)):
        for y in range(len(map[x])):
            if (random.randint(0, 1) == 1):
                map[x][y] = '#'
    return map

# For board/map preview asynchronous calls
def map_preview(request):
    if request.method == 'POST':
        map = base_map_generator(int(request.POST['x-width']),
                int(request.POST['y-length']))
        return map
    
    return ["Invalid length and/or width!"]

# For ease of engine method call for solving for healthy people
def solve_map_healthy(map, people):
    return fullroomapp.engine.solve_for_healthy(map, people)

# For ease of engine method call for solving for sick people
def solve_map_sick(map):
    # Dummy, awaiting sick algorithm
    return map
