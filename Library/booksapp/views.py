from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import RedirectView, TemplateView, View
from django.views.generic.edit import FormView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.db.models import Sum, Min, Max, Avg, Count
from .models import BookModel, AuthorModel
from .forms import BookForm, AuthorForm
# Create your views here.



# This view is for AuthorView
class AuthorView(FormView):
    template_name = 'bookapp/author.html'
    form_class = AuthorForm
    success_url = '/addbook/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

# This view is for BookView
class BookView(FormView):
    template_name = 'bookapp/book.html'
    form_class = BookForm
    success_url = '/dashboard/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
# This view is for DashboardView
class DashboardView(TemplateView):
    template_name = 'bookapp/dashboard.html'
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        bk = BookModel.objects.all()
        ar = AuthorModel.objects.all()
        context = {'book':bk, 'author':ar}
        return context


# This view is for Delete Book
class BookDeleteView(RedirectView):
    url = '/dashboard/'
    def get_redirect_url(self, *args, **kwargs):
        BookModel.objects.get(pk=kwargs['id']).delete()
        return super().get_redirect_url(*args, **kwargs)
    
# This view is for Delete Author
class AuthorDeleteView(RedirectView):
    url = '/dashboard/'
    def get_redirect_url(self, *args, **kwargs):
        AuthorModel.objects.get(pk=kwargs['id']).delete()
        return super().get_redirect_url(*args, **kwargs)

# This view is for Update Book
class BookUpdateView(UpdateView):
    model = BookModel
    fields = ['title', 'author', 'publication_year', 'isbn', 'price']
    success_url = '/dashboard/'
    template_name = 'bookapp/book.html'

# this view is for Update Author
class AuthorUpdateView(UpdateView):
    model = AuthorModel
    fields = ['first_name', 'last_name', 'address',]
    success_url = '/dashboard/'
    template_name = 'bookapp/author.html'

# This view is for Aggregation
class AggregationView(TemplateView):
    template_name = 'bookapp/aggregation.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        cont = BookModel.objects.count()
        price_average = BookModel.objects.aggregate(avg_price=Avg("price"))['avg_price']
        old = BookModel.objects.order_by('publication_year').first()
        new = BookModel.objects.order_by('-publication_year').first()
        books_per_year = BookModel.objects.values('publication_year').annotate(count=Count('id')).order_by('publication_year')

        
    

        context = {'count':cont, 'average':price_average, 'oldest': old, 'newest':new, 'countyear':books_per_year}
        return context


