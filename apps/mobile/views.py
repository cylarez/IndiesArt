# Create your views here.
from django.shortcuts import *
from django import forms
from main.models import *
from main.views import getHomeArtists
from django.template import Context, Template
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files import File
import json

JSON_PATH = 'mobile_data.json'

def main(request):
    #load_data()
    data = default_storage.open(JSON_PATH).read()
    return HttpResponse(data, mimetype='text/javascript')

def load_data():
    slides = []
    submissions = []
    
    for artist in getHomeArtists() :
        slides.append({'url':artist.image.home_file_name(), 'name': artist.name(), 'id':artist.pk})
    
    artists = []
    for artist in Artist.objects.filter(active=1):
        collections = artist.collections()
        a = artist.toJson(True)
        if artist.submission :
            submissions.append(a)
        else :
            artists.append(a)
    
    
    t = loader.get_template('mobile/main_live.json')
    c = Context({
                'artists': json.dumps(artists, indent=4),
                'slides': json.dumps(slides, indent=4),
                'submissions': json.dumps(submissions, indent=4)
                })
    
    f = open(settings.MEDIA_ROOT + JSON_PATH, 'w')
    f.write(t.render(c))
    f.close()

def artist(request, artist_id):
    
    artist = get_object_or_404(Artist, pk=artist_id)
    t = loader.get_template('mobile/artist.json')
    c = Context({
                'artist': json.dumps(artist.toJson(), indent=4),
                })
    
    return HttpResponse(t.render(c), mimetype='text/javascript')

def discover(request):
    
    images = Image.objects.filter(collection__artist__submission=0, collection__artist__active=1).order_by('?')[:58]
    _images = []
    for image in images :
        data = image.toJson()
        data.update(artist = {'id':image.collection.artist.id, 'name':image.collection.artist.name()})
        _images.append(data)
        
    artist = {'id':0, 'images':_images}
    
    t = loader.get_template('mobile/artist.json')
    c = Context({
                'artist': json.dumps(artist, indent=4),
                })
    
    return HttpResponse(t.render(c), mimetype='text/javascript')
    