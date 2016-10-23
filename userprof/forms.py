# -*- coding: utf-8 -*-
from time import timezone
from django import forms
from django.contrib.auth.models import User
from django.db import models
from userprof.models import UserProfile


class UserForm (forms.ModelForm):
	#password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = []


class UserProfileForm (forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['username','website']


