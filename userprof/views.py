# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
#from django.core.context_processors import csrf
from django.contrib import auth
from django.template.context_processors import csrf


def login (request):
	args = {'username': auth.get_user(request).username}
	args.update(csrf(request))
	if request.POST:
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/user/')

		else:
			args['login_error'] = 'Пользователь не найден'
			return render_to_response('login.html',args)
	else:
		return render_to_response('login.html', args)


@login_required
def user_logout(request):
	logout(request)
	return  HttpResponseRedirect('/')

@login_required
def user(request):
	args = {'username': auth.get_user(request).username}
	return render_to_response('user.html', args)