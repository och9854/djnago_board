from django.shortcuts import render, redirect, get_object_or_404
# get_object_or_404: pk값을 이용해 객체를 호출하고, 없다면 404error를 render한다.
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm

# Create your views here.


def home(request):
    # 2-2. QuerySet을 통해 Blog() Object들을 추출
    # DB에서 저장된 블로그 객체들을 가지고 오는 코드

    # 블로그 객체들을 전부 가져오기 with dictionary 형태
    # posts = Blog.objects.all()

    # 원하는 블로그 객체만 filter해서 가져오기
    posts = Blog.objects.filter().order_by('date')
    return render(request, 'index.html', {'posts': posts})  # 블로그 글들의 목록을 전송

# 1. 블로그 글 작성 html을 보여주는 함수


def new(request):
    return render(request, 'new.html')

# 블로그 글을 "저장"해주는 함수


def create(request):
    if (request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()  # get current time
        post.save()
    return redirect('home')  # home으로 재이동

# 매우중요:
# 장고는 사용자로부터 입력을 받을 url이 있으면 한 url에서 GET, POST 요청을 모두 처리할 수 있게 할 수 있다.
# GET: 새 글 작성하기   (=입력값을 받을 수 있는 html을 갖다줘야함)
# POST: 새 글 생성하기  (=입력 내용을 DB에 저장)


def formcreate(request):
    if request.method == 'POST':
        # 입력내용을 DB에 저장
        form = BlogForm(request.POST)  # form을 만들어서, request에 담긴 내용을 받을수 있도록함
        # 입력값 검사: 자동으로 해줌
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        # 입력을 받을 html 전달
        form = BlogForm()

    return render(request, 'form_create.html', {'form': form})
    # render 3rd argument -> views.py 내의 데이터를 html에 넘겨줄 수 있음
    # 단, "딕셔너리 자료형"일 때만 가능하다.


def modelformcreate(request):
    if request.method == 'POST' or request.method == "FILES":
        # 입력내용을 DB에 저장
        # form을 만들어서, request에 담긴 내용을 받을수 있도록함
        form = BlogModelForm(request.POST, request.FILES)
        # 입력값 검사: 자동으로 해줌
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        # 입력을 받을 html 전달
        form = BlogModelForm()

    return render(request, 'form_create.html', {'form': form})


# Detail page view
def detail(request, blog_id):
    # blog_id 번째 블로그 글을 DB로부터 가지고 와서
    # blog_id 번째 블로그 글을 detail.html로 render 하는 코드
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    comment_form = CommentForm()

    return render(request, 'detail.html', {'blog_detail': blog_detail, "comment_form": comment_form})


def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        # 지금 저장하면 안됨! because: 어떤 blog post에 해당하는 건지 모르기 때문에!
        finished_form = filled_form.save(commit=False)  # 저장(commit)을 일시정지 시킴
        finished_form.post = get_object_or_404(Blog, pk=blog_id)  # post id를 받음
        finished_form.save()  # 이제 저장한다.

    return redirect('detail', blog_id)  # blog_id를 갖는 detail page로 redirect!
# 댓글 목록들을 보여주는 함수 작성 예정
