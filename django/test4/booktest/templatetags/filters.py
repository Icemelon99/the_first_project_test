from django.template import Library

register = Library()

@register.filter
def mod(num):
	return num*5