from django.db import models

# Create your models here.
# null = True는 있어도 된다는 뜻 널이
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)
