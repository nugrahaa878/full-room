from django.shortcuts import render
import random

# SAMPLE MAP (For Testing Purposes)
SAMPLE_MAP = [[0,0,0,1,1], 
              [0,1,1,0,0], 
              [0,1,1,1,0], 
              [0,0,0,0,0],
              [1,0,0,0,0]]

def index(request):
    if request.method == 'POST':
        map = base_map_generator(int(request.POST['x-width']),
                int(request.POST['y-length']))
                
        # Until parsed later, this shows the resulting map onto the terminal
        print(map)
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
