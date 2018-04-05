from django.urls import path
from . import views

urlpatterns = [
    path('', views.JournalListView.as_view(), name='list-journals'),
    path('add-journal', views.JournalCreateView.as_view(), name='add-journal'),
    path('<int:pk>/show-journal',
         views.JournalDetailView.as_view(), name='show-journal'),
    path('<int:pk>/edit-journal',
         views.JournalUpdateView.as_view(), name='edit-journal'),
    path('<int:pk>/delete-journal',
         views.JournalDeleteView.as_view(), name='delete-journal')
]
