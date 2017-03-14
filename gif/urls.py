from django.conf.urls import url
from . import views
from .models import Gif
urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^gifs.html',views.gifs,name="gif"),
     url(r'^0',views.PageRedirect,name="redirect"),
    url(r'^'+str(Gif.objects.count()+1),views.PageMoreRedirect,name="more_redirect"),
    url(r'^(?P<gif_id>[0-9]+)/$',views.detail,name="gif_detail")
]