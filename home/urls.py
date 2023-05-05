from home import views
from django.urls import path

app_name = 'home'
urlpatterns = [

    path('index', views.index, name='index'),
    path('create_post', views.create_post, name='create-post'),
     path('<str:speaker_name>', views.detail, name='detail'),
]
