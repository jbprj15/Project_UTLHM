from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # ADMIN PAGE
    url(r'^admin/', include(admin.site.urls)),
    
    # HOMEPAGE
    url(r'^$', 'utlhm.views.home', name='home'),
    
    # ABOUTUS 
    url(r'^aboutus$', 'utlhm.views.aboutus', name='aboutus'),
    
    # test 
    url(r'^test$', 'utlhm.views.test', name='test'),

)
    # Examples:
    # url(r'^$', 'utlhm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                                document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                                document_root=settings.MEDIA_ROOT)