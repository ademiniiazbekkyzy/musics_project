from music_app.views import *

from django.urls import path

urlpatterns = [
    path('music/', MusicListView.as_view()),
    path('music-create/', MusicCreateView.as_view()),
    path('music-update/<int:pk>/', MusicUpdateView.as_view()),
    path('music-detail/<int:pk>/', MusicDetailView.as_view()),
    path('music-delete/<int:id>/', MusicDeleteView.as_view()),
    # path('music/', get_music),
    # path('music/<int:id>/', music_detail),
    # path('music-create/', music_create),

]