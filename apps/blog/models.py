from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.template import defaultfilters
from indiesart.settings_local import *

class Post(models.Model):
	ID	= models.AutoField(primary_key=True)
	post_author = models.IntegerField(verbose_name=_('post_author_id'))
	post_date = models.DateTimeField('Date Created', editable = False, auto_now_add=True)
	post_date_gmt = models.DateTimeField('Date Created GMT', editable = False)
	post_content = models.TextField(verbose_name=_("Content"))
	post_title = models.CharField(max_length=150, verbose_name=_("Title"))
	post_name = models.SlugField(max_length=200, verbose_name=_("Name"))
	post_modified = models.DateTimeField('Date Created', editable = False, auto_now_add=True)
	post_modified_gmt = models.DateTimeField('Date Created GMT', editable = False)
	post_excerpt = models.TextField(default='', blank=True)
	post_status =  models.CharField(max_length=150, default="publish")
	to_ping = models.TextField(default='', blank=True)
	pinged = models.TextField(default='', blank=True)
	post_content_filtered = models.TextField(default='', blank=True)
	def url(self):
		return  '%s?p=%d' % (BLOG_URL, self.ID)
	def add_tag(self, tag):
		slug = defaultfilters.slugify(tag)
		test_term = Term.objects.filter(slug=slug)
		if len(test_term):
			term = test_term[0]
			tax = Taxonomy.objects.get(term_id=term.term_id)
		else :
			term = Term(name=tag)
			term.slug = slug
			term.save()
			tax = Taxonomy(term_id=term.term_id, taxonomy='post_tag')
		test_relation = Relation.objects.filter(object_id=self.pk, term_taxonomy_id=tax.term_taxonomy_id)
		if len(test_relation) == 0:
			tax.count = tax.count + 1
			tax.save()
			relation = Relation(object_id=self.ID, term_taxonomy_id=tax.term_taxonomy_id)
			relation.save()
	def __unicode__(self):
		return self.post_title
	class Meta:
		db_table = u'wp_posts'
		ordering = ["-ID"]
		
class Relation(models.Model):
	object_id = models.IntegerField()
	term_taxonomy_id = models.IntegerField()
	term_order = models.IntegerField(default=0)
	class Meta:
		db_table = u'wp_term_relationships'
		
class Taxonomy(models.Model):
	term_taxonomy_id = models.AutoField(primary_key=True)
	term_id = models.IntegerField()
	taxonomy = models.CharField(max_length=150)
	description = models.TextField(default='')
	parent = models.IntegerField(default=0)
	count = models.IntegerField(default=0)
	class Meta:
		db_table = u'wp_term_taxonomy'
	
class Term(models.Model):
	term_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150, verbose_name=_("Slug"))
	term_group = models.IntegerField(default=0)
	class Meta:
		db_table = u'wp_terms'
	
	