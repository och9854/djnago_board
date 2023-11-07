from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)  # title의 최대 길이를 200자로 제한
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    # auto_now_add: 자동으로 지금 시간을 추가
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # !매우 중요! 어떤 게시물에 달려있는 댓글인지를 알 수 있는, 댓글이 달린 게시물에 쓰이는 foreign key
    # CASCADE: post가 삭제될 때 -> 해당 comment도 함께 삭제됨
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.comment
