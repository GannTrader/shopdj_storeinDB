from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import product, cart
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

listcart = {}
# Create your views here.
def index(request):
	products = product.objects.all()
	return render(request, 'shop/product_list.html', {'products':products})


@login_required
def insertCart(request, id):
	item = get_object_or_404(product, id=id)
	itemCart = cart.objects.filter(product=item, user=request.user)

	if itemCart.exists():
		item_cart = cart.objects.get(product=item, user=request.user)
		item_cart.quantity += 1
		item_cart.save()
		messages.info(request, 'sản phẩm vừa được update số lượng')
	else:		
		cart.objects.create(
			idsp = id,
			user = request.user,
			product=item,
			price = item.price
		)
		messages.warning(request, 'bạn vừa thêm sp vào giỏ')

	return redirect('shop:listproduct')

@login_required
def viewCart(request):
	listcart = cart.objects.all().filter(user=request.user)
	total = 0
	for item in listcart:
		total += item.price * item.quantity
	return render(request, 'shop/viewcart.html', {'listcart':listcart, 'total': total})

@login_required
def updateCart(request, id):
	qty = request.POST['qty']	
	cart.objects.filter(idsp=id).update(quantity=qty)
	messages.success(request, 'bạn vừa thay đổi số lượng sản phẩm')
	return redirect('shop:viewCart')

@login_required
def deleteCart(request, id):
	cart.objects.filter(idsp=id).delete()
	messages.warning(request, 'bạn vừa xóa sp trong giỏ')
	return redirect('shop:viewCart')