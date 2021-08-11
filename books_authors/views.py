from django.shortcuts import render, HttpResponse,redirect
from .models import *
def index(request):
    context = {
        'saludo': 'Hola'
    }

    return render(request, 'landing.html', context)


def second(request, name):
    return HttpResponse('Hola ' + name)

def addbook(request):
    books = Books.objects.all()
    context = {'books': books}
    return render(request,'addbooks.html',context)

def addauthor(request):
    authors = Authors.objects.all()
    context = {'authors': authors}
    return render(request,'addauthors.html',context)

def book(request,int):
    book = Books.objects.get(id=int)
    
    bookauthors = [author.id for author in book.authors.all()]
    nobooksauthor = [author for author in Authors.objects.all() if author.id not in bookauthors]
    context = {'book': book,
                'nobooksauthor':nobooksauthor}
    return render(request,'book.html',context)

def addtobook(request, book_id):
    book = Books.objects.get(id=int(book_id))
    author_id = int(request.POST['newauthor'])
    author = Authors.objects.get(id=author_id)
    author.books.add(book)
    return redirect(f"/byn/books/{book_id}")

def author(request,int):
    author = Authors.objects.get(id=int)
    authorbooks = [book.id for book in author.books.all()]
    noauthorbooks = [book for book in Books.objects.all() if book.id not in authorbooks]
    context = {'author': author,
                'noauthorbooks':noauthorbooks}
    return render(request,'author.html',context)

def addtoauthor(request, author_id):
    author = Authors.objects.get(id=int(author_id))
    book_id = int(request.POST['newbook'])
    book = Books.objects.get(id=book_id)
    book.authors.add(author)
    return redirect(f"/byn/authors/{author_id}")

def createbook(request):
    title = request.POST['title']
    desc = request.POST['desc']
    new_book = Books.objects.create (title = title,desc=desc)
    return redirect("/byn/addbooks")

def delbook(request):
    bookid = request.POST['id']
    bookdel = Books.objects.get(id=bookid)
    bookdel.delete()

    return redirect("/byn/addbooks")

def createauthors(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes = request.POST['notes']
    new_author = Authors.objects.create (first_name = first_name,last_name=last_name,notes=notes)
    return redirect("/byn/addauthors")

def delauthor(request):
    authorid = request.POST['id']
    authordel = Authors.objects.get(id=authorid)
    authordel.delete()

    return redirect("/byn/addauthors")



