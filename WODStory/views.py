from django.shortcuts import render

# Create your views here.

def dailyWOD_list(request):
    return render(request, 'WODStory/dailyWOD_list.html', {})
