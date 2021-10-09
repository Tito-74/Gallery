from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index,name = 'home'),
    url('^location/',views.location,name = 'location'),
    url('^search/',views.search_results,name = 'search'),
]