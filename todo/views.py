from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import TodoItem
import json


def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

@csrf_exempt
def add_todo(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data['title']
        todo = TodoItem.objects.create(title=title)
        return JsonResponse({'id': todo.id, 'title': todo.title, 'completed': todo.completed})

@csrf_exempt
def update_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, pk=todo_id)
    if request.method == 'PUT':
        data = json.loads(request.body)
        completed = data['completed']
        todo.completed = completed
        todo.save()
        return JsonResponse({'id': todo.id, 'completed': todo.completed})

@csrf_exempt
def delete_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, pk=todo_id)
    if request.method == 'DELETE':
        todo.delete()
        return HttpResponse(status=204)