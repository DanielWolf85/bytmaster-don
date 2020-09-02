from django import forms
# from phonenumber_field.modelfields import PhoneNumberField

class BackCallForm(forms.Form):
    # Форма обратного звонка
    name = forms.CharField(max_length=25, label='Ваше имя')
    phone = forms.CharField(max_length=25, label='Ваш телефон*', required=True)


class ZayavkaForm(forms.Form):
    # Форма принятия заявки
    name = forms.CharField(max_length=25, label='Как Вас зовут?')
    phone = forms.CharField(max_length=25, label='Ваш телефон*', required=True)
    problem = forms.CharField(label='Опишите проблему', widget=forms.Textarea)