# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render_to_response
from django.template import Context
from django.template.loader import get_template

from sirodeli1.models import PostForm
from django.http import HttpResponseRedirect
from sirodeli1.forms import MyForm, DeleteNewForm


def demo_func(request):
	all = PostForm.objects.all()
	return render_to_response('all_objects.html', {'all': all, 'username': auth.get_user(request).username})

@login_required()
def my_form(request):
	if request.method == 'POST':
		form = MyForm(request.POST)
		if form.is_valid():
			#commit - произвольная отправка формы
			post = form.save(commit=False)
			#user вытаскивается из сессии
			post.author = request.user
			post.save()
			return redirect('sirodeli1name:post_details', pk = post.pk ) #redirect('demo2name:post_all')
			#HttpResponseRedirect('/demo2/')
	else:
		form = MyForm

	return render(request, 'forms.html', {'form': form, 'username': auth.get_user(request).username})

def post_detail(request, pk):
	post = get_object_or_404(PostForm, pk=pk)
	return render(request, 'post_detail.html', {'post':post, 'username': auth.get_user(request).username})

def post_detai2l(request, pk):
	post = get_object_or_404(PostForm, pk=pk)
	return render(request, 'post_detail.html', {'post':post, 'username': auth.get_user(request).username})

def delete_new(request,pk):
	new_to_delete = get_object_or_404(PostForm, pk=pk)
	# +some code to check if this object belongs to the logged in user

	if request.method == 'POST':
		form = DeleteNewForm(request.POST, instance=new_to_delete)
		# так же для редактирования нужно передать instance поста в форму
		if form.is_valid():  # checks CSRF
			new_to_delete.delete()
			return redirect('sirodeli1name:post_all')  # wherever to go after deleting
	else:
		form = DeleteNewForm(instance=new_to_delete)
	template_vars = {'form': form, 'username': auth.get_user(request).username}
	return render(request, 'delete.html', template_vars)