from django.conf.urls import patterns, url

from ktv import views

urlpatterns = patterns('',
                       # url(r'^$', views.detail_page, name='detail_page'),
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       # url(r'^(?P<ktv_id>\d+)/$', views.detail, name='detail')
                       url(r'(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail')
)




















