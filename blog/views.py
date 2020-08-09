from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Post

@login_required
def index(request):
    # latest_question_list = Post.objects.order_by('-date')[:5]
    template = loader.get_template('blog/index.html')
    # context = {
    #     'latest_question_list': latest_question_list
    # }
    context = {}
    return HttpResponse(template.render(context, request))

@login_required
def detail(request, post_id):
    template = loader.get_template('blog/post.html')
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return HttpResponse(template.render(context, request))

@login_required
def create(request):
    template = loader.get_template('blog/create.html')
    print(request)
    print(request.user)
    if request.method == "POST":
        print("create new post")
        return redirect('/')
    context = {}
    return HttpResponse(template.render(context, request))

@login_required
def projects(request):
    template = loader.get_template('blog/projects.html')
    context = {}
    return HttpResponse(template.render(context, request))

@login_required
def about(request):
    template = loader.get_template('blog/about.html')
    context = {}
    return HttpResponse(template.render(context, request))

class AddUserView(CreateView):
    model = User
    template = 'templates/auth/user_form.html'
    fields = "__all__"

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



