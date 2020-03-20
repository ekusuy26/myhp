from django.contrib import admin
from django.urls import path
from . import views
# pathの関数とmysite内の全viewをインポートする、ということ

app_name ="mysite"

urlpatterns = [
    path('top/', views.top, name='top'),
]


# urlpatterns = [
#     path('', views.post_list, name='post_list'),
# ]