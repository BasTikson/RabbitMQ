from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# router = routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),

    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
