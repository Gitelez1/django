from django.shortcuts import render, redirect
from .models import Product, Order
from decimal import Decimal

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def buy(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        product = Product.objects.get(id=product_id)
        total_charge = product.price * quantity

        # Create the order
        Order.objects.create(total_price=total_charge, total_quantity=quantity)

        # Save data to session
        request.session['total_charge'] = float(total_charge)
        request.session['quantity'] = quantity
        request.session['product_id'] = product_id

        return redirect('/amadon/checkout')

def checkout(request):
    total_charge = request.session.get('total_charge', 0)
    quantity = request.session.get('quantity', 0)

    # Calculate total quantity and total amount from all orders
    total_quantity = sum(order.total_quantity for order in Order.objects.all())
    total_amount = sum(order.total_price for order in Order.objects.all())

    context = {
        'total_charge': total_charge,
        'quantity': quantity,
        'total_quantity': total_quantity,
        'total_amount': total_amount,
    }
    return render(request, 'checkout.html', context)

