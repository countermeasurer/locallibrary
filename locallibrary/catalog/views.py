from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Language


def index(request):
    """
    Функция отображения для домашней страницы

    """

    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()

    # Доступные книги (статус = 'а')

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits']= num_visits+1
    # Кол-во жанров

    num_genre = Genre.objects.all().count()
    num_language = Language.objects.all().count()

    # Отрисовка html- шаблона index.html с данными внутри
    # переменной контекста context

    return render(
        request,
        'index.html',
        context=
        {'num_books': num_books, 'num_instance': num_instance, 'num_instances_available': num_instances_available,
         'num_authors': num_authors, 'num_genre': num_genre, 'num_language': num_language, 'num_visits': num_visits},
    )


from django.views import generic


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author