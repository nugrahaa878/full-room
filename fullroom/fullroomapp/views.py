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
    return render(request, 'index.html', {'map': SAMPLE_MAP})

# Simple map generator
def random_map_generator(panjang, lebar):
    return [[random.randint(0,1) for i in range(panjang)] for j in range(lebar)]
