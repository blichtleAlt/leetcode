from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post

@login_required
def index(request):
    latest_question_list = Post.objects.order_by('-date')[:5]
    template = loader.get_template('blog/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))

@login_required
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return HttpResponse("You're looking at post %s." % post.title)

@login_required
def create(request):
    template = loader.get_template('blog/create.html')
    context = {}
    return HttpResponse(template.render(context, request))


def signup(request):
    # Need a form, this will be a post request handler, on success redirect user logged in to the home page.
    # On failure, retry with a new form and a error message
    template = loader.get_template('blog/signup.html')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return HttpResponse(template.render(context, request))



