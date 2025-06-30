from django.shortcuts import render

def curriculum_view(request):
    return render(request, 'inicio/curriculum_vitae.html')
