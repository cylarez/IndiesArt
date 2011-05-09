from django.shortcuts import *
from main.models import *
from blog.models import *
from django.contrib.sites.models import Site
from django.core import serializers
from django.template import Context, Template

import random

def post(request, collection_id):

	c = get_object_or_404(Collection, pk=collection_id)
	site = Site.objects.get(id=settings.SITE_ID)
	url = 'http://'+ site.domain
	images = c.images()[:12]
	title = 'New Gallery for %s' % c.artist
	
	return render_to_response('blog/post_gallery.html', {'artist':c.artist, 'collection':c, 'images':images, 'url':url })
