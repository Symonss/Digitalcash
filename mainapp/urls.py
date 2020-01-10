
from django.urls import path
from mainapp import views
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', views.home, name='home'),
    path('opportunities', views.post_list, name='opportunities_list'),
    url(r'^opportunities/(?P<opp>[-\w]+)/$', views.opportunity_detail_view, name='opportunity_detail_view'),
    url(r'^stories/(?P<post>[-\w]+)/$', views.post_detail_view, name='story_detail_view'),
    path('management/',views.administration, name = 'admins'),
    path('ff/',views.ff, name = 'ff'),
    path('management/add/opportunity/',views.OppCreatView.as_view(),name = 'creat_opp'),
    path('management/add/category/',views.CatCreatView.as_view(),name = 'creat_cat'),
    path('update/<int:pk>/',views.OppUpdate.as_view(), name= 'opp_update'),
    
]

# serving media files only on debug mode
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]