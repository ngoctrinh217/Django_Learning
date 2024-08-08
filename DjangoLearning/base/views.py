from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

rooms = [
    {
        'id': 1, 'name': 'Lets learning with python'
    },
    {
        'id': 2, 'name': 'Design with me'
    },
    {
        'id': 3, 'name': 'Frontend with python'
    }
]


def home(request):
    return render (request, 'home.html', {'rooms': rooms})
def rooms(request):
    return render (request, 'rooms.html')
