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


INDIE_BOX = settings.MEDIA_ROOT +'indie_box/'

admin.site.register(ArtType)
admin.site.register(MediaType)
admin.site.register(UrlType)

# Images


class ImageAdmin(admin.ModelAdmin):
	list_display = ('name', 'thumb_admin')
	fields = ('thumb_admin', 'name', 'focused',)
	readonly_fields = ('thumb_admin',)

admin.site.register(Image, ImageAdmin)


# Artist
class UrlInline(admin.TabularInline):
	model = Url
	extra = 1

def approved(self, request, queryset):

	from django.core.mail import EmailMultiAlternatives
	from django.template.loader import render_to_string
	site = Site.objects.get(id=settings.SITE_ID)
	
	for artist in queryset:
		artist.active = 1
		artist.save()
		message_html = render_to_string('account/submission-email.html', {'artist': artist, 'url':site.domain})
		message_text = strip_tags(message_html)
        msg = EmailMultiAlternatives('Submission pre-approved', message_text, settings.EMAIL_HOST_USER, [artist.email])
        msg.attach_alternative(message_html, "text/html")
        msg.send()
	self.message_user(request, _("You have approved and sent the email to %s") % (artist.email))

class ArtistAdmin(admin.ModelAdmin):
	actions = [approved]
	inlines = (UrlInline,)
	
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
		
		
# Create Post Action
def create_post(self, request, queryset):
	site = Site.objects.get(id=settings.SITE_ID)
	#api = twitter.Api(username='indiesart', password='838dg34', access_token_key='oJsShRSGfFSjw0IxoznVCQ', access_token_secret='ISmrsNgNI3WqFYVRDqSumExx9QXRN9tZycCLHAbNg') 
	for c in queryset:
		# Wordpress Post
		url = 'http://'+ site.domain
		
		images = c.images()[:15]
		title = 'New Gallery for %s' % c.artist
		content = render_to_string('blog/post_gallery.html', {'artist':c.artist, 'collection':c, 'images':images, 'url':url })
		
		post = Post(post_title=title, post_name=defaultfilters.slugify(title), post_content=content, post_author=1)
		gmt_time = datetime.datetime.fromtimestamp(time.mktime(time.gmtime()))
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
		
		# Twitter
		#if (settings.SITE_ID == 1):
			#api.PostUpdate(title +' => '+ post.url())
		
		time.sleep(1)
	self.message_user(request, _("You have create a post with %d images into %s ") % (len(images), c.name))
		
create_post.short_description = _("Create a Post")

class CollectionAdmin(admin.ModelAdmin):
	actions = [import_images, create_post]
	inlines = (ImageInline,)

admin.site.register(Collection, CollectionAdmin)



