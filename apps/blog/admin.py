from blog.models import *
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
import datetime
from django.template import defaultfilters

# Create Tweet
def tweet(self, request, queryset):
	api = twitter.Api(username='indiesart', password='838dg34') 
	for p in queryset:		
		api.PostUpdate(p.post_title +' => '+ p.url())
	self.message_user(request, _("You have created %d tweets ") % len(queryset))
	
def fix(self, request, queryset):
	for p in queryset:
		d = p.post_date.day
		h = p.post_date.hour
		if (p.post_date.hour > 19) :
			d = d + 1
			h = h - 24
		p.post_date_gmt = datetime.datetime(p.post_date.year, p.post_date.month, d, h + 4, p.post_date.minute, p.post_date.second)
		
		
		d = p.post_modified.day
		h = p.post_modified.hour
		if (p.post_modified.hour > 19) :
			d = d + 1
			h = h - 24
		p.post_modified_gmt = datetime.datetime(p.post_modified.year, p.post_modified.month, d, h + 4, p.post_modified.minute, p.post_modified.second)
		p.post_name = defaultfilters.slugify(p.post_title)
		p.save()
	self.message_user(request, _("%d posts have been fixed! ") % len(queryset))
		
tweet.short_description = _("Create Tweet")

class PostAdmin(admin.ModelAdmin):
	actions = [tweet, fix]
	
admin.site.register(Post, PostAdmin)