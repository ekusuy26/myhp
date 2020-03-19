from django.urls import path
from . import views
# pathの関数とmysite内の全viewをインポートする、ということ

urlpatterns = [
    path('', views.post_list, name='post_list'),
]