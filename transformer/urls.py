from django.urls import path

from .views import home, train, predict
urlpatterns = [
    path('', home, name='home'),
    path('train/', train, name='train'),
    path('predict/', predict, name='predict'),
]
