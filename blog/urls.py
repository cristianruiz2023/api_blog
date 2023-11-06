
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from categories.api.router import router_categories
from posts.api.router import router_posts
from comments.api.router import router_comments


schema_view = get_schema_view(
   openapi.Info(
      title="Medium API",
      default_version='v1',
      description="Practica de api rest",
      terms_of_service="codigofacilito.com",
      contact=openapi.Contact(email="admin@admin.py"),
      license=openapi.License(name="CodigoFacilito"),
   ),
   public=True,
   # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema_swagger_ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema_redoc_ui'),
    path('api/', include('users.api.router')),
    path('api/', include(router_categories.urls)),
    path('api/', include(router_posts.urls)),
    path('api/', include(router_comments.urls)),
    
]
