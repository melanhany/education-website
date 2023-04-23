from django.urls import path, include
from rest_framework_nested import routers
from .import views

router = routers.DefaultRouter()
router.register('modules', views.ModuleViewSet, basename="module")
router.register('tests', views.TestViewSet, basename="test")

module_router = routers.NestedDefaultRouter(router, 'modules', lookup='module')
module_router.register('images', views.ModuleImageViewSet, basename='module-images')
module_router.register('files', views.ModuleFileViewSet, basename='module-files')

test_router = routers.NestedDefaultRouter(router, 'tests', lookup='test')
test_router.register('questions', views.QuestionViewSet, basename='test-questions')
question_router = routers.NestedDefaultRouter(test_router, 'questions', lookup='question')
question_router.register('answers', views.AnswerViewSet, basename='question-answers')

urlpatterns = router.urls + module_router.urls + test_router.urls + question_router.urls