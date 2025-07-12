from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), # for better experience to authentication and login in browser with django api view.
    path('accounts/', include("django.contrib.auth.urls")),
    path('blog/', include("blog_module.urls",namespace='blog_module')),
    path('api-docs/', include_docs_urls(title='api sample')), # pip install coreapi +add configs in settings and add this for documentation to have simple documenation.
    
]


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)