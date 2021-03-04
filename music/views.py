from django.shortcuts import render
from django.views.generic import View ,DetailView ,TemplateView
from .models import *
from django.db.models import Q

# Create your views here.

class Home(View):
    def get(self,request):
        context = {"song":Music.objects.all()}
        return render(request,'music/home.html',context)


class Mymusic(TemplateView):
    template_name = 'music/music_payer.html'


class SongPlay(DetailView):
    model = Music
    template_name = 'music/music_payer.html'
    context_object_name = "song"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allsong'] = Music.objects.all()
        return context


class Search(View):
    def get(self,request):
        search = request.GET.get('search')
        cond = Q(song_title__icontains = search) | Q(song_category__title__icontains = search) | Q(song_movie__icontains = search)
        context = {"song":Music.objects.filter(cond)}
        return render(request,'music/home.html',context)




