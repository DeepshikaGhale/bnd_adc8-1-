from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template,Context
from .models import Lyrics


# Create your views here.
def view_Lyrics_page(request):
    return render(request,'Lyrics.html')

def view_Lyrics_lists(request):
    list_of_Lyrics= Lyrics
    print(list_of_Lyrics)
    context_variable = {
        'Lyrics':list_of_Lyrics
    }
    return render(request,'Lyrics.html',context_variable)

def view_Lyrics_form(request):
    return render(request,'Lyricsform.html')

def view_Lyricsdata_save(request):
    if request.method == "POST":
        #get_all = request.POST
        get_UserName = request.POST['Lyrics_UserName']
        print(type(get_UserName))
        get_SongName = request.POST['Lyrics_SongName']
        get_Lyric = request.POST['Lyrics_Lyric']
        print(get_UserName)
        Lyrics_obj = Lyrics(UserName=get_UserName,SongName=get_SongName,Lyric=get_Lyric)
        Lyrics_obj.save()
        return redirect('Harmonyapp/Lyricsdata')
    else:
        return HttpResponse("Error record saving")

def view_Lyricsdata_updateform(request,ID):
    print(ID)
    Lyrics_obj = Lyrics
    print(Lyrics_obj)
    context_varible = {
        'Lyrics':Lyrics_obj
    }
    return render(request,'LyricsUpdateForm.html',context_varible)

def view_update_form_data_in_db(request,ID):
    Lyrics_obj = Lyrics
    print(Lyrics_obj)
    Lyrics_form_data = request.POST
    print(Lyrics_form_data)
    Lyrics_obj.UserName = request.POST['Lyrics_UserName']
    Lyrics_obj.SongName =request.POST['Lyrics_SongName']
    Lyrics_obj.Lyric = request.POST['Lyrics_Lyric']
    
    return HttpResponse("Record Updated!")     