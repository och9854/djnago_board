from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)  # title의 최대 길이를 200자로 제한
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)  # auto_now_add: 자동으로 지금 시간을 추가

    def __str__(self) -> str:
        return self.title