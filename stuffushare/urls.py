from django.conf.urls import patterns, include, url

from django.contrib import admin

from main.views import HelloWorldView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HelloWorldView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
