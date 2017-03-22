from django.conf.urls import url
from . import views

app_name = 'book'
urlpatterns = [
    url(r'^$', views.book_list, name='book_list'),
]