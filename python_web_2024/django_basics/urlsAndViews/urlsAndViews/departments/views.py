from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from urlsAndViews.departments.models import Department


# Create your views here.
def index(request):
    url = reverse('redirect-view')
    url_lazy = reverse_lazy('redirect-view')
    return HttpResponse(f"<h1>{url_lazy}</h1>")


def view_with_name(request, variable):
    # return HttpResponse(f"<h1>Variable: {variable}</h1>")
    return render(request, 'departments/name_template.html', {'variable': variable})


def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f"<h1>Args: {args}, Kwargs: {kwargs}</h1>")


def view_with_int_pk(request, pk):
    return JsonResponse({'pk': pk})


def view_with_slug(request, pk, slug):
    # department = Department.objects.filter(pk=pk, slug=slug, )
    #
    # if not department:
    #     raise Http404("Department not found")

    department = get_object_or_404(Department, pk=pk, slug=slug)

    return HttpResponse(f"<h1>Department from slug: {department}</h1>")


def show_archive(request, archive_year):
    return HttpResponse(f"<h1>The year is {archive_year}</h1>")


def redirect_to_softuni(request):
    return redirect('https://softuni.bg')

def redirect_to_view(request):
    # return redirect('http://localhost:8000')
    # return redirect(index)
    # return redirect(to='home')
    # return HttpResponse('http://localhost:8000', status=302)
    return redirect('numbers', pk=2)