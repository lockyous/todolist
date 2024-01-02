from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:jw>/', views.todo_detail, name='todo_detail'),
    path('post/', views.todo_post, name='todo_post'),
    path('<int:jw>/edit/', views.todo_edit, name='todo_edit'),
    path('done/', views.todo_done_list, name='todo_done_list'),
    path('done/<int:jw>', views.todo_done, name='todo_done'),
    path('undone/<int:jw>', views.todo_undone, name='todo_undone')
]