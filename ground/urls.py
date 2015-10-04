from django.conf.urls import include, url
from django.contrib import admin
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
=======
>>>>>>> origin/master


urlpatterns = [
    # Examples:
    # url(r'^$', 'ground.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^printo-app/',include('printo_app.urls')),
<<<<<<< HEAD
    # url(r'^api/',include('api.urls')),
    # url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^accounts/', include('allauth.urls')),
    # url(r'^printo/', include('printo.urls')),
    url(r'^admin/', include(admin.site.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
    url(r'^api/',include('api.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^printo/', include('printo.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
>>>>>>> origin/master
