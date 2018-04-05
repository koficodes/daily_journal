from django.shortcuts import render, redirect, get_object_or_404
# redirect and get_object_or_404 modules will be used later.
from .models import Journal
from .forms import JournalFoam


def list_journals(request):
    context = {'journals': Journal.objects.all}
    return render(request, 'journal/list_journals.html', context)

def add_journal(request):

    if request.method == 'POST':
        form = JournalFoam(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            journal = Journal.objects.create(title=title, content=content) # assign to a journal variable

            return redirect(journal.get_absolute_url()) 

    context = {'form': JournalFoam()}
    return render(request, 'journal/add_journal.html', context)

def show_journal(request, pk):
    journal = get_object_or_404(Journal, pk=pk)
    return render(request, 'journal/show_journal.html', {'journal': journal} )
    

def edit_journal(request, pk):
    journal = get_object_or_404(Journal, pk=pk)

    if request.method == 'POST':
        form = JournalFoam(request.POST)
        if form.is_valid():
            journal.title = form.cleaned_data['title']
            journal.content = form.cleaned_data['content']

            journal.save()
            return redirect('list-journals')

    form = JournalFoam(
        initial={'title': journal.title, 'content': journal.content})

    return render(request, 'journal/edit_journal.html',
                  {'form': form, 'pk': pk})

def delete_journal(request, pk):
    journal = get_object_or_404(Journal, pk=pk)

    if request.method == 'POST':
        journal.delete()
        return redirect('list-journals')

    return render(request, 'journal/journal_confirm_delete.html',
                  {'journal': journal})
