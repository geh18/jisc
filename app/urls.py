from django.conf.urls import url

from .views import HomeView, SinglePostView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='app-home'),
    url(r'^post/(?P<pk>\d+)/$', SinglePostView.as_view(), name='app-single-post'),
]