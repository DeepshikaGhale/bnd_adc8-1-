

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ 
    path('Lyrics/',view_Lyrics_page), 
    path('Lyricsdata/',view_Lyrics_lists), 
    path('Lyricsform/',view_Lyrics_form),
     path('Lyricsform/save',view_Lyricsdata_save),
     path('Lyricsdata/edit/<int:ID>',view_Lyricsdata_updateform),
     path('Lyricsdata/edit/update/<int:ID>',view_update_form_data_in_db),
    ]