from django.conf.urls.defaults import *
from main.views import *

urlpatterns = patterns('main.views',
	url(r'^$', 'index'),
	url(r'^artist/(?P<artist_id>\d+)', artist, name='artist'),
	url(r'^artists/page-(?P<num>\d+)', 'artists'),
	url(r'^collection/(?P<collection_id>\d+)[^/]+/page-(?P<num>\d{1})', collection),
	url(r'^collection/(?P<collection_id>\d+)', collection, {'num':1}),
	url(r'^image/(?P<image_id>\d+)', image, name='image'),
	url(r'^random$', 'random'),
	url(r'^mobile_data.json$', 'mobile_data'),
)
