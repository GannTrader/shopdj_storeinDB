from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import product, cart
# Create your views here.
def index(request):
	products = product.objects.all()
	return render(request, 'shop/product_list.html', {'products':products})

def insertCart(request, id):
	item = get_object_or_404(product, id=id)
	itemCart = cart.objects.filter(product=item)

	if itemCart.exists():
		item_cart = cart.objects.get(product=item)
		item_cart.quantity += 1
		item_cart.save()
	else:
		cart.objects.create(product=item)

	return redirect('shop:listproduct')