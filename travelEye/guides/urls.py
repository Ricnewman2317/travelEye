from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns =[
    url(r'^$', views.index_page, name='index'),
    url(r'login/$', views.login_view, name='login'),
    url(r'^guides/PointsOfInterest/$',views.PointsOfInterestList.as_view()),
    url(r'^guides/PointsOfInterest/(?P<pk>[0-9]+)/$', views.PointsOfInterestDetail.as_view()),
    url(r'^guides/Streets/$',views.StreetsList.as_view()),
    url(r'^guides/Streets/(?P<pk>[0-9]+)/$', views.StreetsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
