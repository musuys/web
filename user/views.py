from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, update_session_auth_hash
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods

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



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/user/login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/change_password.html', {
        'form': form
    })