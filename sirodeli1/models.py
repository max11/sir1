from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.

class PostForm(models.Model):
	class Meta():
		db_table = 'app_forms_active'

	author = models.ForeignKey('auth.User')
	name = models.CharField(max_length=200)
	text = RichTextUploadingField(blank=True)

	#text_redactor = RichTextUploadingField(blank=True)
	#publ = models.DateTimeField(blank=True)
	#text2 = models.TextField(blank=True)
	def __unicode__(self):
		return self.name