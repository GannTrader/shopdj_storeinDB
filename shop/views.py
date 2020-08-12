from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import product, cart
# Create your views here.
def index(request):
	products = product.objects.all()
	return render(request, 'shop/product_list.html', {'products':products})

def insertCart(request, id):
	item = get_object_or_404(product, id=id)
	itemCart = cart.objects.get_or_create(product=item)
	return HttpResponse(itemCart)