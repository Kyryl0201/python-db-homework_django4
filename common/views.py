from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as django_logout
from django.views import View
from common.Forms import RegisterForm, LoginForm


class LoginView(View):
    form = LoginForm
    template_name = "login.html"
    
    def get(self, request):
        return render(request, self.template_name, context={"form": self.form()})

    def post(self, request):
        form = self.form(request.POST)

        if not form.is_valid():
            return render(request, self.template_name, {"form": form})

        user = auth.authenticate(
            request,
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )

        if user is not None:
            auth.login(request, user)
            return redirect(f"/user/{user.id}/")

        return render(request, self.template_name, {"form": form,"error": "wrong login or password",})

class RegisterView(View):
    template_name = "register.html"
    form = RegisterForm

    def get(self, request):
        return render(request, self.template_name, context={"form": self.form()})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, self.template_name, context={"form": form})



def logout(request):
    django_logout(request)
    return redirect("login")


@login_required(login_url="login")
def user_view(request, user_id):
    user = get_object_or_404(User, id=user_id)

    groups_qs = user.groups.all()
    group_name = groups_qs.first().name if groups_qs.exists() else "No group"

    return render(request, "user_page.html", {
        "user": user,
        "group_name": group_name,
    })
