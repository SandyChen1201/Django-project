from django.shortcuts import render
from .models import Todo

# Create your views here.


def todo(request):
    # all,get,filter
    # todos = Todo.objects.all()
    # 確認使用者:
    todos = None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)
    # print(todos)

    return render(request, "todo/todo.html", {"todos": todos})