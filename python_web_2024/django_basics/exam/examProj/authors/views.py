from django.contrib.auth import get_user
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from authors.forms import AuthorCreateForm, AuthorEditForm
from authors.models import Author
from examProj.util import get_user_obj


class AuthorCreateView(CreateView):
    model=Author
    form_class = AuthorCreateForm
    template_name = 'author/create-author.html'
    success_url = reverse_lazy('dashboard')
    def form_valid(self, form):
        form.instance.owner= get_user_obj()
        return super().form_valid(form)

class AuthorDetailView(DetailView):
    template_name = 'author/details-author.html'

    def get_object(self, queryset=None):
        return get_user_obj()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = get_user_obj()
        context['authors_posts'] = author.posts.order_by('updated_at').last()
        return context

class AuthorDeleteView(DeleteView):
    template_name = 'author/delete-author.html'
    success_url = reverse_lazy('home')
    def get_object(self, queryset=None):
        return get_user_obj()


class AuthorEditView(UpdateView):
    model = Author
    fields = [
        'first_name',
        'last_name',
        'pets_number',
        'info',
        'image_url'
    ]
    pk_url_kwarg = 'id'
    template_name = 'author/edit-author.html'
    success_url = reverse_lazy('author-details')

    def get_object(self, queryset=None):
        return get_user_obj()
