from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from apps.repocheck.urls import api_urls as repocheck__urls
from apps.user.urls import web_urls as user_web_urls


admin.site.site_header = "gitscore admin"
admin.site.site_title = "gitscore admin"
admin.site.index_title = "gitscore admin"

# swagger setup docs
schema_view = get_schema_view(openapi.Info(
        title="gitscore api",
        default_version='v1',
        description="gitscore api docs",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),)

api_patterns = []
web_patterns = []
web_patterns += user_web_urls

# API documentation only on debug
if settings.DEBUG:
    api_patterns += [re_path(r'^docs/$', schema_view.with_ui(
        'swagger', 
        cache_timeout=0,
    ), name='schema-swagger-ui')]

api_patterns += repocheck__urls

urlpatterns = [
    re_path('^admin/', admin.site.urls),
    # API
	re_path('^api/v1/', include(api_patterns)),
    # web
    re_path('', include(web_patterns)),
    # Social auth
    url(r'auth-social/', include('allauth.urls'))
]

if (settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

