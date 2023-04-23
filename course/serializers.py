from rest_framework import serializers
from .models import Module, ModuleImage, ModuleFile, Test, Question, Answer

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


class AnswerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        question_id = self.context['question_id']
        return Answer.objects.create(question_id=question_id, **validated_data)

    class Meta:
        model = Answer
        fields = ['id', 'description', 'correction']

class QuestionSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        test_id = self.context['test_id']
        return Question.objects.create(test_id=test_id, **validated_data)

    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['id', 'description', 'answers']

class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Test
        fields = ['id', 'name', 'module', 'questions']