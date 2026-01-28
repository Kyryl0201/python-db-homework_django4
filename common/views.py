from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout

from common.Forms import RegisterForm, LoginForm


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(
                request,
                username=form.cleaned_data["login"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                auth.login(request, user)
                return redirect(f"/user/{user.id}/")
            else:
                return render(request, "login.html", {"form": form, "error": "wrong login or password"})
        return render(request, "login.html", {"form": form})
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, "register.html", {"form": form})
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})




def logout(request):
    django_logout(request)
    return redirect("login")


@login_required(login_url="login")
def user_view(request, user_id):
    user = User.objects.get(id=user_id)
    user_groups = user.groups.all()[0]
    return render(request, "user_page.html", context={"user": user, "group_name": user_groups.name})
