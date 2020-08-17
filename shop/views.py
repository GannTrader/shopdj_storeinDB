from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import product, cart
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import loginForm, signupForm
from django.views import View

listcart = {}
# Create your views here.
def index(request):
	products = product.objects.all()
	return render(request, 'shop/product_list.html', {'products':products})


@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def viewCart(request):
	listcart = cart.objects.all().filter(user=request.user)
	total = 0
	for item in listcart:
		total += item.price * item.quantity
	return render(request, 'shop/viewcart.html', {'listcart':listcart, 'total': total})

@login_required(login_url='/login/')
def updateCart(request):
	id = request.POST.get('id')
	number = request.POST.get('number')

	cart.objects.filter(idsp=id).update(quantity=number)

	return redirect('shop:viewCart')

@login_required(login_url='/login/')
def deleteCart(request, id):
	cart.objects.filter(idsp=id).delete()
	messages.warning(request, 'bạn vừa xóa sp trong giỏ')
	return redirect('shop:viewCart')

class loginUser(View):
	def get(self, request):
		login_form = loginForm
		return render(request, 'shop/login.html', {'login_form':login_form})

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None :
			login(request, user)
			return redirect('shop:listproduct')
		else:
			pass

def logoutUser(request):
	logout(request)
	return redirect('shop:listproduct')

class signupUser(View):
	def get(self, request):
		signup_Form = signupForm
		return render(request, 'shop/signup.html', {'signup_Form':signup_Form})
	def post(self, request):
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		re_password = request.POST['re_password']

		if password==re_password:
			user = User.objects.create_user(username, email, password)
			user.save()
			return redirect('shop:login')

		else:
			messages.warning(request, 'vui lòng nhập mật khẩu trùng khớp nha bạn')
			return redirect('shop:signup')



