from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uphero.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^tinymce/', include('tinymce.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    # url(r'^ajax_search/',include('ajax_search.urls')),
    url(r'^uphero/', include('ktv.urls'))
)













