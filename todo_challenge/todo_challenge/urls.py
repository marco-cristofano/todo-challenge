from django.contrib import admin
from django.urls import (
    include,
    path
)
from rest_framework import routers

from to_do.api.to_do import TodoViewSet

app_name = 'api'
router = routers.SimpleRouter()
router.register('to_do', TodoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))

]
