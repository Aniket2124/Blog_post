# from django import forms
# from django.shortcuts import redirect, render,HttpResponseRedirect
# from django.contrib.auth.models import User
from django.views.generic import CreateView,ListView, UpdateView,DetailView
from.models import Post
from .forms import PostForm, SignupForm
from django.urls import reverse_lazy
# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'post/home.html'
    context_object_name = 'post_list'


    def get_queryset(self):
        return Post.objects.filter(is_published = True, author = self.request.user).order_by('-published_date')

class DraftPost(ListView):
    model = Post
    template_name = 'post/home.html'
    context_object_name = 'post_list'


    def get_queryset(self):
        return Post.objects.filter(is_draft = True, author = self.request.user).order_by('-published_date')


class PostListView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'post_list'


    def get_queryset(self):
        """
        This are the list of published Blogs
        """
        return Post.objects.filter(is_published = True).order_by('-is_published')
    


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    success_url = '/home/'


    def form_valid(self, form):
        if form.is_valid():
            if "draft" in self.request.POST:
                instance = form.save(commit = False)
                instance.is_draft = True
                instance.is_published = False
                instance.author = self.request.user
                instance.save()
            
            if "post" in self.request.POST:
                instance = form.save(commit = False)
                instance.is_published = True
                instance.is_draft = False
                instance.author = self.request.user
                instance.save()

        return super().form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.is_valid():
            if "draft" in self.request.POST:
                instance = form.save(commit = False)
                instance.is_draft = True
                instance.is_published = False
                instance.author = self.request.user
                instance.save()
            
            if "post" in self.request.POST:
                instance = form.save(commit = False)
                instance.is_published = True
                instance.is_draft = False
                instance.author = self.request.user
                instance.save()

        return super().form_valid(form)

class Post_Details(DetailView):
    model = Post

class SignUpView(CreateView):
    form_class = SignupForm
    template_name = 'post/signup.html'
    success_url = reverse_lazy('login')

        
        

