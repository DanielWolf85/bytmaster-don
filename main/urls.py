from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    # main views
    path('', views.main_view, name="main_view"),
    path('remont-holodilnikov/', views.refrigerators_view, name='refrigerators_view'),
    path('remont-stiralnyh-mashin/', views.washing_machines_view, name='washing_machines_view'),
]