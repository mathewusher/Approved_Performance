from django.conf.urls import patterns, include, url
from Amazon import views
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Approved_Performance.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
)
