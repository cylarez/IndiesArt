# Create your views here.
from django.shortcuts import *
from django import forms
from main.models import *
from main.admin import *
import os

UPLOAD_DIR = settings.MEDIA_ROOT +'uploads/'

def handle_uploaded_file(files, tempDir):
	for img in files :
		f = tempDir + img.name
		f = f.encode('ascii', 'ignore')
		destination = open(f, 'wb+')
		for chunk in img.chunks():
			destination.write(chunk)
		destination.close()

def submissionNew(request):

	if request.method == 'POST' and len(request.FILES.getlist('file_upload')) > 0:
		post = request.POST
		
		# Create the artist
		a = Artist(lastname=post['lastname'], firstname=post['firstname'], bio=post['bio'], email=post['email'], submission=True)
		a.save()
		
		# Create a temp folder
		tempDir = UPLOAD_DIR + str(a.pk) +'/'
		os.makedirs(tempDir)
		
		# Launch Upload
		handle_uploaded_file(request.FILES.getlist('file_upload'), tempDir)
		
		# Create collection
		art_type = ArtType.objects.get(pk=post['category_id'])
		c = Collection(name=post['collection'], artist=a, art_type=art_type)
		c.save()
		
		# launch Import
		load_image(c, tempDir)
		
		# Link the art type
		a.art_types.add(art_type)
		
		# Link the urls
		urls = post.getlist('url')
		types = [1, 3, 6, 9]
		
		for i in xrange(len(urls)):
			url = urls[i]
			if (url != "") :
				t = UrlType.objects.get(pk=types[i])
				u = Url(name=url, artist=a, url_type=t)
				u.save()
				
		from django.core.mail import EmailMultiAlternatives
		from django.template.loader import render_to_string
		
		message_html = render_to_string('account/submission-email-1.html', {'artist': a})
		message_text = strip_tags(message_html)
		msg = EmailMultiAlternatives('Submission received', message_text, settings.EMAIL_HOST_USER, [a.email, settings.EMAIL_HOST_USER])
		msg.attach_alternative(message_html, "text/html")
		msg.send()
		
	category = ArtType.objects.all()
	urlType = UrlType.objects.all()
	
	return render_to_response('account/submission-new.html', {'category': category, 'urlType': urlType})


def submissionList(request):

	artists =	Artist.objects.filter(submission=1, active=1)
	images	=	[]
	for a in artists :
		images.append(a.images(1)[0])
	return render_to_response('account/submission-list.html', {'images':images})