from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllSectionView.as_view(), name="all_section"),
    path('<slug:slug_sect>/', views.SectionView.as_view(), name="section"),
    path('<slug:slug_sect>/<slug:slug_ssect>/', views.SubsectionView.as_view(), name="subsection"),
    path('<slug:slug_sect>/<slug:slug_ssect>/<slug:slug_sssect>/', views.SubsubsectionView.as_view(), name="subsubsection"),
]
