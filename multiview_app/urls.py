from django.conf.urls import url
from django.contrib.auth import views as auth_views

import views

urlpatterns = [
    url(
        r'^login/$', auth_views.login,
        {'template_name': 'multiview_app/login.html'},
        name='login',
    ),
    url(
        r'^logout/$',
        auth_views.logout,
        {'next_page': '/login/'},
        name='logout',
    ),
    url(r'^$', views.home, name='home'),
    url(r'^image_add/$', views.image_upload, name='image_upload'),
    url(r'^images/$', views.images, name='images')
]
