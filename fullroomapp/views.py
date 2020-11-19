from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        map = base_map_generator(int(request.POST['x-width']),
                int(request.POST['y-length']))

        list_of_invalid_tiles = request.POST['invalids'].split(';')
        for coordinate in list_of_invalid_tiles:
            coordinate = coordinate.split(',')
            map = set_invalid_tiles(map, int(coordinate[0]), int(coordinate[1]))
        # Until parsed later, this shows the resulting map onto the terminal
        print(map)
        return render(request, 'index.html', {'map': map})

    return render(request, 'index.html')

# Base map generator, initially all tiles are set to 1 to indicate free tiles
def base_map_generator(width, length):
    return [[1 for i in range(width)] for j in range(length)]

# Sets invalid tiles by setting their value to 0
def set_invalid_tiles(map, x, y):
    map[x][y] = 0
    return map

# TODO : CSP algorithm, prioritize healthy people first
def csp():
    pass