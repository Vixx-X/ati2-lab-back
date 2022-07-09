from django.urls.conf import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(
    r"businesses",
    views.BusinessViewSet,
)
router.register(
    r"employee",
    views.EmployeeViewSet,
)
router.register(
    r"provider",
    views.ProviderViewSet,
)

urlpatterns = [
    path(
        "",
        include(router.urls),
    ),
]
