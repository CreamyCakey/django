from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Instruction(models.Model):
    instruction_id = models.AutoField(primary_key=True)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    instruction = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.instruction