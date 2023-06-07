from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

def index(request):
    ls=Post.objects.all()
    return render(request,'index.html',{'posts':ls})

def post_single(request,pk):
    # Post.objects.get(pk=pk)
    p=get_object_or_404(Post.objects.all(),pk=pk)
    return render(request,'post_single.html',{'post':p})