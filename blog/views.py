from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)
from .models import Post 
from .permissions import HasAdminAccessPermission


class PostListView(LoginRequiredMixin, ListView):
    model = Post

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, HasAdminAccessPermission, CreateView):
    model = Post
    fields = ["title", "body"]
    success_url = '/'

class PostUpdateView(LoginRequiredMixin, HasAdminAccessPermission, UpdateView):
    model = Post
    fields = ["title", "body"]
    success_url = '/'

class PostDeleteView(LoginRequiredMixin, HasAdminAccessPermission, DeleteView):
    model = Post
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('/')