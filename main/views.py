from django.shortcuts import render
from .models import Review


def main_view(request):
    # Главная
    return render(request, 'main/main.html')


def refrigerators_view(request):
    # Ремонт холодильников
    return render(request, 'main/refrigerators.html')

def washing_machines_view(request):
    # Ремонт стиральных машин
    return render(request, 'main/washing_machines.html')