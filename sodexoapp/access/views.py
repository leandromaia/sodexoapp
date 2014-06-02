# coding=utf-8
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render


@login_required
def show_system(request):
    user = {'id': request.user.id,
            'username': request.user.username,
            'email': request.user.email}
    return render_to_response('index.html', {'user': user})


def do_login(request):
    if request.method == 'GET':
        error_msg = request.GET.get('error_msg', '')
        report_msg = request.GET.get('report_msg', '')
        return render_to_response('login.html',
                            {'error_msg': error_msg, 'report_msg': report_msg})

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/')

    return render_to_response('login.html',
                    {'error_msg': ('Usuário ou senha inválido')})


def do_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def recover_password(request):
    return render(request, 'pwrecover.html', content_type='text/html')


def create_account(request):
    return render(request, 'createaccount.html', content_type='text/html')
