from django.shortcuts import render
from .models import Review
from .forms import BackCallForm, ZayavkaForm
from django.core.mail import send_mail


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

def privacy_policy_view(request):
    # Политика конфиденциальности
    return render(request, 'main/components/privacy_policy.html')



def back_call_form(request):
    # обработчик формы обратного звонка
    sent = False
    if request.method == 'POST':
        form = BackCallForm(request.POST)
        # Если форма заполнена корректно,
        # сохраняем все введенные значения
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'danielvolf1985@yandex.ru'
            sender = 'danielvolf1985@yandex.ru'
            # message = str(cd['name']) + " : " + str(cd['phone'])
            message = "Обратный звонок!\n\nМеня зовут: " + str(cd['name']) + "\nПерезвоните мне на номер: " + str(cd['phone']) + "\n\nЗаявка пришла с нового сайта bytmaster-don.com"
            # send mail...
            send_mail(subject, message, sender, ['danielvolf1985@yandex.ru'])
            sent = True
    else:
        form = BackCallForm()
    # Выводим форму в шаблон
    return render(request, 'main/back_call.html', {
        'form': form,
        'sent': sent,
    })


def zayavka_form(request):
    # обработчик формы заявки
    sent = False
    if request.method == 'POST':
        form = ZayavkaForm(request.POST)
        # Если форма заполнена корректно,
        # сохраняем все введенные значения
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'danielvolf1985@yandex.ru'
            sender = 'danielvolf1985@yandex.ru'
            message = "Заявка!\n\n" + "Меня зовут: " + str(cd['name']) + "\nМой телефон: " + str(cd['phone']) + "\nУ меня такая проблема: " + str(cd['problem']) + "\n\nЗаявка пришла с нового сайта bytmaster-don.com"
            # send mail...
            send_mail(subject, message, sender, ['danielvolf1985@yandex.ru'])
            sent = True
    else:
        form = ZayavkaForm()
    # Выводим форму в шаблон
    return render(request, 'main/zayavka.html', {
        'form': form,
        'sent': sent,
    })
