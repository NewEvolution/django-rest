from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter


# Create a router and register the viewsets.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# API urls are determined by the router.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls'))
]
