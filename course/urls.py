from django.urls import path, include
from rest_framework_nested import routers
from .import views

router = routers.DefaultRouter()
router.register('modules', views.ModuleViewSet, basename="module")

module_router = routers.NestedDefaultRouter(router, 'modules', lookup='module')
module_router.register('images', views.ModuleImageViewSet, basename='module-images')
module_router.register('files', views.ModuleFileViewSet, basename='module-files')


urlpatterns = router.urls + module_router.urls