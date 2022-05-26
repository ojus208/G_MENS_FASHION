
from . import paytm as PaytmChecksum
import json
import requests
from dataclasses_json import Undefined
from django.http import request, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from itsdangerous import json
from .models import Offer_poster, Brand, Products_type, Products, auth_user, category_product
from django.views.decorators.csrf import csrf_exempt
from twilio.rest import Client
import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.conf import settings
from .models import Transaction



account_sid = 'AC159bf72e0da7b32743c938369db9bfaa'
auth_token = '76cfca110b1984bb7535d136f7ab5ca9'
client = Client(account_sid, auth_token)

# Create your views here.


def home(request):
    poster = Offer_poster.objects.all()
    brand = Brand.objects.all()
    product_type = Products_type.objects.all()
    cat = category_product.objects.all()
    products = Products.objects.all()
    if request.user.is_authenticated:
        user = auth_user.objects.filter(user=request.user)[0]
    else:
        user = None

    context_dict = {
        'posters': poster,
        'brands': brand,
        'pro_type': product_type,
        'category': cat,
        'products': products,
        'user': user
    }
    print(context_dict['user'])

    return render(request, "home.html", context_dict)


def category(request, title):
    cat = get_object_or_404(category_product, category=title)
    products = Products.objects.filter(category=cat)
    if request.user.is_authenticated:
        user = auth_user.objects.filter(user=request.user)[0]
    else:
        user = None

    return render(request, "type.html", {"products": products, "category": cat, 'user':user})


def type(request, title):
    cat = get_object_or_404(Products_type, title=title)
    products = Products.objects.filter(Product_type=cat)
    if request.user.is_authenticated:
            user = auth_user.objects.filter(user=request.user)[0]
    else:
        user = None

    return render(request, "type.html", {"products": products, "category": cat, "user": user})
    


def brand(request, title):
    cat = get_object_or_404(Brand, name=title)
    products = Products.objects.filter(company=cat)
    if request.user.is_authenticated:
            user = auth_user.objects.filter(user=request.user)[0]
    else:
        user = None


    return render(request, "type.html", {"products": products, "category": cat, "user": user})


def search(request):
    if request.method == "GET":
        query = request.GET.get("search_for")
        if query == "" or not query:
            return render(request, "explor.html")
        cat = category_product.objects.all()

        products = Products.objects.filter(
            title__icontains=query, subtitle__icontains=query)
        print(products)
        if request.user.is_authenticated:
            user = auth_user.objects.filter(user=request.user)[0]
        else:
            user = None
        
        return render(request, "search.html", {"products": products, "user":user})


def cart(request):
    if request.user.is_authenticated:
        user = auth_user.objects.filter(user=request.user)[0]
        print(user.user.username)
        return render(request, "cart.html", {'user': user})
    return render(request, "cart.html", {'user': None})


def favorite(request):
    products = Products.objects.all()
    if request.user.is_authenticated:
            user = auth_user.objects.filter(user=request.user)[0]
    else:
        user = None
    return render(request, "favorite.html", {"products": products, "user": user})


def product(request, title):
    pro = get_object_or_404(Products, title=title)
    products = Products.objects.all()
    images = pro.image.all()
    if request.user.is_authenticated:
            user = auth_user.objects.filter(user=request.user)[0]
    else:
        user = None

    return render(request, "product.html", {"product": pro, "images": images, "products": products, "user":user})


def user(request):
    if request.user.is_authenticated:
        user = auth_user.objects.filter(user=request.user)[0]
        return render(request, "user.html", {'user': user})
    return render(request, "user_auth.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse("invalid")
        auth_login(request, user)
        return redirect('user')
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


@csrf_exempt
def otp(request):

    if request.method == "POST":
        phone = request.POST.get('phone')
        otp = "".join(str(random.randint(0, 9)) for _ in range(6))
        respont = client.messages.create(
            messaging_service_sid='MG558627416573f90653834e32e75a9640',
            body=f'your OTP for gmf is{otp}',
            to=f'+91{phone}',
        )

        print(respont)
        return HttpResponse(otp)


@csrf_exempt
def signup(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        email = "ojusoni@gmail.com"
        user = User.objects.create_user(fname, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        authuser = auth_user(user=user, phone=phone)
        authuser.save()
        user = authenticate(username=fname, password=password)
        if user is None:
            return HttpResponse("error")

        auth_login(request, user)
        return redirect('home')


def logout(request):
    auth_logout(request)
    return redirect('user')


# def orderDetail(request):
#     if request.method == "POST":
#         pass
#     return HttpResponse("order")

# payment method paytm extemcton
@csrf_exempt
def initiate_payment(request):
    if request.method == "GET":
        return render(request, 'payments/pay.html')
    try:
        user = request.user
        # amount = int(request.POST.get['amount'])
        # order = request.POST.get['order']
        amount = int(100)
        order = "123"
        print(user)
        print(amount)
        print(order)

    except:
        print("error")
        return render(request, 'home.html', context={'error': 'Wrong Accound Details or amount'})

    transaction = Transaction.objects.create(
        made_by=user, amount=amount, order=order)
    transaction.save()
    merchant_key = settings.PAYTM_SECRET_KEY

    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', str(transaction.order_id)),
        ('CUST_ID', str(transaction.made_by.email)),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        # ('EMAIL', request.user.email),
        # ('MOBILE_N0', '9911223388'),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
        # ('PAYMENT_MODE_ONLY', 'NO'),
    )

    paytm_params = dict(params)
    checksum = PaytmChecksum.generate_checksum(paytm_params, merchant_key)
    
    transaction.checksum = checksum
    transaction.save()

    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)
    return render(request, 'redirect.html', context=paytm_params)


@csrf_exempt
def callback(request):
    if request.method != 'POST':
        return

    paytm_checksum = ''
    print(request.body)
    print(request.POST)
    received_data = dict(request.POST)
    print(received_data)
    paytm_params = {}
    paytm_checksum = received_data['CHECKSUMHASH'][0]
    for key, value in received_data.items():
        if key == 'CHECKSUMHASH':
            paytm_checksum = value[0]
        else:
            paytm_params[key] = str(value[0])
    if is_valid_checksum := PaytmChecksum.verify_checksum(
        paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum)
    ):
        print("Checksum Matched")
        received_data['message'] = "Checksum Matched"
    else:
        print("Checksum Mismatched")
        received_data['message'] = "Checksum Mismatched"

    return render(request, 'callback.html', context=received_data)


