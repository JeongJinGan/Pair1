from django.db import models

# Create your models here.


class Todo(models.Model):
    # django에서 pk(id)는 자동으로 만들어준다.
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now=True)
