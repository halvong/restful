from django.urls import path, include
from toys import views

urlpatterns = [
    path('toys/', views.toy_list),
    path('toys/<int:pk>', views.toy_detail),
]
