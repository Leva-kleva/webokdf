from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllPostsView.as_view(), name="posts"),
    path('<slug:slug_post>/', views.PostView.as_view(), name="post"),
]
