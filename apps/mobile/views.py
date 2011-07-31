# Create your views here.
from django.shortcuts import *
from django import forms
from main.models import *
from django.template import Context, Template
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files import File
from django.conf import settings
import json

def main(request):
    data = default_storage.open(settings.MOBILE_JSON_PATH).read()
    return HttpResponse(data, mimetype='text/javascript')

def artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    t = loader.get_template('mobile/artist.json')
    c = Context({
                'artist': json.dumps(artist.toJson(), indent=4),
                })
    
    return HttpResponse(t.render(c), mimetype='text/javascript')

def discover(request):
    images = Image.objects.filter(collection__artist__submission=0, collection__artist__active=1).order_by('?')[:57]
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
    
def about(request):
    t = loader.get_template('mobile/about.json')
    data = Context(get_about_data())
    return HttpResponse(t.render(data), mimetype='text/javascript')
