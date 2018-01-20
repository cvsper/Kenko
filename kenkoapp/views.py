from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from kenkoapp.forms import UserForm, CareproForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def home(request):
	return redirect(carepro_home)

@login_required(login_url='/carepro/sign-in/')
def carepro_home(request):
		return render(request, "carepro/home.html", {})

def carepro_sign_up(request):
	user_form = UserForm()
	carepro_form = CareproForm()

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		carepro_form = CareproForm(request.POST, request.FILES)

		if user_form.is_vaild() and carepro_form.is_vaild():
			new_user = User.objects.create_user(**user_form.cleaned_data)
			new_carepro = carepro_form.save(commit=False)
			new_carepro.user = new_user
			new_carepro.save()

			login(request, authenticate(
				username = user_form.cleaned_data("username"),
				password = user_form.cleaned_data("password")
				))

			return redirect(carepro_home)

	return render(request, 'carepro/sign_up.html', {
		"user_form" : user_form,
		"carepro_form" : carepro_form
		})