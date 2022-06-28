import os

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

from board.forms import PostForm
from board.models import Post
from config import settings
from reply.forms import ReplyForm

@login_required(login_url='/user/login')
def like(request, bid):
    post = Post.objects.get(id=bid)

    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
        return JsonResponse({'message': 'deleted', 'like_cnt': post.like.count()})
    else:
        post.like.add(request.user)
       # JsonResponse=> 비동기 통신
        return JsonResponse({'message':'added','like_cnt': post.like.count()})

def mainPage(request):
    return render(request, 'board/index.html')


@login_required(login_url='/user/login')
def create(request):
    if request.method == "GET":
        postForm = PostForm()
        context = {'postForm': postForm}
        return render(request, 'board/create.html', context)
    elif request.method == "POST":
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.writer = request.user
            #######
            post.image = request.FILES.get('image', None)
            post.save()

            ########
            return redirect('/board/read/' + str(post.id))


def listGet(request):
    posts = Post.objects.all().order_by('-id')

    context = {'posts': posts}

    return render(request, 'board/list.html', context)


def readGet(request, bid):

    # select_related => 정방향
    # prefetch_related => 역방향
    post = Post.objects.prefetch_related('reply_set').get(id=bid)

    replyForm = ReplyForm()
    context = {'post': post, 'replyForm': replyForm}

    return render(request, 'board/read.html', context)

@login_required(login_url='/user/login')
def deleteGet(request, bid):
    post = Post.objects.get(id=bid)
    if request.user != post.writer:
        return redirect('/board/read/'+str(bid))

    post.delete()

    return redirect('/board/list')

@login_required(login_url='/user/login')
def update(request, bid):
    post = Post.objects.get(id=bid)

    if request.user != post.writer:
        return redirect('/board/read/' + str(post.id))

    if request.method == "GET":
        postForm = PostForm(instance=post)
        context = {
            'post': post
        }
        return render(request, 'board/update.html', context)
    elif request.method == "POST":
        postForm = PostForm(request.POST, instance=post)
        if postForm.is_valid():

            post = postForm.save(commit=False)

            post.image = request.FILES.get('image', None)
            post.save()
        return redirect('/board/read/' + str(post.id))
