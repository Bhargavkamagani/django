from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.http import JsonResponse

# def index(request):
#     if request.method == "POST":
#         title = request.POST.get("title")
#         Task.objects.create(title=title)
#         return redirect("index")

#     tasks = Task.objects.all()
#     return render(request, "todo/index.html", {"tasks": tasks})


def index(request):
    # GET → show all tasks
    if request.method == "GET":
        tasks = Task.objects.all().order_by("-id")
        return render(request, "todo/index.html", {"tasks": tasks})

    # POST → create task
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            Task.objects.create(title=title)
        return redirect("index")


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("index")


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        completed = request.POST.get("completed")

        if title:
            task.title = title
        task.completed = True if completed == "on" else False
        task.save()

    return redirect("index")
