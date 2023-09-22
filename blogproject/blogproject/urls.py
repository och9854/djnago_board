"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogapp import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name='home'),

    # 1. html form을 이용해 블로그 객체만들기
    path("new/", views.new, name='new'),
    path("create/", views.create, name='create'),

    # 2. django form을 이용해 블로그 객체만들기
    path("formcreate/", views.formcreate, name='formcreate'),
    # 3. django model form을 이용해 블로그 객체만들기
    path("modelformcreate/", views.modelformcreate, name='modelformcreate'),


    # detail page 구현
    # 127.0.0.1:8000/detail/1
    # 127.0.0.1:8000/detail/2
    # 127.0.0.1:8000/detail/3
    # 127.0.0.1:8000/detail/4
    # 위와 같이 설계하기 위해서는 url 호출시 detail + 순서 키가 필요하다.
    path('detail/<int:blog_id>', views.detail, name='detail')
    # blog_id: detail이라는 함수에 인자로 넘길 변수값
]
