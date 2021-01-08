"""acme_bank_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
#from acme_bank_api import core_banking_system
from django.conf.urls import include, url
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="ACME Bank Pvt LTD.",
        default_version='v1',
        description="Owned by Shiva"
    ),
    validators=['flex', 'ssv'],
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('acme_bank_api.core_banking_system.urls')),
    #path('', include('acme_bank_api.users.urls')),
]

urlpatterns += [
    url(r'', include('acme_bank_api.core_banking_system.urls')),
    url(r'', include('acme_bank_api.users.urls')),
    #url(r'^api/core_banking_system/', include('acme_bank_api.core_banking_system.urls')),
    #url(r'^api/users/', include('acme_bank_api.users.urls')),

    url(r'^docs/swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=None),name='schema-json'),
    url(r'^docs/swagger/$', schema_view.with_ui('swagger', cache_timeout=None),name='schema-swagger-ui'),
    url(r'^docs/redoc/$', schema_view.with_ui('redoc', cache_timeout=None),name='schema-redoc'),

]

"""if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns """