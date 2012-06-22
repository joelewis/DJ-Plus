from django.conf.urls import *
from DJPlus.models import Entry, Category
from django.views.generic import YearArchiveView
from datetime import datetime
from tagging.models import Tag


entry_info_dict = {
	'queryset': Entry.objects.all(),
	'date_field': 'pub_date',
	'extra_context' : {"month_list" : Entry.objects.filter().dates('pub_date','month'),
					   "category_list" : Category.objects.all(),
					   "tag_list" : Tag.objects.all()}
	}

urlpatterns = patterns('',
	url(r'^$', 'django.views.generic.date_based.archive_index',entry_info_dict,name='DJPlus_entry_archive_index'),
	url(r'^(?P<year>\d{4})/$',YearArchiveView.as_view(queryset=Entry.objects.all(),date_field='pub_date'),name='DJPlus_entry_archive_year'),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$','django.views.generic.date_based.archive_month',entry_info_dict,'DJPlus_entry_archive_month'),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$','django.views.generic.date_based.archive_day',entry_info_dict),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$','django.views.generic.date_based.object_detail',entry_info_dict,'DJPlus_entry_detail'),
	)
