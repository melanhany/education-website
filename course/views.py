from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .serializers import ModuleSerializer, ModuleImageSerializer, ModuleFileSerializer, TestSerializer, QuestionSerializer, AnswerSerializer
from .models import Module, ModuleImage, ModuleFile, Test, Question, Answer

class ModuleViewSet(ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class ModuleImageViewSet(ModelViewSet):
    serializer_class = ModuleImageSerializer

    def get_serializer_context(self):
        return {'module_id': self.kwargs['module_pk']}

    def get_queryset(self):
        return ModuleImage.objects.filter(module_id=self.kwargs['module_pk'])
    
class ModuleFileViewSet(ModelViewSet):
    serializer_class = ModuleFileSerializer

    def get_serializer_context(self):
        return {'module_id': self.kwargs['module_pk']}

    def get_queryset(self):
        return ModuleFile.objects.filter(module_id=self.kwargs['module_pk'])
    
class AnswerViewSet(ModelViewSet):
    serializer_class = AnswerSerializer

    def get_serializer_context(self):
        return {'question_id': self.kwargs['question_pk']}

    def get_queryset(self):
        return Answer.objects \
                .filter(question_id=self.kwargs['question_pk'])

class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer

    def get_serializer_context(self):
        return {'test_id': self.kwargs['test_pk']}

    def get_queryset(self):
        return Question.objects \
                .filter(test_id=self.kwargs['test_pk'])

class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    