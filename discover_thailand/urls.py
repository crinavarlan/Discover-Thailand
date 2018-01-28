"""discover_thailand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from accounts import views as accounts_views
from home import views as home_views
from contact import views as contact_views
from blog import views as blog_views
from about import views as about_views
from django.contrib import admin
from .settings import MEDIA_ROOT
from django.views.static import serve
from django.conf.urls import url, include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.get_home, name='home'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),

    # authentication url
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),

    # contact url
    url(r'^contact/$', contact_views.contact, name='contact'),

    # about url
    url(r'^about/$', about_views.about, name='about'),

    # blog url
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^blog/$', blog_views.post_list),
    url(r'^blog/(?P<id>\d+)/$', blog_views.post_detail),
    url(r'^blog/top', blog_views.top_posts),
    url(r'^post/new/$', blog_views.new_post, name='new_post'),
    url(r'^blog/(?P<id>\d+)/edit$', blog_views.edit_post),
]


