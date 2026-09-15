from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task1/', views.task1, name='task1'),
    path('task2/', views.task2, name='task2'),
    path('task3/', views.task3, name='task3'),
    path('task4/', views.task4, name='task4'),
    path('task5/', views.task5, name='task5'),
    path('task6/', views.task6, name='task6'),
    path('task7/', views.task7, name='task7'),
    path('task8/', views.task8, name='task8'),
    path('task9/', views.task9, name='task9'),
    path('task10/', views.task10, name='task10'),
]