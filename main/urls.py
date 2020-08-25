from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    # main views
    path('', views.main_view, name="main_view"),
    path('remont-holodilnikov/', views.refrigerators_view, name='refrigerators_view'),
    path('remont-stiralnyh-mashin/', views.washing_machines_view, name='washing_machines_view'),
    path('remont-posudomoechnyh-mashin/', views.dishwashers_view, name='dishwashers_view'),
    path('remont-kofemashin/', views.coffee_machines_view, name='coffee_machines_view'),
    path('remont-gazovyh-plit/', views.gas_stoves_view, name='gas_stoves_view'),
    path('remont-pylesosov/', views.hoovers_view, name='hoovers_view'),
    path('ustanovka-i-podklyuchenie/', views.installation_view, name='installation_view'),
    path('chistka-kondicionerov/', views.cleaning_of_air_view, name='cleaning_of_air_view'),
    path('discounts/', views.discounts_view, name='discounts_view'),
    path('faq/', views.faq_view, name='faq_view'),
    path('contacts/', views.contacts_view, name='contacts_view'),
    path('about/', views.about_view, name='about_view'),
]