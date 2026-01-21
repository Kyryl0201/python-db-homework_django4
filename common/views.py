from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == "POST":
        return "ok"
    else:
        return render("login.html")

def register(request):
    return "ok"

def logout(request):
    return redirect("login")

def user_view(request, user_id):
    return f"ok {user_id}"
