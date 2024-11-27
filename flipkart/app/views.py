from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from . models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def login(req):
    if 'shop' in req.session:
        return redirect(admin_home)
    if 'user'in req.session:
        return redirect(index)
    else:
        if req.method=='POST':
            username=req.POST['username']
            password=req.POST['password']
            data=authenticate(username=username,password=password)
            if data:
                auth_login(req,data)
                if data.is_superuser:
                    req.session['admin']=username
                    return redirect(admin_home)
                else:
                    req.session['username']=username
                    return redirect(index)
            else:
                messages.warning(req, "username or password invalid.") 
            return redirect(login)
        else:
            return render(req,'login.html')
        
def logout(req):
    auth_logout(req)
    req.session.flush()
    return redirect(login)

def register(req):
    if req.method=='POST':
        email = req.POST.get('email', None) 
        username = req.POST.get('username', None)
        password = req.POST.get('password', None)
        try:
            messages.success(req,'successfully registered') 
            data=User.objects.create_user(first_name=username,username=email,email=email,password=password)
            data.save()
            return redirect(login)
        except:
            messages.warning(req,'user details already exits') 
            return redirect(register)   
    else:
        return render(req,'register.html')

    







# ----------------------------------admin------------------------------------------------------

def admin_home(req):
    if 'admin' in req.session:
        phones=Products.objects.filter(phone=True)
        dress=Products.objects.filter(dress=True)
        return render(req,'admin/admin_home.html',{'phones':phones,'dress':dress})
    else:
       return redirect(admin_home)
    
def add_product(req):
    if req.method == 'POST':
        pro_id = req.POST['pro_id']
        name = req.POST['name']
        price = req.POST['price']
        offer_price = req.POST['o_price']
        image = req.FILES['img']
        description = req.POST.get('description', '')
        highlights = req.POST.get('highlights', '')
        
        phone = 'phone' in req.POST
        dress = 'dress' in req.POST
        laptop = 'laptop' in req.POST
        others = 'others' in req.POST

        data = Products.objects.create(P_id=pro_id,name=name,price=price,offer_price=offer_price,image=image,
        description=description,highlights=highlights,phone=phone,dress=dress,laptop=laptop,others=others)
        data.save()
        return redirect(admin_home)
  
    return render(req, 'admin/add_product.html')



def delete_product(req,id):
    data=Products.objects.get(pk=id)
    url=data.image.url
    url=url.split('/')[-1]
    os.remove('media/'+url)
    data.delete()
    return redirect(admin_home)


# -----------------------------user-----------------------------------------------------

def index(request):
    phones=Products.objects.filter(phone=True)
    dress=Products.objects.filter(dress=True)
    return render(request, 'user/index.html',{'phones':phones,'dress':dress})

def secpage(request,id):
    product=Products.objects.get(id=id)
    phones=Products.objects.filter(phone=True)
    dress=Products.objects.filter(dress=True)
    return render(request, 'user/secpage.html',{'product':product,'phones':phones,'dress':dress})
def add_to_cart(req,pid):
    product=Products.objects.get(pk=pid)
    user=User.objects.get(username=req.session['username'])
    data=Cart.objects.create(user=user,product=product)
    data.save()
    return redirect(cart_display)
def cart_display(req):
    user=User.objects.get(username=req.session['username'])
    data=Cart.objects.filter(user=user)[::-1]
    return render(req,'user/cart.html',{'data':data})

def cart_delete(req,id):
    data=Cart.objects.get(pk=id)
    data.delete()
    return redirect(cart_display)

def buy_pro(req,id):
    product=Products.objects.get(pk=id)
    user=User.objects.get(username=req.session['username'])
    price=product.offer_price
    if isinstance(price, str): 
        price = float(price.replace(",", ""))
    data=Buy.objects.create(user=user,product=product,price=price)
    data.save()
    return redirect(view_bookings)

def view_bookings(req):
    user=User.objects.get(username=req.session['username'])
    data1=Buy.objects.filter(user=user)[::-1]
    return render(req,'user/user_bookings.html',{'data1':data1})

def delete_order(req,id):
    data=Buy.objects.get(pk=id)
    data.delete()
    return redirect(view_bookings)