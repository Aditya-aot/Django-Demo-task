from django.db import models
from django.conf import settings
from django.contrib.auth.models import  User, auth
# Create your models here.

class Question_Asked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , null= True  )
    content = models.TextField()
    message = models.TextField( null= True)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)



class Answer_model(models.Model):
    chat = models.ForeignKey(Question_Asked ,related_name="answer", on_delete= models.CASCADE)
    answer = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE , null= True  )
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __aiter__(self):
        return "%s - %s" % (self.chat.content , self.name)
