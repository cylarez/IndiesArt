from main.models import *
from blog.models import *
from django.contrib import admin
import os, glob, time, datetime
from django.utils.translation import ugettext_lazy as _
from django.core.files import File
from django.core.files.storage import default_storage
from django.template.loader import render_to_string
from django.template import defaultfilters
from django.contrib.sites.models import Site
from django.utils.html import strip_tags
from datetime import datetime
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


INDIE_BOX = settings.MEDIA_ROOT +'indie_box/'
site = Site.objects.get(id=settings.SITE_ID)

admin.site.register(ArtType)
admin.site.register(MediaType)
admin.site.register(UrlType)

# Images
class ImageAdmin(admin.ModelAdmin):
	list_display = ('name', 'thumb_admin')
	fields = ('name', 'thumb_admin', 'focused',)
	readonly_fields = ('thumb_admin',)

admin.site.register(Image, ImageAdmin)


# Artist
class UrlInline(admin.TabularInline):
	model = Url
	extra = 1

def _approve(artist):
    artist.active = 1
    artist.save()
    message_html = render_to_string('account/submission-email.html', {'artist': artist, 'url':site.domain})
    message_text = strip_tags(message_html)
    msg = EmailMultiAlternatives('Submission pre-approved', message_text, settings.EMAIL_HOST_USER, [artist.email, settings.EMAIL_HOST_USER])
    msg.attach_alternative(message_html, "text/html")
    msg.send() 

def approve(self, request, queryset):
    for artist in queryset:
        _approve(artist)
    self.message_user(request, _("You have approved some artists"))

def _publish(artist):
    artist.created = datetime.now()
    artist.approved = 1
    artist.submission = 0
    artist.save()
    collections = Collection.objects.filter(artist=artist.pk)
    c = collections[0]
    count = _create_post(c, 'Approved Submission for %s' % artist)
    
    message_html = render_to_string('account/submission-published-email.html', {'artist': artist, 'url':site.domain})
    message_text = strip_tags(message_html)
    msg = EmailMultiAlternatives('Submission approved and published', message_text, settings.EMAIL_HOST_USER, [artist.email, settings.EMAIL_HOST_USER])
    msg.attach_alternative(message_html, "text/html")
    msg.send()

def publish(self, request, queryset):
    for artist in queryset:
        _publish(artist)
    self.message_user(request, _("You have publish some artists!"))


class CollectionInline(admin.TabularInline):
    model = Collection
    extra = 1
    fields = ('name', 'art_type', 'admin_url_html')
    readonly_fields = ('admin_url_html',)
    def thumb_admin(self, collection):
        images = collection.focused()
        retain = ''
        images = images[:2]
        for i in images :
            retain += i.thumb_admin()
        return retain
    thumb_admin.allow_tags = True

class ArtistAdmin(admin.ModelAdmin):
    actions = [approve, publish]
    inlines = (CollectionInline, UrlInline)
    list_filter = ('submission', 'active')
    search_fields = ['firstname', 'lastname']    
    def save_model(self, request, obj, form, change):
        obj.save()
        
        if obj.pk :
            return True
        artist = Artist.objects.get(pk=obj.pk)
        if (change and artist.submission):
            if (artist.active == False and obj.active):
                _approve(obj)
            if (artist.approved == False and obj.approved):
                _publish(obj)
            
	
admin.site.register(Artist, ArtistAdmin)


# Collection
class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ImageAdmin.fields
    readonly_fields = ImageAdmin.readonly_fields
	
# Import Image Action
def import_images(self, request, queryset):
	for obj in queryset:
		num = load_image(obj, INDIE_BOX)
		obj.active = 1
		obj.save()
	self.message_user(request, _("You have imported %d images into %s ") % (num, obj.name))
	
import_images.short_description = _("Import Image")


def load_image(collection, folder):
	os.chdir(folder)
	files = glob.glob("*.*")
	for file in files:
		i = Image()
		i.collection = collection
		i.save()
		
		fname = folder + file.encode('ascii', 'ignore')
		
		f = File(open(fname))
		i.photo.save(file, f, save=False)
		name = f.name
		i.name = file[:-4]
		i.save()
		default_storage.delete(f)
	return len(files)
		
def _create_post(c, title):
    # Wordpress Post
	url = 'http://'+ site.domain
	
	images = c.images()[:15]
	content = render_to_string('blog/post_gallery.html', {'artist':c.artist, 'collection':c, 'images':images, 'url':url })
	
	post = Post(post_title=title, post_name=defaultfilters.slugify(title), post_content=content, post_author=2)
	gmt_time = datetime.fromtimestamp(time.mktime(time.gmtime()))
	post.post_date_gmt = gmt_time
	post.post_modified_gmt = gmt_time
	post.save()
	
	relation = Relation(object_id=post.pk, term_taxonomy_id=4)
	relation.save()
	
	# Post's tags
	post.add_tag(c.artist.__unicode__())
	for art_type in c.artist.art_types.all():
		post.add_tag(art_type.name)
	
	# Active artist
	c.artist.active = 1
	c.artist.save()
	return len(images)
		
# Create Post Action
def create_post(self, request, queryset):
    for c in queryset:
        count = _create_post(c, 'New Gallery for %s' % c.artist)

    self.message_user(request, _("You have create a post with %d images into %s ") % (count, c.name))
		
create_post.short_description = _("Create a Post")



class CollectionAdmin(admin.ModelAdmin):
    actions = [import_images, create_post]
    fields = ['name', 'art_type', 'artist', 'artist_admin_url']
    readonly_fields = ['artist_admin_url']
    inlines = (ImageInline,)
    def artist_admin_url(self, collection):
        return collection.artist.admin_url_html()
    artist_admin_url.allow_tags = True
    raw_id_fields = ("artist",)


admin.site.register(Collection, CollectionAdmin)



