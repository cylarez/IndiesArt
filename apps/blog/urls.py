from django.conf.urls.defaults import *
from blog.views import *


urlpatterns = patterns('blog.views',

	url(r'^post/(?P<collection_id>\d+)', post, name='post')

)
