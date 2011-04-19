from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='clean_keywords')
@stringfilter
def clean_keywords (string): 
	string = string.replace(" > ", ",")
	string = string.replace(" &gt; ", ",")
	return string
