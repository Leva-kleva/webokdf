from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllContentView.as_view(), name="all_content"),
    #path('parade/', views.ParadeView.as_view(), name="parade"),
    #path('retro/', views.RetroView.as_view(), name="retro"),
    #path('fontan/', views.FontansView.as_view(), name="fontan"),
    #path('fontan/add', views.AddFontansView.as_view(), name="add_fontan"),
    path('<slug:slug_page>/', views.PageView.as_view(), name="page"),
    path('fontan/add/', views.AddFontansView.as_view(), name="add_fontan"),
    path('wishes/sticker/', views.AddStickerView.as_view(), name="add_sticker"),
    #path('wishes/all_stickers/', views.AllStickersView.as_view(), name="all_stickers"),
    path('stream/add/', views.AddHistoryView.as_view(), name="add_history"),
    #path('contests/add/', views.AddZagsView.as_view(), name="add_zags"),
]
