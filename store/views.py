from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.http import JsonResponse
from .models import Book, Author, Category, Enquiry

def home_view(request):
    featured_books = Book.objects.filter(is_featured=True)[:4]
    categories = Category.objects.all()
    carousel_books = Book.objects.all()[:3]
    return render(request, 'store/index.html', {
        'featured_books': featured_books,
        'categories': categories,
        'carousel_books': carousel_books,
    })

def book_list_view(request):
    query = request.GET.get('q', '').strip()
    category_slug = request.GET.get('category', '').strip()

    books = Book.objects.all()
    categories = Category.objects.all()

    if query:
        books = books.filter(Q(title__icontains=query) | Q(author__name__icontains=query))

    if category_slug:
        books = books.filter(category__slug=category_slug)

    return render(request, 'store/books.html', {
        'books': books,
        'categories': categories,
        'query': query,
        'selected_category': category_slug,
    })

def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    related_books = Book.objects.filter(category=book.category).exclude(pk=book.pk)[:3]
    return render(request, 'store/book_detail.html', {
        'book': book,
        'related_books': related_books,
    })

def author_list_view(request):
    authors = Author.objects.all()
    return render(request, 'store/authors.html', {
        'authors': authors,
    })

def author_detail_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author_books = author.books.all()
    return render(request, 'store/author_detail.html', {
        'author': author,
        'books': author_books,
    })

def about_view(request):
    return render(request, 'store/about.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        messages.success(request, f"Thank you {name}! Your message regarding '{subject}' has been sent successfully.")
        return redirect('store:contact')

    return render(request, 'store/contact.html')

def enquiry_submit_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        book_title = request.POST.get('bookTitle', '')
        inquiry_type = request.POST.get('inquiryType', 'availability')
        message = request.POST.get('message', '')

        Enquiry.objects.create(
            name=name,
            email=email,
            book_title=book_title,
            inquiry_type=inquiry_type,
            message=message
        )

        if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.content_type == 'application/json':
            return JsonResponse({'status': 'success', 'message': 'Enquiry submitted successfully!'})

        messages.success(request, 'Thank you! Your enquiry has been submitted successfully.')
        return redirect('store:home')

    return redirect('store:home')

# Real-Time Live Search JSON API
def api_book_search(request):
    query = request.GET.get('q', '').strip()
    category_slug = request.GET.get('category', '').strip()

    books = Book.objects.all()
    if query:
        books = books.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
    if category_slug:
        books = books.filter(category__slug=category_slug)

    data = [{
        'id': b.id,
        'title': b.title,
        'author': b.author.name,
        'category': b.category.name if b.category else 'General',
        'price': str(b.price),
        'rating': b.rating,
        'reviews_count': b.reviews_count,
        'image': b.image,
        'detail_url': f'/books/{b.id}/'
    } for b in books]

    return JsonResponse({'books': data, 'count': len(data)})
