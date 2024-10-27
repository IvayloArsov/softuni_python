from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from examProj.util import get_user_obj, PlaceholderMixin
from posts.forms import PostCreateForm, PostDeleteForm, PostEditForm
from posts.models import Post


# Create your views here.
class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post/create-post.html'
    success_url = reverse_lazy('dashboard')
    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data()
        context['author'] = get_user_obj()
        context['posts'] = Post.objects.all()
        return context

class PostDetailsView(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'post/details-post.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data()
        context['author'] = get_user_obj()
        context['posts'] = Post.objects.all()
        return context


class PostDeleteView(DeleteView):
    model = Post
    form_class = PostDeleteForm
    pk_url_kwarg = 'id'
    template_name = 'post/delete-post.html'
    success_url = reverse_lazy('dashboard')


    def get_initial(self):
        return self.object.__dict__
    def form_invalid(self, form):
        return self.form_valid(form)

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data()
        context['author'] = get_user_obj()
        context['posts'] = Post.objects.all()
        return context


class PostEditView(UpdateView):
    model = Post
    pk_url_kwarg = 'id'
    form_class = PostEditForm
    template_name = 'post/edit-post.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data()
        context['author'] = get_user_obj()
        context['posts'] = Post.objects.all()
        return context


