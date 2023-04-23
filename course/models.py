from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator

class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    last_tested = models.DateField(null=True, blank=True)
    test_result = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(1)])
    
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']

class Module(models.Model):
    name = models.CharField(max_length=255, default='example module')
    text = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class ModuleImage(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='course/images')


class ModuleFile(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='course/files')

class Test(models.Model):
    name = models.CharField(max_length=255)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='tests')

class Question(models.Model):
    description = models.CharField(max_length=255)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')

class Answer(models.Model):
    description = models.CharField(max_length=255)
    correction = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')