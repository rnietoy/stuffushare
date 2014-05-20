from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.views import HomeView
from user.views import LoginView, RegisterView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login/?$', LoginView.as_view(), name='login'),
    url(r'^register/?$', RegisterView.as_view(), name='register'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
