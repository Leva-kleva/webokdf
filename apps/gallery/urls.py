from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllGalleryView.as_view(), name="all_gallery"),
    path('<int:pk>', views.GalleryView.as_view(), name="gallery"),
    #path('img/', views.AllGalleryView.as_view(), name),
    path('img/<int:pk>', views.ImgView.as_view(), name="image"),
]
