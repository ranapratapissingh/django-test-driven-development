from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Entry
from django.views.generic import DetailView

# Create your views here.



class HomeView(ListView):

    template_name = 'index.html'
    queryset = Entry.objects.order_by('-created_at')


class EntryDetail(DetailView):
    model = Entry