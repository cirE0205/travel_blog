from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from index.views import index_1_views, blog_post_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', index_1_views),
    url(r'^index/$', index_1_views),
    url(r'^blog-post/$', blog_post_views),


]


# urlpatterns += [
#
#     url(r'^index/$', index_views),
# ]