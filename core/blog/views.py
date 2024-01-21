from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from .models import Post 

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ["title", "body"]
    success_url = '/'

class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "body"]
    success_url = '/'

class PostDeleteView(DeleteView):
    model = Post
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('/')