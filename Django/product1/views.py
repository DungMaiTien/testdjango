from django.shortcuts import render, redirect
from .models import Product1
from cart.models import CartItem

# Create your views here.
def product1(request):
    products = Product1.objects.all()
    return render(request, 'product1/product1.html', {'products': products})

def add_to_cart(request, product_id):
    # Lấy thông tin sản phẩm từ ID hoặc POST request
    product = Product1.objects.get(pk=product_id)
    
    # Xác định người dùng hiện tại (ở đây giả định bạn đã đăng nhập)
    user = request.user
    
    # Xác định giỏ hàng của người dùng, nếu không có thì tạo mới
    cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
    
    # Tăng số lượng sản phẩm trong giỏ hàng
    cart_item.quantity = 1
    cart_item.save()
    
    return redirect('cart:cart')