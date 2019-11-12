from rest_framework.routers import SimpleRouter
from .views import BookOperations

simpleRouter = SimpleRouter()

simpleRouter.register('book',BookOperations)

urlpatterns = simpleRouter.urls