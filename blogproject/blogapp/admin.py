from django.contrib import admin
from .models import Blog, Comment

# Register your models here.
admin.site.register(Blog)  # admin site에서 Blog 객체를 확인할 수 있게 해줌
admin.site.register(Comment)  # admin site에서 admin 객체를 확인할 수 있게 해줌
