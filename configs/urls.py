"""resturant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
from resturant.authtoken_extention.api.viewsets import CustomObtainAuthToken
import debug_toolbar


urlpatterns = [
    path('api/__debug__/', include(debug_toolbar.urls)),
    path('api/admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/user/', include('resturant.user.urls')),
    path('', include('resturant.cart.urls'), name='cart'),
    path('api/food/', include('resturant.food.urls')),
    path('baton/', include('baton.urls')),
    path('api/token/', include('resturant.authtoken_extention.urls')),
]

# media and static

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# drf yasg doc

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="resturant API",
      default_version='v1',
      description="",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@resturant.com"),
   ),
   public=True,
)

urlpatterns += [
   re_path(r'^api/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^api/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^api/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]