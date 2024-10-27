from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView
from authors.forms import AuthorCreateForm
from examProj.util import get_user_obj
from posts.forms import PostCreateForm
from posts.models import Post


class HomePage(ListView, BaseFormView):
    template_name = 'index.html'
    model = Post
    form_class = AuthorCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data()
        context['author'] = get_user_obj()
        return context

class DashboardPage(ListView, BaseFormView):
    template_name = 'dashboard.html'
    model = Post
    form_class = AuthorCreateForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data()
        context['author'] = get_user_obj()
        context['posts'] = Post.objects.all()
        return context