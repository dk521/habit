from django.shortcuts import render, HttpResponse
from .models import *



def index(request):
    return render(request, 'index.html', {})


def dashboard(request):
    habits = Habits.objects.all()

    context = {
        'habits' : habits,
    }

    return render(request, 'Dash.html', context)


def recommend(request):
    if request.method == 'POST':
        # print(True)
        habits = Habits.objects.all()

        collected_data = {}
        for i in habits:
            id = request.POST.get(i)
            habit = request.POST.get(str(i.id))
            if habit == 'True':
                collected_data[i.name] = True

            else:
                collected_data[i.name] = False
            print(habit)

        mood = request.POST.get('mood')         # mood data  >>>>>>>>>>>>>


        # <<<<<<<<<<<<<<<<  tick marks are stored >>>>>>>>>>>>>>>
        



        # print('ID: ',i, id)
    return HttpResponse('Working')
