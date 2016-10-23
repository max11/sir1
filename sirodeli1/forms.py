# -*- coding: utf-8 -*-
from time import timezone
from django import forms
from django.db import models
from  sirodeli1.models import PostForm

class MyForm(forms.ModelForm):
	class Meta:
		model = PostForm
		fields = ('name', 'text',) #, 'text'


class DeleteNewForm(forms.ModelForm):
	class Meta:
		model = PostForm
		fields = []
