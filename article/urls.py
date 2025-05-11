from django.urls import path
from .views import index, show, new, create, edit, update, delete

app_name = 'article'

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>', show, name='show'),
    path('new/', new, name='new'),
    path('create/', create, name='create'),
    path('<int:pk>/edit/', edit, name='edit'),
    path('<int:pk>/update/', update, name='update'),
    path('<int:pk>/delete/', delete, name='delete'),
]