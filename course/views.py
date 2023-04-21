from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ModuleSerializer, ModuleImageSerializer, ModuleFileSerializer
from .models import Module, ModuleImage, ModuleFile

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
    