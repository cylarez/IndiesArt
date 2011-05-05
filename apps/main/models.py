from django.db import models
from django.contrib.auth.models import User as DjangoUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.sitemaps import ping_google
from django.contrib.sites.models import Site
from django.core import urlresolvers
from main.thumbs import ImageWithThumbsField
import random, re, json, logging

site = Site.objects.get(id=settings.SITE_ID)

if site.id != 1 :
    logger = logging.getLogger(__name__)
    logFile = logging.FileHandler(settings.MAIN_DIR + 'logs')
    logger.addHandler(logFile)

class DefaultModel(models.Model):	
    created		= 	models.DateTimeField('Date Created', editable = True, auto_now_add=True)
    modified	= 	models.DateTimeField('Date Updated', editable = True, auto_now=True)
    active		= 	models.BooleanField(default=0)
    def url(self):
        return self.get_absolute_url()
    def get_absolute_url(self):
        className = self.__class__.__name__.lower()
        name = self.__unicode__()
        name = re.sub(r'[^a-z0-9-]+', '-', name.lower()).strip('-')
        return "/"+ className +"/"+ str(self.pk) +"-"+ name
    def pub_date(self):
        return self.created
    def admin_url(self):
        if self.pk == None :
            return False
        className = self.__class__.__name__.lower()
        return 'http://%s%s' % (site.domain, urlresolvers.reverse('admin:main_'+ className +'_change', args=(self.id,)))
    def admin_url_html(self):
        url = self.admin_url()
        if (url):
            return '<a href="%s">Update</a>' % url
        else :
            return ''
    admin_url_html.allow_tags = True
    class Meta:
        abstract = True
        ordering = ["-id"]
    def __unicode__(self):
        return self.name
   
class ArtType(DefaultModel):
	name = models.CharField(max_length=150, verbose_name=_("Art Type"))
	art_type = models.ForeignKey('ArtType', blank = True, null = True)
	def __unicode__(self):
		if self.art_type is None :
			return self.name
		else:
			return self.art_type.__unicode__() +" > "+ self.name
	def get_absolute_url(self):
		name = self.__unicode__()
		name = re.sub(r'[^a-z0-9-]+', '-', name.lower()).strip('-')
		return "/category/"+ str(self.pk) +"-"+ name
	def artists(self):
		self.artists = Artist.objects.filter(art_types=self.pk)
		return self.artists
	class Meta:
		db_table = u'main_art_type'

class Artist(DefaultModel):
    submission = models.BooleanField(default=0)
    approved = models.BooleanField(default=0)
    lastname = models.CharField(max_length=150, verbose_name=_("Lastname"), blank=True)
    firstname =  models.CharField(max_length=150, verbose_name=_("Firstname"))
    email = models.CharField(max_length=150, verbose_name=_("Email"))
    art_types = models.ManyToManyField(ArtType)
    bio = models.TextField(verbose_name=_("Biography"))
    bio_fr = models.TextField(verbose_name=_("Biography Fr"), blank=True)

    def urls(self):
        self.urls = Url.objects.filter(artist=self.pk)
        return self.urls
    def name(self):
        if self.lastname :
            return self.firstname +" "+ self.lastname
        else :
            return self.firstname	
    def __unicode__(self):
        return self.name()
    def collections(self):
        self.collections = []
        collections = Collection.objects.filter(artist=self.pk)
        for c in collections :
            c.images()
            self.collections.append(c)
        return self.collections
    def images(self, sample, toJson = False):
        self.images = []
        images = Image.objects.filter(collection__artist=self.pk).order_by('-focused', '-id')
        if toJson :
            for image in images :
                image = image.toJson()  
        if sample == False or len(images) < sample :
            sample = len(images)  
        self.images = images[:sample]
        return self.images
    def keywords(self):
        if self.lastname :
            return '%s,%s,%s' % (self.name(), self.firstname, self.lastname)
        else :
            return self.firstname
    def toJson(self, image = False):
        artist = {'id': self.pk, 'name': self.name(), 'firstname': self.firstname, 'submission': self.submission}
        if image :
            artist['image'] = image.photo.url_50x50.replace(' ', '%20')
        else :
            artist['images'] = self.images(False, True)
        return artist
    class Meta:
        ordering = ["-created"]

class UrlType(DefaultModel):
    name = models.CharField(max_length=150, verbose_name=_("Url Type"))
    class Meta:
		db_table = u'main_url_type'
	
class Url(DefaultModel):
    name = models.CharField(max_length=150, verbose_name=_("Url"))
    artist = models.ForeignKey(Artist)
    url_type = models.ForeignKey(UrlType)

class MediaType(DefaultModel):
	name = models.CharField(max_length=150, verbose_name=_("Media Type"))
	class Meta:
		db_table = u'main_media_type'
		
class Collection(DefaultModel):
    name = models.CharField(max_length=150, verbose_name=_("Collection Title"))
    art_type = models.ForeignKey(ArtType)
    artist = models.ForeignKey(Artist, related_name='Author')
    media_type = models.ForeignKey(MediaType, blank=True, null=True)
    def focused(self):
        images = Image.objects.filter(collection=self.pk, focused=1)
        for i in images :
            i.resize = (i.photo.width > 620)
        if (len(images) < 1) :
            images = Image.objects.filter(collection=self.pk)[:1]
        self.focused = images
        return images
    def images(self):
        images = Image.objects.filter(collection=self.pk).order_by('-focused')
        self.images = images
        return images
    def save(self, force_insert=False, force_update=False):
        super(Collection, self).save(force_insert, force_update)
        if (settings.SITE_ID == 1):
            try:
                ping_google('/sitemap.xml')
            except Exception:
                pass


class Piece(DefaultModel):
    name = models.CharField(max_length=255, blank=True, verbose_name=_("Piece Title"))
    focused = models.BooleanField(default=0)
    collection = models.ForeignKey(Collection)

class Image(Piece):
    def get_path(self, name):
        return 'image/%d/%d/%s' % (self.collection.artist.id, self.collection.id, name) 
    photo = ImageWithThumbsField(upload_to=get_path, sizes=((50,50),(200,200)))
    def file_name(self):
        tab = self.photo.name.split("/")
        return tab[len(tab)-1]
    def home_file_name(self):
        return '%shome_slide/%s' % (settings.MEDIA_URL, self.file_name())
    def main_url(self):
        return settings.MEDIA_URL + self.photo.name
    def toJson(self):
        return {'name': self.name, 'url':self.main_url().replace(' ', '%20'), 'url_200x200': self.photo.url_200x200.replace(' ', '%20')}
    def thumb_admin(self):
        if self.pk == None :
            return ''
        return '<img src="%s" style="padding:5px" alt="thumb" />' % (self.photo.url_200x200,)
    thumb_admin.allow_tags = True

class User(DjangoUser):
	favoris = models.ManyToManyField(Collection, blank=True, related_name='Favoris')