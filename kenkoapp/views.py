from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from kenkoapp.forms import UserForm, CareproForm, UserFormForEdit, CareForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from kenkoapp.models import Care, Order

# Create your views here.
def home(request):
	return redirect(carepro_home)

@login_required(login_url='/carepro/sign-in/')
def carepro_home(request):
		return redirect(carepro_order)

@login_required(login_url='/carepro/sign-in/')
def carepro_account(request):
    user_form = UserFormForEdit(instance = request.user)
    carepro_form = CareproForm(instance = request.user.carepro)

    if request.method == "POST":
        user_form = UserFormForEdit(request.POST, instance = request.user)
        carepro_form = CareproForm(request.POST, request.FILES, instance = request.user.carepro)

        if user_form.is_valid() and carepro_form.is_valid():
            user_form.save()
            carepro_form.save()

    return render(request, 'carepro/account.html', {
        "user_form": user_form,
        "carepro_form": carepro_form
    })

@login_required(login_url='/carepro/sign-in/')
def carepro_report(request):
		return render(request, "carepro/report.html", {})

@login_required(login_url='/carepro/sign-in/')
def carepro_order(request):
        if request.method == "POST":
            order = Order.objects.get(id = request.POST["id"], carepro = request.user.carepro)

            if order.status == Order.READY:
                order.status = Order.ONTHEWAY
                order.save()

        orders = Order.objects.filter(carepro = request.user.carepro).order_by("-id")
        return render(request, "carepro/order.html", { 'orders' : orders })

@login_required(login_url='/carepro/sign-in/')
def carepro_care(request):
        cares = Care.objects.filter(carepro = request.user.carepro).order_by('-id')

        return render(request, "carepro/care.html", {'cares' : cares})  

@login_required(login_url='/carepro/sign-in/')
def carepro_add_care(request):
        form = CareForm()
        if request.method=='POST':
            form = CareForm(request.POST,request.FILES)

            if form.is_valid():
                care = form.save(commit = False)
                care.carepro = request.user.carepro
                care.save()

                return redirect(carepro_care)

        return render(request, "carepro/add_care.html", {
            'form' : form
            })                						

@login_required(login_url='/carepro/sign-in/')
def carepro_edit_care(request, care_id):
        form = CareForm(instance = Care.objects.get(id = care_id))
        if request.method=='POST':
            form = CareForm(request.POST,request.FILES, instance = Care.objects.get(id = care_id))

            if form.is_valid():
                care.save()

                return redirect(carepro_care)

        return render(request, "carepro/edit_care.html", {
            'form' : form
            })

def carepro_sign_up(request):
    user_form = UserForm()
    carepro_form = CareproForm()

    if request.method == "POST":
        user_form = UserForm(request.POST)
        carepro_form = CareproForm(request.POST, request.FILES)

        if user_form.is_valid() and carepro_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_carepro = carepro_form.save(commit=False)
            new_carepro.user = new_user
            new_carepro.save()

            login(request, authenticate(
                username = user_form.cleaned_data["username"],
                password = user_form.cleaned_data["password"]
            ))

            return redirect(carepro_home)

    return render(request, "carepro/sign_up.html", {
        "user_form": user_form,
        "carepro_form": carepro_form
    })