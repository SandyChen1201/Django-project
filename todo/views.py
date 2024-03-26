from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def delete_todo(request, id):
    # get指定要的事項
    try:
        todo = Todo.objects.get(id=id)
        todo.delete()
    except Exception as e:
        print(e)
    return redirect("todolist")


@login_required
def completed_todo(request):
    # all,get,filter
    # todos = Todo.objects.all()
    # order_by:排序(要排的東西)(-是降序)
    # 確認使用者:
    todos = None
    completed = True
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user, completed=True).order_by(
            "-created"
        )
    # print(todos)
    # 給前端一個變數區分
    return render(request, "todo/todo.html", {"todos": todos, "completed": completed})


@login_required
def create_todo(request):  # 程式的函數或變數宣告才會用底線
    # 第一次會是GET模式
    # 因為不管是GET還是POST都要回傳FROM
    message = ""
    form = TodoForm()
    if request.method == "POST":
        try:
            print(request.POST)
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)  #
            new_todo.user = request.user
            new_todo.save()
            message = "建立事項成功"
            return redirect("todolist")
        except Exception as e:
            print(e)
            message = "建立失敗:("
    return render(request, "todo/create-todo.html", {"form": form, "message": message})


def todolist(request):
    # all,get,filter
    # todos = Todo.objects.all()
    # order_by:排序(要排的東西)(-是降序)
    # 確認使用者:
    todos = None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user).order_by("-created")
    # print(todos)

    return render(request, "todo/todo.html", {"todos": todos})


@login_required
def view_todo(request, id):
    # 因為查看單一事項是唯一，所以用get
    todo = None
    message = ""
    try:
        todo = Todo.objects.get(id=id)
        form = TodoForm(instance=todo)  # instance實體=單一物件)

        if request.method == "POST":
            print(request.POST)
            if request.POST.get("update"):

                if request.POST.get("completed"):
                    todo.date_completed = datetime.now()
                else:
                    todo.date_completed = None

                form = TodoForm(request.POST, instance=todo)
                if form.is_valid():
                    form.save()
                    message = "修改成功"
            elif request.POST.get("delete"):
                todo.delete()
                return redirect("todolist")

    except Exception as e:
        print(e)
        message = "修改/刪除失敗"

    return render(
        request, "todo/view-todo.html", {"todo": todo, "form": form, "message": message}
    )
