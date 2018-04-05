from .models import Journal
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, DetailView, 
                                  UpdateView, DeleteView)


class JournalListView(ListView):
    model = Journal
    template_name = 'journal/list_journals.html'
    context_object_name = 'journals'


class JournalCreateView(CreateView):
    model = Journal
    template_name = "journal/add_journal.html"
    fields = ['title', 'content']


class JournalDetailView(DetailView):
    model = Journal
    template_name = 'journal/show_journal.html'
    context_object_name = 'journal'
    

class JournalUpdateView(UpdateView):
    model = Journal
    context_object_name = 'journal'
    template_name = 'journal/edit_journal.html'
    fields = ['title', 'content']


class JournalDeleteView(DeleteView):
    model = Journal
    context_object_name = 'journal'
    success_url = reverse_lazy('list-journals')
