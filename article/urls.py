from django.urls import path
from .views import index, show, create, update, delete

app_name = 'article'

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>', show, name='show'),
    path('create/', create, name='create'),
    path('<int:pk>/update/', update, name='update'),
    path('<int:pk>/delete/', delete, name='delete'),
]