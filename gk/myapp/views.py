from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Bills, BillDetails, Category, Product, CustomUser
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

@login_required(login_url='/myapp/login/')
def index(request):
    if not request.user.is_authenticated:
        redirect(login)
    
    user = request.user
    username = user.get_username()
    
    bill_id = Bills.objects.all().count() + 1
    bill = BillDetails.objects.filter(bill_id=bill_id).values()
    number_product = 0
    for x in bill:
        number_product += x['quantity']
    return render(request, 'index.html', {'username': username, "number_product": number_product})

def login(request):
    if request.user.is_authenticated:
        return redirect(index)
    
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if CustomUser.objects.filter(username = username).exists():
            user = CustomUser.objects.filter(username = username).values()
            if user[0]['password'] == password:
                response = render(request, 'index.html', {'username':username})
                response.set_cookie('username', username)
                return response
            else:
                context["messages"] = ["Username or Password is not correct"]
                messages.info(request, 'Passwords are not correct')
                return redirect(login)
        else:
            messages.info(request, 'Username is not exists')
            return redirect(login)
    else:
        return render(request, 'login.html')
 
def cart(request):
    bill_id = Bills.objects.all().count() + 1
    bill = BillDetails.objects.filter(bill_id = bill_id).values()
    products = []
    for x in bill:
        y = Product.objects.filter(id = x['id_product']).values()[0]
        item = dict()|y
        item['quantity'] = x['quantity']
        item['id'] = x['id']
        products.append(item)
    context = {'products': products}
    return render(request, 'cart.html', context)


def iphone(request):
    user = request.user
    username = user.get_username()
    # type = Category.objects.filter(name="Apple").values()[0]['id']
    type = 1
    products = Product.objects.filter(type=type)
    bill_id = Bills.objects.all().count() + 1
    bill = BillDetails.objects.filter(bill_id=bill_id).values()
    number_product = 0
    for x in bill:
        number_product += x['quantity']
    context = {'items': products, 'username': username, 'number_product': number_product}
    return render(request, 'iphone-product.html', context)

def samsung(request):
    user = request.user
    username = user.get_username()
    # type = Category.objects.filter(name="Samsung").values()[0]['id']
    type = 2
    products = Product.objects.filter(type=type)
    bill_id = Bills.objects.all().count() + 1
    bill = BillDetails.objects.filter(bill_id=bill_id).values()
    number_product = 0
    for x in bill:
        number_product += x['quantity']
    context = {'items': products, 'username': username, 'number_product': number_product}
    return render(request, 'samsung-product.html', context)

def oppo(request):
    user = request.user
    username = user.get_username()
    # type = Category.objects.filter(name="Oppo").values()[0]['id']
    type = 3
    products = Product.objects.filter(type=type)
    bill_id = Bills.objects.all().count() + 1
    bill = BillDetails.objects.filter(bill_id=bill_id).values()
    number_product = 0
    for x in bill:
        number_product += x['quantity']
    context = {'items': products, 'username': username, 'number_product': number_product}
    return render(request, 'oppo-product.html', context)

def google(request):
    user = request.user
    username = user.get_username()
    # type = Category.objects.filter(name="Google").values()[0]['id']
    type = 4
    products = Product.objects.filter(type=type)
    bill_id = Bills.objects.all().count() + 1
    bill = BillDetails.objects.filter(bill_id=bill_id).values()
    number_product = 0
    for x in bill:
        number_product += x['quantity']
    context = {'items': products, 'username': username, 'number_product': number_product}
    return render(request, 'google-product.html', context)

def nokia(request):
    user = request.user
    username = user.get_username()
    # type = Category.objects.filter(name="Nokia").values()[0]['id']
    type = 5
    products = Product.objects.filter(type=type)
    bill_id = Bills.objects.all().count() + 1
    bill = BillDetails.objects.filter(bill_id=bill_id).values()
    number_product = 0
    for x in bill:
        number_product += x['quantity']
    context = {'items': products, 'username': username, 'number_product': number_product}
    return render(request, 'nokia-product.html', context)

def add(request):
    bill_id = Bills.objects.all().count() + 1
    id_product = request.GET.get('id')
    if(BillDetails.objects.filter(bill_id=bill_id, id_product=id_product)).exists():
        x = BillDetails.objects.get(bill_id=bill_id, id_product=id_product)
        x.quantity += 1
        x.save()
    else:
        x = BillDetails(id_product=id_product, quantity=1, bill_id=bill_id)
        x.save()
    return JsonResponse({'status': True, 'data': 'Thành công'})
    
def update(request):
    id = request.GET['id']
    quantity = request.GET['quantity']
    x = BillDetails.objects.get(id=id)
    x.quantity = quantity
    x.save()
    return JsonResponse({'status': True, 'data': 'Thành công'})

def delete(request):
    id = request.GET.get('id')
    item = BillDetails.objects.get(id=id)
    item.delete()
    return JsonResponse({'status': True, 'data': 'Thành công'})

def pay(request):
    bill_id = Bills.objects.all().count() + 1
    # total = request.GET["total"]
    items = BillDetails.objects.filter(bill_id=bill_id).values()
    total = 0
    for item in items:
        y = Product.objects.filter(id = item['id_product']).values()[0]
        total += y['price']*item['quantity']
    bill = Bills(id=bill_id, total=total)
    bill.save()
    return JsonResponse({'status': True, 'data': 'Thành công'})

@login_required(login_url='/myapp/login/')
def logout(request):
    auth_logout(request)
    return redirect(login)

def logup(request):
    if request.user.is_authenticated:
        return redirect(index)
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pwd']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(logup)
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(logup)
            else:
                user = CustomUser(username=username, password=password, email=email)
                user.save()
                return redirect(login)
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(logup)
    else:
        return render(request, 'logup.html')