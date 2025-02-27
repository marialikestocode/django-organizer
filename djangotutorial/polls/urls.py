from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path('', views.index, name="index"),
    path('questions/<int:question_id>/', views.detail, name="detail"),
    path('questions/<int:question_id>/vote/', views.vote, name="vote"),
    path('questions/<int:question_id>/results/', views.results, name="results"),
]