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


def view_todo(request, id):
    # 因為查看單一事項是唯一，所以用get
    todo = None
    try:
        todo = Todo.objects.get(id=id)
    except Exception as e:
        print(e)

    return render(request, "todo/view-todo.html", {"todo": todo})
