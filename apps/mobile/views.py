# Create your views here.
from django.shortcuts import *
from django import forms
from main.models import *
from main.views import getHomeArtists
from django.template import Context, Template
import json

def main(request):
    t = loader.get_template('mobile/main.json')   
    return HttpResponse(t.render(Context({})), mimetype='text/javascript')

def main_bck(request):
    slides = []
    submissions = []
    
    for artist in getHomeArtists() :
        slides.append(artist.image.home_file_name())
    
    artists = []
    for artist in Artist.objects.filter(active=1):
        collections = artist.collections()
        a = artist.toJson( collections[len(collections)-1].focused()[0])
        if artist.submission :
            submissions.append(a)
        else :
            artists.append(a)
    
    
    t = loader.get_template('mobile/main.json')
    c = Context({
                'artists': json.dumps(artists, indent=4),
                'slides': json.dumps(slides, indent=4),
                'submissions': json.dumps(submissions, indent=4)
                })
    
    return HttpResponse(t.render(c), mimetype='text/javascript')

def artist(request, artist_id):
    
    artist = get_object_or_404(Artist, pk=artist_id)
    t = loader.get_template('mobile/artist.json')
    c = Context({
                'artist': json.dumps(artist.toJson(), indent=4),
                })
    
    return HttpResponse(t.render(c), mimetype='text/javascript')

    