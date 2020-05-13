# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'game/index.html')

def table(request, table_code):
    #Check that table_code exists before you render.
    return render(request, 'game/table.html', {
        'table_code': table_code
    })
