from django.shortcuts import render
import random

# SAMPLE MAP (For Testing Purposes)
SAMPLE_MAP = [[0,0,0,1,1], 
              [0,1,1,0,0], 
              [0,1,1,1,0], 
              [0,0,0,0,0],
              [1,0,0,0,0]]

# Create your views here.
def index(request):
    # Dummy inputs
    map = base_map_generator(5,5)
    map = set_invalid_tiles(map, 1, 2)
    print(map)
    
    return render(request, 'index.html', {'map': SAMPLE_MAP})

# Base map generator
def base_map_generator(panjang, lebar):
    return [[1 for i in range(panjang)] for j in range(lebar)]

def set_invalid_tiles(map, x, y):
    map[x][y] = 0
    return map

# CSP algorithm
def csp():
    pass