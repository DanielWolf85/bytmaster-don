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

def dishwashers_view(request):
    # Ремонт посудомоечных машин
    return render(request, 'main/dishwashers.html')

def coffee_machines_view(request):
    # Ремонт кофемашин  
    return render(request, 'main/coffee_machines.html')

def gas_stoves_view(request):
    # Ремонт газовых плит
    return render(request, 'main/gas_stoves.html')

def hoovers_view(request):
    # Ремонт пылесосов
    return render(request, 'main/hoovers.html')

def installation_view(request):
    # Установка и подключение
    return render(request, 'main/installation.html')

def cleaning_of_air_view(request):
    # Чистка кониционеров
    return render(request, 'main/cleaning_of_air.html')

def discounts_view(request):
    # Скидки
    return render(request, 'main/discounts.html')

def faq_view(request):
    # Часто задаваемые вопросы
    return render(request, 'main/faq.html')

def contacts_view(request):
    # Контакты
    return render(request, 'main/contacts.html')

def about_view(request):
    # О нас
    return render(request, 'main/about.html')