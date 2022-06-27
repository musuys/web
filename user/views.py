from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('/board/list')


def login(request):
    if request.method == "GET":
        loginForm = AuthenticationForm()
        return render(request, 'user/login.html', {'loginForm': loginForm})
    elif request.method == "POST":
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            auth_login(request, loginForm.get_user())
            return redirect('/board/list')



def signup(request):
    if request.method == "GET":

        #UserCreationForm 장고에서 제공하는 회원가입
        signupForm = UserCreationForm()
        return render(request, 'user/signup.html', {'signupForm': signupForm})

    elif request.method == "POST":
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid():
            user = signupForm.save(commit=False)
            user.save()
        return redirect('/user/login')


def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
        # 탈퇴후 로그아웃순으로 처리.
        # 먼저 로그아웃하면 해당 request 객체 정보가 없어져서 삭제가 안됨.
    return redirect('/user/login')


def update(request):
    if request.method == "POST":
        # updating
        user_change_form = UserChangeForm(data=request.POST, instance=request.user)

        if user_change_form.is_valid():
            user = user_change_form.save()

    else:
        # editting
        user_change_form = UserChangeForm(instance=request.user)

        context = {
            'user_change_form': user_change_form,
        }

        return render(request, 'update.html', context)