from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Advance Django Project",
      default_version='v1',
      description="Bigdeli Advance Django Project",
    #   terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="bahmanpn@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), # for better experience to authentication and login in browser with django api view.
    path('accounts/', include("account_module.urls")),
    path('blog/', include("blog_module.urls",namespace='blog_module')),
    path('api-docs/', include_docs_urls(title='api sample')), # pip install coreapi +add configs in settings and add this for documentation to have simple documenation.
    
    # api documents endpoints
    path('swagger/output.json', schema_view.without_ui(cache_timeout=0), name='schema-json'), # for download api document with (json or yaml)formats we want.
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)