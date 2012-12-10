from django.conf.urls.defaults import *
from django.contrib import admin
from settings_local import *
from django.views.generic.simple import redirect_to

from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from main.models import *


sitemaps = {
    'artist': GenericSitemap({'queryset': Artist.objects.all(), 'date_field': 'modified'}),
    'collection': GenericSitemap({'queryset': Collection.objects.all(), 'date_field': 'modified'}),
    'images': GenericSitemap({'queryset': Image.objects.all() ,'date_field': 'modified'}),
}


admin.autodiscover()

urlpatterns = patterns('',
	
    # Admin doc
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin
    (r'^admin/', include(admin.site.urls)),
    
    # Main App
    (r'^main/', include('main.urls')),
    
    # Blog App
    (r'^blog/', include('blog.urls')),
    
     # Account App
    (r'^account/', include('account.urls')),
    
    # Account App
    (r'^mobile/', include('mobile.urls')),

    # Home page
    (r'', include('main.urls')),
    
	url(r'^search$', redirect_to, {'url':'/artists/page-1'}),
	
	# Sitemap
	(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})

)
