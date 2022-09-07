from django.shortcuts import render, redirect
from django.contrib.auth import login ,logout , authenticate
from django.contrib import messages
from .models import *
from .forms import *
from .serializers import *
from rest_framework import generics
from django.http import HttpResponse

def home(request):
    #post = Post.objects.filter(status = True)
    post_count = Post.objects.filter(status = True).count()
    answer = answers.objects.filter(staus = True)
    return render(request, 'chatapp/index.html',{'answer': answer, 'post_count': post_count})

def details_post(request, pk):
    post = answers.objects.filter(question = pk)
    return render(request, 'chatapp/details_post.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST , request.FILES)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('home')
        
    form = CreatePost()    
    return render(request, 'chatapp/add_discussion.html', {'form': form})

def admin_approve(request):
    post_list = Post.objects.all().order_by('-date_asked')
    if request.user.is_superuser:
        if request.method == 'POST':
            id_list = request.POST.getlist('boxes')
            post_list.update(status = False)
            for x in id_list:
                Post.objects.filter(pk = int(x)).update(status= True)
            messages.success(request, ('Approved'))
            return redirect('home')
        else:
            return render(request,'chatapp/approve.html',{'post_list':post_list})
    else:
        messages.success(request, ('you are not a super user!'))
        return redirect('home')

def admin_approve_answer(request):
    answer_list = answers.objects.all().order_by('-ate_answered')
    if request.user.is_superuser:
        if request.method == 'POST':
            id_list = request.POST.getlist('boxes')
            answer_list.update(staus = False)
            for x in id_list:
                answers.objects.filter(pk = int(x)).update(staus= True)
            messages.success(request, ('Approved'))
            return redirect('home')
        else:
            return render(request,'chatapp/approve_answer.html',{'answer_list':answer_list})
    else:
        messages.success(request, ('you are not a super user!'))
        return redirect('home')

def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form)
            user = form.save()
            Users.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    
    return render(request, 'chatapp/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
    return redirect('home')

def signout(request):
    logout(request)
    return redirect('home')


# API views

class List_view(generics.ListAPIView):
    queryset= Post.objects.all()
    serializer_class = list_post