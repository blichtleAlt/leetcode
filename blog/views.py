from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from .models import Post

def index(request):
    latest_question_list = Post.objects.order_by('-date')[:5]
    template = loader.get_template('blog/index.html')
    context = {
        'latest_question_list': latest_question_list,
        'user': 'Brendan'
    }
    return HttpResponse(template.render(context, request))

def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return HttpResponse("You're looking at post %s." % post.title)

