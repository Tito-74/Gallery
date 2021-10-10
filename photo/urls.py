from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$',views.index,name = 'home'),
    # url('^location/',views.post_location,name = 'location'),
    url('^search/',views.search_category,name = 'search'),
    url('^image/(?P<post_id>\d+)/$',views.post_properties, name='image'),
    url(r'^location/(?P<location>\w+)',views.post_location,name = 'location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)