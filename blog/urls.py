from django.urls import path
from .views import index, post_single

urlpatterns = [
    path('',index,name='index'),
        path('<int:pk>/',post_single,name='single'),
]
