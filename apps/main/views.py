from django.shortcuts import *
from main.models import *
from blog.models import *
from django.contrib.sites.models import Site
from django.core import serializers
from django.template import Context, Template
from django.core.paginator import Paginator, InvalidPage, EmptyPage

import random, json

def getHomeArtists():
    homeImageId = [9688, 13213, 13704, 13582, 13156, 12563, 12351, 11663, 11291, 10689, 9940]
    homeArtists = []
    
    for id in homeImageId :
        i = Image.objects.get(pk=id)
        a = i.collection.artist
        a.image = i
        homeArtists.append(a)
    
    return homeArtists

def index(request):

	homeArtists = getHomeArtists()
	artists = Artist.objects.filter(active=1, submission=0).order_by('?')[:7]
	for a in artists :
		a.images(4)
	
	lastCollection = []
	lastArtists = Artist.objects.filter(active=1, submission=0)[:3]
	
	for artist in lastArtists :
		focused_collection = False
		i = 0
		collections = artist.collections()
		while (focused_collection == False) :
			collection = collections[i]
			i += 1
			focused = collection.focused()
			if len(focused) > 0 :
				focused_collection = True
		collection.mainImage = focused[0]
		collection.homeImages = collection.images[:10]	
		lastCollection.append(collection)
	
	lastImages = Image.objects.filter(collection__artist__submission=0, collection__artist__active=1)[:16]
	randomImages = Image.objects.filter(collection__artist__submission=0, collection__artist__active=1).order_by('?')[:16]
	
	return render_to_response('main/index.html', {'homeArtists':homeArtists, 'artists':artists, 'lastImages':lastImages, 'lastCollection':lastCollection, 'randomImages': randomImages})


def artists(request, num):
	artists = Artist.objects.filter(active=1, submission=0)
	paginator = Paginator(artists, 12)
	
	try:
		page = paginator.page(num)
	except (EmptyPage, InvalidPage):
		raise Http404
	
	t = loader.get_template('main/artists_pager.html')
	c = Context({'page': page})
	pager = t.render(c)
	
	artists = page.object_list
	
	for a in artists :
		a.images(8)
	return render_to_response('main/search.html', {'artists': artists, 'pager': pager, 'page': page})

def artist(request, artist_id):
	artist = get_object_or_404(Artist, pk=artist_id)
		
	if (artist.submission == True) :
		return submission(artist)
		
	artist.images(8)
	return render_to_response('main/artist.html', {'artist':artist})


def submission(artist):	
	artist.images(32)
	return render_to_response('account/submission.html', {'artist':artist})


def collection(request, collection_id, num):
	collection = get_object_or_404(Collection, pk=collection_id)
	artist = collection.artist
	if (artist.submission == True) :
		raise Http404
		
	images = collection.images()
	
	paginator = Paginator(images, 16)
	
	try:
		page = paginator.page(num)
	except (EmptyPage, InvalidPage):
		raise Http404
	
	t = loader.get_template('main/collection_pager.html')
	c = Context({'page': page, 'collection': collection})
	pager = t.render(c)
	images = page.object_list
	return render_to_response('main/collection.html', {'artist':artist, 'collection': collection, 'images': images, 'pager': pager, 'page': page})

def image(request, image_id):
	site = Site.objects.get(id=settings.SITE_ID)
	image = get_object_or_404(Image, pk=image_id)
	artist = image.collection.artist
	
	if (artist.active == False) or (artist.submission == True) :
		raise Http404
	
	collection = image.collection
	images = collection.images()

	#collection.images	=	random.sample(images, len(images)<10 and len(images) or 10)
	collection.images	=	images[:10]

	resize = (image.photo.width > 670)
	return render_to_response('main/image.html', {'image':image, 'collection':collection, 'artist':artist, 'resize':resize, 'url':site.domain})

def random(request):
	images = Image.objects.filter(collection__artist__submission=0, collection__artist__active=1).order_by('?')[:16]
	return render_to_response('main/random.html', {'images': images})
	
