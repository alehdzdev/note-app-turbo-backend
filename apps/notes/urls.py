# Third Party
from rest_framework.routers import DefaultRouter

# Local
from notes.views import NoteViewSet

router = DefaultRouter()
router.register("", NoteViewSet, basename="notes")

urlpatterns = router.urls
