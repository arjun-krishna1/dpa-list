from django.urls import path


from .views import (
    index,
    join,
)

urlpatterns = [
    path('', index, name='index'),
    path('join/', join, name='join'),
]
