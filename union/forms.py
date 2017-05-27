from django.contrib.auth.models import User
from django import forms
from .models import Union, Member

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class UnionForm(forms.ModelForm):

	class Meta:
		model = Union
		fields = ['name', 'logo', 'info']


class MemberForm(forms.ModelForm):

	class Meta:
		model = Member
		fields = ['name', 'member_id', 'major','sex']