from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_journals, name='list-journals'),
    path('add-journal', views.add_journal, name='add-journal'),
    path('<int:pk>/show-journal', views.show_journal, name='show-journal'),
    path('<int:pk>/edit-journal', views.edit_journal, name='edit-journal'),
    path('<int:pk>/delete-journal', views.delete_journal, name='delete-journal')
]