from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register("reports", ReportItemsViewSet, basename="reports")
router.register("blocked_resources", BlockedResourcesViewSet, basename="blocked_resources")
urlpatterns = router.urls
