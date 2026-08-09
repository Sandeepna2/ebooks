from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.http import JsonResponse
from store.models import Book
from .cart import Cart
from .models import Order, OrderItem

def cart_detail_view(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {
        'cart': cart
    })

def cart_add_view(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    quantity = int(request.POST.get('quantity', 1)) if request.method == 'POST' else 1
    cart.add(book=book, quantity=quantity)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
        return JsonResponse({
            'status': 'success',
            'cart_count': len(cart),
            'subtotal': f"{cart.get_subtotal_price():.2f}",
            'tax': f"{cart.get_tax():.2f}",
            'total': f"{cart.get_total_price():.2f}",
            'message': f'Added "{book.title}" to cart!'
        })

    messages.success(request, f'Added "{book.title}" to cart!')
    return redirect('cart:cart_detail')

def cart_remove_view(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
        return JsonResponse({
            'status': 'success',
            'cart_count': len(cart),
            'subtotal': f"{cart.get_subtotal_price():.2f}",
            'tax': f"{cart.get_tax():.2f}",
            'total': f"{cart.get_total_price():.2f}",
            'message': f'Removed "{book.title}" from cart.'
        })

    messages.info(request, f'Removed "{book.title}" from cart.')
    return redirect('cart:cart_detail')

def cart_update_view(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(book=book, quantity=quantity, override_quantity=True)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
        return JsonResponse({
            'status': 'success',
            'cart_count': len(cart),
            'subtotal': f"{cart.get_subtotal_price():.2f}",
            'tax': f"{cart.get_tax():.2f}",
            'total': f"{cart.get_total_price():.2f}"
        })

    return redirect('cart:cart_detail')

def api_cart_data(request):
    cart = Cart(request)
    items = []
    for item in cart:
        items.append({
            'book_id': item['book'].id,
            'title': item['title'],
            'author': item['author'],
            'price': str(item['price']),
            'quantity': item['quantity'],
            'total_price': str(item['total_price']),
            'image': item['image']
        })

    return JsonResponse({
        'cart_count': len(cart),
        'subtotal': f"{cart.get_subtotal_price():.2f}",
        'tax': f"{cart.get_tax():.2f}",
        'total': f"{cart.get_total_price():.2f}",
        'items': items
    })

def checkout_view(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, 'Your cart is empty.')
        return redirect('store:book_list')

    if request.method == 'POST':
        full_name = request.POST.get('full_name', request.user.get_full_name() or 'Guest Reader')
        email = request.POST.get('email', request.user.email or 'guest@example.com')

        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            full_name=full_name,
            email=email,
            total_price=cart.get_total_price(),
            tax=cart.get_tax(),
            status='completed'
        )

        for item in cart:
            OrderItem.objects.create(
                order=order,
                book=item['book'],
                price=item['price'],
                quantity=item['quantity']
            )

        cart.clear()
        messages.success(request, f'Order #{order.id} placed successfully! Thank you for your purchase.')
        return render(request, 'cart/order_confirmation.html', {'order': order})

    return render(request, 'cart/checkout.html', {'cart': cart})
