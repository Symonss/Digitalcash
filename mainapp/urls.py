
from django.urls import path
from mainapp import views
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', views.home, name='home'),
    path('opportunities', views.post_list, name='opportunities_list'),
    url(r'^opportunities/(?P<post>[-\w]+)/$', views.post_detail_view, name='opportunity_detail_view'),
    
]

# serving media files only on debug mode
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]