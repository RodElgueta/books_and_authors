from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('second/<name>', views.second),
    path('addbooks',views.addbook),
    path('addauthors',views.addauthor),
    path('books/<int>',views.book),
    path('createbook',views.createbook),
    path('createauthors',views.createauthors),
    path('delbook',views.delbook),
    path('authors/<int>',views.author),
    path('delauthor',views.delauthor),
    path('addtoauthor/<author_id>',views.addtoauthor),
    path('addtobook/<book_id>',views.addtobook)
]
