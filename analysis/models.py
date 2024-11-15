from django.db import models
GENDER_TYPE=(('Male','Male'),('Female','Female'),)
# Create your models here.
class SocialData(models.Model):
    gender=models.CharField(max_length=50,choices=GENDER_TYPE)
    age=models.IntegerField()
    salary=models.IntegerField()
    purchase=models.BooleanField()