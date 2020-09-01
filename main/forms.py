from django import forms
# from phonenumber_field.modelfields import PhoneNumberField

class BackCallForm(forms.Form):
    # Форма обратного звонка
    name = forms.CharField(max_length=25)
    phone = forms.CharField(max_length=25)