from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread, Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def create_thread(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            thread = Thread.objects.create(title=title, content=content, author=request.user)
            return redirect('forum_home')
    return render(request, 'test_forums.html')

@login_required
def delete_thread(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    if thread.author != request.user:
        return HttpResponseForbidden()
    thread.delete()
    return redirect('forum_home')

@login_required
def modify_thread(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    if thread.author != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            thread.title = title
            thread.content = content
            thread.save()
            return redirect('forum_home')
    return render(request, 'test_forums.html', {'thread_to_modify': thread})


@login_required
def create_comment(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(thread=thread, content=content, author=request.user)
            return redirect('forum_home')
    return render(request, 'test_forums.html')

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author != request.user:
        return HttpResponseForbidden()
    comment.delete()
    return redirect('forum_home')

@login_required
def modify_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            comment.content = content
            comment.save()
            return redirect('forum_home')
    return render(request, 'test_forums.html', {'comment_to_modify': comment})

def forum_home(request):
    threads = Thread.objects.all().prefetch_related('comments')
    return render(request, 'test_forums.html', {'threads': threads})