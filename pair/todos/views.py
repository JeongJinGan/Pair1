from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.


def index(request):
    todos = Todo.objects.all()
    context = {
        "todos": todos,
    }
    return render(request, "todos/index.html", context)


def new(request):
    return render(request, "todos/new.html")


def create(request):
    # 1. parameter로 날라온 데이터를 DB에 저장
    title = request.GET.get("title___")
    content = request.GET.get("content___")

    # 2. DB에 저장
    Todo.objects.create(title=title, content=content)

    return redirect("todos:index")


def detail(request, pk_):
    todo = Todo.objects.get(pk=pk_)
    context = {
        "todo": todo,
    }
    return render(request, "todos/detail.html", context)


def edit(request, pk_):
    todo = Todo.objects.get(pk=pk_)
    context = {
        "todo": todo,
    }
    return render(request, "todos/edit.html", context)


def update(request, pk_):
    # update할 특정 데이터를 불러온다 -> pk_를 사용해서
    todo = Todo.objects.get(pk=pk_)
    title_ = request.GET.get("title___")
    content_ = request.GET.get("content___")

    # 데이터를 수정
    todo.title = title_
    todo.content = content_

    # 데이터를 수정한 것을 반영(save)
    todo.save()

    # 데이터의 디테일 페이지로 리다이렉트
    return redirect("todos:detail", todo.pk)


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()

    return redirect("todos:index")
