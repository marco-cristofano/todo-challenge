from django.contrib import admin
from django.urls import (
    include,
    path
)
from rest_framework import routers

from to_do.api.to_do import TodoViewSet
from user.api.user import CreateUserView

app_name = 'api'
router = routers.SimpleRouter()
router.register('to_do', TodoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('user/', CreateUserView.as_view(), name='user'),
]
