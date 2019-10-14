from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    url(r'^$',views.pictures_of_day,name='picturesToday'),

    url(r'^search/', views.search_results, name='search_results'),
    url(r'^onepic/(\d+)',views.onepic,name ='onepic')
    # url(r'^location/(\d+)', views.filter_by_location, name = 'filter_by_location'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
