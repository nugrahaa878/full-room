from django.shortcuts import render

# SAMPLE MAP (For Testing Purposes)
SAMPLE_MAP = [[0,0,0,1,1], 
              [0,1,1,0,0], 
              [0,1,1,1,0], 
              [0,0,0,0,0],
              [1,0,0,0,0]]

# Create your views here.
def index(request):
    return render(request, 'index.html', {'map': SAMPLE_MAP})
