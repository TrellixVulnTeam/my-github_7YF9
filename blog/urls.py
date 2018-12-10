from django.conf.urls import url
from blog.views import PostLV, PostDV, PostAV, PostYAV, PostMAV, PostDAV, PostTAV # import * 는 지양하세요.
app_name = 'blog'
urlpatterns = [
    url(r'^$', PostLV.as_view(), name='index'), # "blog:index"
    url(r'^post/$', PostLV.as_view(), name='post_list'),
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),
    url(r'^tag/$',TagTV.as_view(),name='tag_cloud'),
    
]
