from django.urls import path
import views

urlpatterns = [
    path('', views.CreateForm, name='index'),
]
