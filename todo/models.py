from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)  # varcher(100) not null
    text = models.TextField(blank=True)  # 可以為空內容
    created = models.DateField(auto_now_add=True)
    date_completed = models.DateTimeField(
        blank=True, null=True
    )  # 內容物可為空，物件也可以為空
    important = models.BooleanField(default=False)

    # user_id綁定todo_id   ForeignKey進行外界關聯,自動建立關聯關係***
    # todo_id<=>user_id
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}-[{self.created}-{self.title}-{self.user}]"
