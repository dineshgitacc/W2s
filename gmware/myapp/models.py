from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

class CUser(User):
    score=models.IntegerField()
    
    # def __str__(self) -> str:
    #     return  