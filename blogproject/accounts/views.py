from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.


def login(request):
    # POST 요청이 들어오면 로그인 처리를 해줌
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        # !! 중요 !! djnago에서는 DB에 저장된 회원 여부를 판단해주는 내장 기능이 있다.
        '''
        - 입력 ID, PW를 토대로 검사를 해줌 
        - 이미 저장되어 있는 회원이라면: 저장된 User() 객체를 반환 -> django는 내장된 User()가 있다.
        - 그렇지 않다면: None을 반환한다.
        '''
        user = auth.authenticate(
            request, username=userid, password=pwd)

        if user is not None:
            auth.login(request, user)  # request, User() 객체를 받는다.
            return redirect('home')  # home으로 이동
        else:
            return render(request, 'bad_login.html')

    # GET 요청이 들어오면 login form을 달고있는 login.html을 띄워주는 역할을 함
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
