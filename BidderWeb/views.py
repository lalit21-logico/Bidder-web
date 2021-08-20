from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from BidderWeb.models import BWUser
from BidderWeb.models import *
from django.db.models import F
import random
from datetime import datetime

# Create your views here.
def home(request):
    data = product_data.objects.filter(auction_day_left__gte = 1).order_by('-product_id')
    datasold = product_data.objects.filter(auction_day_left = 0).order_by('-product_id')
    return render(request, 'home.html',{'data':data,'datasold':datasold})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')


def cart(request):
    if request.session.get('user_email') != None:
        cart_user_id =  request.session.get('user_id')
        data = cart_data.objects.filter(cart_user_id = cart_user_id,product_id__auction_day_left__gte = 1  ).order_by('-item_id')
        count = cart_data.objects.filter(cart_user_id = cart_user_id,product_id__auction_day_left__gte = 1  ).count()
        request.session['cart_count'] = count
        return render(request, 'cart.html',{'data':data})
    else:
        return render(request, 'login.html')


def contact(request):
    if request.session.get('user_email') != None:
        schedularDay()
        return render(request, 'contact.html')
    else:
        return render(request, 'login.html')

def product(request):
    if request.session.get('user_email') != None:
        product_id = request.GET['id']
        data = product_data.objects.filter(product_id = product_id)      
        return render(request, 'product.html',{'data':data})
    else:
        return render(request, 'login.html')

def sell(request):
    if request.session.get('user_email') != None:
        return render(request, 'sell.html')
    else:
        return render(request, 'login.html')

def activeList(request):
    if request.session.get('user_email') != None:
        data = product_data.objects.filter(auction_day_left__gte = 1).order_by('-product_id')
        return render(request, 'activeList.html',{'data':data})
    else:
        return render(request, 'login.html')

def orderList(request):
    if request.session.get('user_email') != None:
        cart_user_id =  request.session.get('user_id')
        data = cart_data.objects.filter(cart_user_id = cart_user_id,product_id__auction_day_left__lte = 0  ).order_by('-item_id')
        return render(request, 'orderList.html',{'data':data})
    else:
        return render(request, 'login.html')

def sellingList(request):
    if request.session.get('user_email') != None:
        user_id =  request.session.get('user_id')
        data = product_data.objects.filter(user_id = user_id ).order_by('-product_id')
        return render(request, 'sellingList.html',{'data':data})
    else:
        return render(request, 'login.html')

def watchList(request):
    if request.session.get('user_email') != None:
            user_id =  request.session.get('user_id')
            data = watchlist_data.objects.filter(watch_user_id=user_id).order_by('-watchlist_id')   
            return render(request, 'watchList.html',{'data':data})
    else:
        return render(request, 'login.html')

def addUser(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['re_password']:
            name = request.POST['name']
            email = request.POST['email']
            mobile = request.POST['mobile']
            address = request.POST['address']
            password = request.POST['password']
            count = BWUser.objects.filter(email = email).count()
            if count <= 0:
                BWUser(name = name, email = email, mobile = mobile, address = address,password = password).save()
                msg = "Account created Sucessfully Login Now"
                return render(request, 'login.html',{'msg':msg})
            else:
                msg = "Email already exisist"
            return render(request, 'signup.html',{'msg':msg})
        else:
            msg = "Password not match"
            return render(request, 'signup.html',{'msg':msg})
    else:
        return HttpResponse("<h1>404 -- Not Found </h1>")

def userLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        data = BWUser.objects.filter(email= email)
        counts = BWUser.objects.filter(email= email).count()
        if counts == 1:
            data=data[0]
            if data.password == request.POST['password']:
                cart_user_id =  data.ID
                count = cart_data.objects.filter(cart_user_id = cart_user_id,product_id__auction_day_left__gte = 1  ).count()
                request.session['user_id'] = data.ID
                request.session['user_email'] = data.email
                request.session['user_name'] = data.name
                request.session['cart_count'] = count
                return render(request, 'home.html')
            else:
                msg = "email or Password invalid"
                return render(request, 'login.html',{'msg':msg})
        else:
            msg = "email or Password invalid"
            return render(request, 'login.html',{'msg':msg})
    else:
        return HttpResponse("<h1>404 -- Not Found </h1>")

def logout(request):
    try:
        request.session['user_id'] = None
        request.session['user_email'] = None
        request.session['user_name'] = None
        request.session['cart_count'] = None
        print('del')
    except KeyError:
        pass
    return home(request)

def productUpload(request): 
    if request.method == 'POST' and request.FILES['myfile']:
        x = random.randint(999,10000)
        files = request.FILES['myfile']
        files.name = 'img'+str(x)+files.name
        title = request.POST['title']
        base_price = request.POST['basePrice']
        information = request.POST['information']
        user_ob = BWUser.objects.get(ID = request.session.get('user_id'))
        product_image = files
        auction_day_left = 10
        product_data(product_name = title, base_price = base_price,high_price = base_price, information = information, user_id = user_ob,product_image = product_image,auction_day_left=auction_day_left).save()    
    return sellingList(request)

def addWatchList(request):
    if request.session.get('user_email') != None:
        if request.method == 'GET':
            product_id = request.GET['id']
            watch_user_id =  request.session.get('user_id')
            pro = product_data.objects.get(product_id= product_id)
            watchlist_data(product_id = pro, watch_user_id = watch_user_id).save()
            data = watchlist_data.objects.filter(watch_user_id=watch_user_id).order_by('-watchlist_id')  
            return render(request, 'watchList.html',{'data':data})
    else:
        return render(request, 'login.html')

def removeWatchList(request):
    if request.session.get('user_email') != None:
        if request.method == 'GET':
            watchlist_id = request.GET['id']
            watch_user_id =  request.session.get('user_id')
            watchlist_data.objects.get(watchlist_id= watchlist_id).delete()
            data = watchlist_data.objects.filter(watch_user_id=watch_user_id).order_by('-watchlist_id')  
            return render(request, 'watchList.html',{'data':data})
    else:
        return render(request, 'login.html')


def placeBid(request):
    if request.session.get('user_email') != None:
        if request.method == 'POST':
            product_id = request.GET['id']
            data = product_data.objects.filter(product_id = product_id)
            pro = product_data.objects.get(product_id = product_id)
            buyer_id =  request.session.get('user_id')
            d = data[0]
            if str(d.high_price) <  request.POST['high_price']:
                cart_user_id =  request.session.get('user_id')
                count = cart_data.objects.filter(cart_user_id = cart_user_id,product_id__product_id = product_id).count()
                if count == 0:
                    cart_data(product_id = pro, my_price = request.POST['high_price'],cart_user_id = buyer_id ).save()
                else:
                    if count == 1:
                        cart_data.objects.filter(cart_user_id = cart_user_id,product_id__product_id = product_id).update(my_price=request.POST['high_price'])     
                product_data.objects.filter(product_id = product_id).update(high_price = request.POST['high_price'], buyer_id = buyer_id)
                cart_user_id =  request.session.get('user_id')
                count = cart_data.objects.filter(cart_user_id = cart_user_id,product_id__auction_day_left__gte = 1  ).count()
                request.session['cart_count'] = count
                return cart(request)
            else:
                msg = "Price is less or equal to High price"
                return render(request, 'product.html',{'data':data,'msg':msg})    
        return render(request, 'product.html',{'data':data})
    else:
        return render(request, 'login.html')


def schedularDay():
    d = datetime.now()
    count = schedular_flag.objects.filter(d = d.day, m= d.month, y=d.year).count()
    if count == 0:
        schedular_flag.objects.all().delete()
        schedular_flag(d = d.day, m= d.month, y=d.year).save()
        product_data.objects.filter(auction_day_left__gte = 1).update(auction_day_left = F('auction_day_left')-1)
    else:
        print("0")
    print("lalyt")




