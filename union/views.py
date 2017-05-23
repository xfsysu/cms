from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Union,Member
from .forms import UnionForm, MemberForm, UserForm

IMAGE_FILE_TYPE = ['jpg', 'png', 'jpeg']

def index(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('union:login_user', kwargs={}))
	else:	
		unions = Union.objects.filter(user=request.user)
		return render(request, 'union/index.html', {'unions':unions})

def detail(request, union_id):
	union = get_object_or_404(Union, pk=union_id)
	return render(request, 'union/detail.html', {'union': union})

def union_add(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('union:login_user', kwargs={}))
	else:
		form = UnionForm(request.POST or None, request.FILES or None)

		if form.is_valid():
			union = form.save(commit=False)
			union.user = request.user
			union.logo = request.FILES['logo']
			union.save()

			file_type = union.logo.url.split('.')[-1].lower()

			if file_type not in IMAGE_FILE_TYPE:
				context = {
					'form': form,
					'error_message': 'Image file must be PNG, JPG, or JPEG'
				}
				return render(request, 'union/union_add.html', context)
			else:
				return HttpResponseRedirect(reverse('union:detail', kwargs={'union_id':union.id}))

		return render(request, 'union/union_add.html', {'form': form})

def union_delete(request, union_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('union:login_user', kwargs={}))
	else:
		union = get_object_or_404(Union, pk=union_id)
		union.delete()
		return HttpResponseRedirect(reverse('union:index'), kwargs={})

def member_add(request, union_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('union:login_user', kwargs={}))
	else:
		form = MemberForm(request.POST or None)
		union = get_object_or_404(Union, pk=union_id)

		if form.is_valid():
			member = form.save(commit=False)
			member.union = union
			member.save()

			return HttpResponseRedirect(reverse('union:detail', kwargs={'union_id':union_id}))

		context = {
			'form': form,
			'union': union,
		}
		return render(request, 'union/member_add.html', context)

def member_delete(request, member_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('union:login_user', kwargs={}))
	else:
		member = get_object_or_404(Member, pk=member_id)
		union_id = member.union.id
		member.delete()

		return HttpResponseRedirect(reverse('union:detail', kwargs={'union_id':union_id}))

def member_edit(request, member_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('union:login_user', kwargs={}))
	else:
		member = get_object_or_404(Member, pk=member_id)
		union = member.union
		if request.method == "POST":
			form = MemberForm(request.POST or None, instance=member)
			if form.is_valid():
				member_info = form.save(commit=False)
				member_info.union = union
				member_info.save()
				return HttpResponseRedirect(reverse('union:detail', kwargs={'union_id':union.id}))
	
		if request.method == "GET":
			form = MemberForm(instance=member) #store the original info
		context = {
			'form':form,
			'union':union
		}
		return render(request, 'union/member_edit.html', context)

def view_all(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('union:login_user', kwargs={}))
	else:
		unions = Union.objects.filter(user=request.user)
		members = []

		for union in unions:
			members += union.member_set.all()
		return render(request, 'union/view_all.html', {'members':members})

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				unions = Union.objects.filter(user=request.user)
				return render(request, 'union/index.html', {'unions':unions})
			else:
				return render(request, 'union/login.html', {'error_message':"Your Account is disabled!"})
		else:
			return render(request, 'union/login.html', {'error_message':"Invalid Input"})

	return render(request, 'union/login.html')

def register(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user.set_password(password)
		user.save()

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				unions = Union.objects.filter(user=request.user)
				return render(request, 'union/index.html', {'unions':unions})
 
	return render(request, 'union/register.html', {'form':form})

def logout_user(request):
	logout(request)
	return HttpResponseRedirect(reverse('union:login_user', kwargs={}))