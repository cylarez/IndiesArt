from django.conf.urls.defaults import *
from mobile.views import *

urlpatterns = patterns('mobile.views',
    url(r'^main$', 'main'),
    url(r'^discover$', 'discover'),
    url(r'^artist/(?P<artist_id>\d+)', artist, name='artist'),
)
