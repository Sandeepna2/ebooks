from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail_view, name='cart_detail'),
    path('add/<int:book_id>/', views.cart_add_view, name='cart_add'),
    path('remove/<int:book_id>/', views.cart_remove_view, name='cart_remove'),
    path('update/<int:book_id>/', views.cart_update_view, name='cart_update'),
    path('checkout/', views.checkout_view, name='checkout'),
    
    # Real-Time API
    path('api/data/', views.api_cart_data, name='api_cart_data'),
]
