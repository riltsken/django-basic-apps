from django.conf.urls.defaults import *
from django.conf import settings

BLOG_BASE_TEMPLATE = settings.BLOG_BASE_TEMPLATE

urlpatterns = patterns('basic.blog.views',
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        view='post_detail',
		kwargs={'extra_context': {'base_template': BLOG_BASE_TEMPLATE}},
        name='blog_detail'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/$',
        view='post_archive_day',
		kwargs={'extra_context':  {'base_template': BLOG_BASE_TEMPLATE}},
        name='blog_archive_day'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
        view='post_archive_month',
		kwargs={'extra_context':  {'base_template': BLOG_BASE_TEMPLATE}},
        name='blog_archive_month'
    ),
    url(r'^(?P<year>\d{4})/$',
        view='post_archive_year',
		kwargs={'extra_context':  {'base_template': BLOG_BASE_TEMPLATE}},
        name='blog_archive_year'
    ),
    url(r'^categories/(?P<slug>[-\w]+)/$',
        view='category_detail',
		kwargs={'extra_context':  {'base_template': BLOG_BASE_TEMPLATE}},
        name='blog_category_detail'
    ),
    url (r'^categories/$',
        view='category_list',
		kwargs={'extra_context':  {'base_template': BLOG_BASE_TEMPLATE}},
        name='blog_category_list'
    ),
    url(r'^tags/(?P<slug>[-\w]+)/$',
        view='tag_detail',
		kwargs={'extra_context':  {'base_template': BLOG_BASE_TEMPLATE}},
        name='blog_tag_detail'
    ),
    url (r'^search/$',
        view='search',
		kwargs={'extra_context':  {'base_template': BLOG_BASE_TEMPLATE}},
        name='blog_search'
    ),
    url(r'^page/(?P<page>\d+)/$',
        view='post_list',
		kwargs={'extra_context':  {'base_template': BLOG_BASE_TEMPLATE}},
        name='blog_index_paginated'
    ),
    url(r'^$',
        view='post_list',
		kwargs={'extra_context':  {'base_template': BLOG_BASE_TEMPLATE}},
        name='blog_index'
    ),
)
