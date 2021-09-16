from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.index, name='create'),
    path('<int:pk>/', views.index, name='detail'),
    path('<int:pk>/delete/', views.index, name='delete'),
    path('<int:pk>/update/', views.index, name='update'),
]
