from rest_framework import serializers
from .models import Module, ModuleImage, ModuleFile

class ModuleImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        module_id = self.context['module_id']
        return ModuleImage.objects.create(module_id=module_id, **validated_data)

    class Meta:
        model = ModuleImage
        fields = ['id', 'image']

class ModuleFileSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        module_id = self.context['module_id']
        return ModuleFile.objects.create(module_id=module_id, **validated_data)

    class Meta:
        model = ModuleFile
        fields = ['id', 'file']

class ModuleSerializer(serializers.ModelSerializer):
    images = ModuleImageSerializer
    files = ModuleFileSerializer
    class Meta:
        model = Module
        fields = ['id', 'name', 'text', 'images', 'files']