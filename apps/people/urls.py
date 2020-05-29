from django.urls import path
from . import views

urlpatterns = [
    path('', views.PeopleView.as_view(), name="people"),
    path('<int:pk>/', views.ManView.as_view(), name="man"),
]
