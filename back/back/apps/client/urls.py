from django.urls.conf import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(
    r"clients",
    views.ClientViewSet,
)
router.register(
    r"particular-clients",
    views.ParticularClientViewSet,
)
router.register(
    r"countries",
    views.CountryViewSet,
)

urlpatterns = [
    path(
        "",
        include(router.urls),
    ),
]
