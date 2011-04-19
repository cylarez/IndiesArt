from django.conf.urls.defaults import *
from account.views import *

urlpatterns = patterns('account.views',
	url(r'^submission/list$', 'submissionList'),
	url(r'^submission/new$', 'submissionNew'),
)
