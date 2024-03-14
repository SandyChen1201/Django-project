from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def user_register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        print(username, password1, password2)

    return render(
        request, "user/register.html", {"form": UserCreationForm()}
    )  # 因為有兩層目錄所以要這樣寫
