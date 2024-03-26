from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.


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
