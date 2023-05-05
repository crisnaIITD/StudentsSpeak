from django.shortcuts import render, HttpResponse, redirect
from home.models import Speak
from home.forms import PostForm

from django.utils import timezone
from datetime import timedelta

# Create your views here.
def index(request):
    Speaks = Speak.objects.all().order_by('-id')
    context = {
        'speaks':Speaks
    }
    return render(request, 'home/index.html', context)


def detail(request, speaker_name):
    speaker_posts = Speak.objects.filter(who_speaks=speaker_name)
    
    for post in speaker_posts:
        time_diff = timezone.now() - post.speak_time
        if time_diff <= timedelta(minutes=59):
            post.time_ago = f"{time_diff.seconds // 60} minutes ago"
        elif time_diff <= timedelta(hours=23):
            post.time_ago = f"{time_diff.seconds // 3600} hours ago"
        else:
            post.time_ago = post.speak_time.strftime("%b %d, %Y %I:%M %p")
    
    context = {
        'speaker_name': speaker_name,
        'speaker_posts': speaker_posts
    }
    return render(request, "home/detail.html", context)


def create_post(request):
    post_form = PostForm(request.POST or None)

    if post_form.is_valid():
        post_form.save()
        return redirect('home:index')
    
    context = {
        'post_form': post_form
    }
    return render(request, 'home/create-post.html', context)