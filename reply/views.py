from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from board.models import Post
from reply.forms import ReplyForm
from reply.models import Reply

@login_required(login_url='/user/login')
def create(request, bid):
    # if request.method == "GET":
    #     replyForm = ReplyForm()
    #     return render(request, 'reply/create.html', {'replyForm': replyForm})
    if request.method == "POST":
        replyForm = ReplyForm(request.POST)
        if replyForm.is_valid():
            reply = replyForm.save(commit=False)

            # 사용자 지정
            reply.writer = request.user

            post = Post()
            post.id = bid
            reply.post = post
            reply.save()
        return redirect('/reply/read/' + str(reply.id))


def list(request):
    replys = Reply.objects.all().order_by('-id')

    return render(request, 'reply/list.html', {'replys':replys})

def read(request, rid):
    reply = Reply.objects.get(id=rid)

    return render(request, 'reply/read.html', {'reply':reply})


@login_required(login_url='/user/login')
def delete(request, rid):
    reply = Reply.objects.get(id=rid)

    if request.user != reply.writer:
        return redirect('/reply/read/'+str(rid))

    reply.delete()
    return render(request, 'reply/deleteUpdate.html')





#     def deleteGet(request, bid):
#         post = Post.objects.get(id=bid)
#         if request.user != post.writer:
#             return redirect('/board/read/' + str(bid))
#
#         post.delete()
#
#         return redirect('/board/list')

def update(request, rid):
    reply = Reply.objects.get(id=rid)
    if request.method == "GET":
        replyForm = ReplyForm(instance=reply)
        return render(request, 'reply/create.html', {'replyForm': replyForm})
    elif request.method == "POST":
        replyForm = ReplyForm(request.POST, instance=reply)
        if replyForm.is_valid():
            reply = replyForm.save(commit=False)
            reply.save()
        return redirect('/reply/update/' + str(reply.id))


