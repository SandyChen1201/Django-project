# 後端
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


@login_required
def user_logout(request):
    logout(request)
    return redirect("login")


@login_required
def user_profile(request):
    return render(request, "user/profile.html", {"user": request.user})


def user_login(request):
    # 起手式兩行
    # message = ""
    # return render(request, "user/login.html", {"message": message})"""
    message = ""
    # 使登入區功能按註冊button轉向到指定url
    if request.method == "POST":
        if request.POST.get("register"):
            print("123")
            return redirect("register")

        elif request.POST.get("login"):
            username = request.POST.get("username")
            password = request.POST.get("password")
            if username == "" or password == "":
                message = "username&password not allow empty!!"
            else:
                # 使登入後跨網域還會存在
                print(User.objects.get(username=username))
                user = authenticate(request, username=username, password=password)
                print(user, username, password)
                if user:
                    login(request, user)
                    message = "login success"
                    return redirect("todolist")
                else:
                    message = "user or password invalide"
    return render(request, "user/login.html", {"message": message})


# Create your views here.
def user_register(request):
    message = ""
    form = UserCreationForm()
    # 取得所有使用者all(會出現在terminal)
    # User.objects.all()
    # 取得唯一使用者get
    # User.objects.get(username="Sandy"))
    # 取得篩選filter
    # print(User.objects.all())
    print(User.objects.filter(username="Sandy"))
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        print(username, password1, password2)
        # 設定限制檢查帳號是否存在(console端用print,後端到前端要賦予意義)
        try:
            if len(password1) < 8:
                message = "password unless 8 words..."
            elif password1 != password2:
                message = "password not same"
            else:
                # 檢查是否有已存在的使用者(.save()等於insert into的用法(簡報28業))
                user = User.objects.filter(username=username)
                if len(user) != 0:
                    message = "user exist!"
                else:
                    User.objects.create_user(
                        username=username, password=password1
                    ).save()
                    message = "sign in success!"
        except Exception as e:
            print(e)
            message = "There has some unexpected error happend..."
    return render(
        request, "user/register.html", {"form": form, "message": message}
    )  # 因為有兩層目錄所以要這樣寫
