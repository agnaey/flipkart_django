from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from . models import *
import os
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def login(req):
    if 'admin' in req.session:
        return redirect(admin_home)
    if 'username'in req.session:
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
        username = req.POST['username']
        email = req.POST['Email']
        password = req.POST['password']
        send_mail('Flipkart','Flipkart Account Created Successfully',settings.EMAIL_HOST_USER,[email])
        try:
            data=User.objects.create_user(first_name=username,username=email,email=email,password=password)
            data.save()
            # messages.success(req, "User Registered Successfully")
            # return redirect(login)
        except:
            messages.warning(req,'user details already exits') 
            return redirect(register)   
    else:
        return render(req,'register.html')
    



# ----------------------------------admin------------------------------------------------------

def admin_home(req):
    product=Products.objects.all()
    categories = Categorys.objects.select_related('product')

    if 'admin' in req.session:
        phones = Products.objects.filter(phone=True)
        dress = Products.objects.filter(dress=True)
        laptop = Products.objects.filter(laptop=True)
        others = Products.objects.filter(others=True)

        # phone_categories = Categorys.objects.filter (phone_categories=True)
        # dress_categories = Categorys.objects.filter(dress_categories=True)
        # laptop_categories = Categorys.objects.filter(laptop_categories=True)
        # other_categories = Categorys.objects.filter (other_categories=True)

        context = {
            'product': product,
            'categories': categories,
            'phones': phones,
            'dress': dress,
            'laptop': laptop,
            'others': others,
            # 'phone_categories': phone_categories,
            # 'dress_categories': dress_categories,
            # 'laptop_categories': laptop_categories,
            # 'other_categories': other_categories,
        }
        return render(req, 'admin/admin_home.html', context)
    else:
        return redirect(admin_home)
    

def pro_details(req,id):
    product=Products.objects.get(pk=id)
    categories = Categorys.objects.filter(product=product)

    context = {
        'product': product,
        'categories': categories,
        'is_phone': product.phone,
        'is_dress': product.dress,
        'is_laptop': product.laptop
    }
    
    return render(req,'admin/product_details.html',context)
    
def add_product(req):
    if req.method == 'POST':
        pro_id = req.POST['pro_id']
        name = req.POST['name']
      
        if 'img' in req.FILES:
            image = req.FILES['img']        
        description = req.POST.get('description', '')
        highlights = req.POST.get('highlights', '')
        
        phone = 'phone' in req.POST
        dress = 'dress' in req.POST
        laptop = 'laptop' in req.POST
        others = 'others' in req.POST

        data = Products.objects.create(P_id=pro_id,name=name,image=image,description=description
        ,highlights=highlights,phone=phone,dress=dress,laptop=laptop,others=others)
        print(req.FILES)
        print(req.POST)

        data.save()
        return redirect('category',id=data.id)
    return render(req, 'admin/add_product.html')

def category(req, id):
    product = Products.objects.get(pk=id)

    if req.method == 'POST':
        storage = req.POST['storage']
        color = req.POST['color']
        price = req.POST['price']
        offer_price = req.POST['o_price']
        size = req.POST['size']

        category = Categorys.objects.create(product=product,storage=storage,color=color,price=price,offer_price=offer_price,size=size)
        return redirect('category' , id=id)

    return render(req, 'admin/category.html', {'product': product})

def edit_product(req,id):
    data=Products.objects.get(pk=id)
    if req.method == 'POST':
        pro_id = req.POST['pro_id']
        name = req.POST['name']
        image = req.FILES.get('img')
        description = req.POST.get('description', '')
        highlights = req.POST.get('highlights', '')
        
        phone = 'phone' in req.POST
        dress = 'dress' in req.POST
        laptop = 'laptop' in req.POST
        others = 'others' in req.POST
        print (image)
        if image:
            Products.objects.filter(pk=id).update(P_id=pro_id,name=name,image=image,
            description=description,highlights=highlights,phone=phone,dress=dress,laptop=laptop,others=others)
        else:
            Products.objects.filter(pk=id).update(P_id=pro_id,name=name,
            description=description,highlights=highlights,phone=phone,dress=dress,laptop=laptop,others=others)
        
        return redirect('edit_category',id=id)
    return render(req, 'admin/edit_product.html',{'data':data})

def edit_category(req, id):
    product = Products.objects.get(pk=id)
    categories = Categorys.objects.filter(product=product)

    if req.method == 'POST':
        storage = req.POST['storage']
        color = req.POST['color']
        price = req.POST['price']
        offer_price = req.POST['o_price']
        size = req.POST['size']
        category=req.POST['category']

        Categorys.objects.filter(pk=category).update(storage=storage,color=color,
            price=price,offer_price=offer_price,size=size
        )
        return redirect(admin_home)
    return render(req, 'admin/edit_category.html', {'product': product, 'categories': categories})

def del_category(req,id):
    data=Categorys.objects.get(id=id)
    data.delete()
    return redirect(admin_home)

def delete_product(req,id):
    data=Products.objects.get(pk=id)
    url=data.image.url
    url=url.split('/')[-1]
    os.remove('media/'+url)
    data.delete()
    return redirect(admin_home)

def admin_bookings(req):
    user=User.objects.all()
    data=Buy.objects.all()[::-1]
    category = Categorys.objects.select_related('product')
    is_phone = Products.objects.filter(phone=True)
    is_dress = Products.objects.filter(dress=True)
    is_laptop = Products.objects.filter(laptop=True)
    # others = Products.objects.filter(others=True)
    return render(req,'admin/admin_bookings.html',{'user':user,'data':data,'category':category,'is_phone':is_phone,'is_dress':is_dress,'is_laptop':is_laptop})

def cancel_order(req,id):
    data=Buy.objects.get(pk=id)
    data.delete()
    return redirect(admin_bookings)

def confirm_order(request, order_id):
    order = get_object_or_404(Buy, id=order_id)
    order.is_confirmed = True 
    order.save()
    return redirect(admin_bookings)

def view_pro(req):
        categories = Categorys.objects.select_related('product')

        is_phone = Products.objects.filter(phone=True)
        is_dress = Products.objects.filter(dress=True)
        is_laptop = Products.objects.filter(laptop=True)
        others = Products.objects.filter(others=True)
        for category in categories:
            print(category.product, category.storage, category.color, category.size)

        
        context = {
            'categories': categories,
            'is_phone': is_phone,
            'is_dress': is_dress,
            'is_laptop': is_laptop
        }

        return render(req,'admin/view_all_pro.html',context)

def toggle_confirmation(request, order_id):
        order = get_object_or_404(Buy, id=order_id)
        order.is_confirmed = True  
        order.save()
        return redirect('admin_bookings') 


# -----------------------------user-----------------------------------------------------

def index(request):
    phones = Products.objects.filter(phone=True).prefetch_related('categorys_set')
    dress = Products.objects.filter(dress=True).prefetch_related('categorys_set')
    laptop = Products.objects.filter(laptop=True).prefetch_related('categorys_set')
    others = Products.objects.filter(others=True).prefetch_related('categorys_set')


    return render(request, 'user/index.html', {'phones': phones,'dress': dress,'laptop': laptop,'others': others
    })
def secpage(request, id):
    log_user = User.objects.get(username=request.session['username'])
    product = Products.objects.get(id=id)
    category = Categorys.objects.filter(product=product)

    # Check if the product is in the user's cart
    # try:
    #     catr1 = Cart.objects.get(category=category, user=log_user)
    # except Cart.DoesNotExist:
    cart1 = None

    phones = Products.objects.filter(phone=True)
    dress = Products.objects.filter(dress=True)
    laptop = Products.objects.filter(laptop=True)
    # category_id = request.session.get('cat')
    # category_data = Categorys.objects.filter(pk=category_id).first() if category_id else None

    category_id=request.session.get('cat')

    f=0
    for i in category:
        if category_id:
            if i.pk==int(category_id):
                category_data = Categorys.objects.get(pk=category_id)
                f=1
    if f==0:
        category_data=None
    

    context = {
        'product': product,
        'categories': category,
        'is_phone': product.phone,
        'is_dress': product.dress,
        'is_laptop': product.laptop,
        'cart1': cart1,
        'phones': phones,
        'dress': dress,
        'laptop': laptop,
        'category_id':category_data
    }

    return render(request, 'user/secpage.html', context)
def demo(req,id):
    req.session['cat']=id
    category=Categorys.objects.get(pk=id)
    return redirect('sec',id=category.product_id)

# def demo1(req,id):
#     req.session['cat']=id
#     category=Categorys.objects.get(pk=id)
#     return redirect('cart_disp',id=category.product_id)





def add_to_cart(request, pid):
    log_user = User.objects.get(username=request.session['username'])
    # category_id =request.session['cat']=pid

    category = Categorys.objects.get(pk=request.session['cat'])  
    

    cart_item, created = Cart.objects.get_or_create(user=log_user,  category=category)
    if cart_item.quantity < 5:
        cart_item.quantity += 1
        cart_item.save()
    else:
        messages.warning(request, "Maximum quantity limit of 5 reached.")
    

    return redirect(cart_display) 

def add_quantity(request, category_id):
    category = Categorys.objects.get( id=category_id)
    
    cart_item, created = Cart.objects.get_or_create(user=request.user, category=category)
    
    if cart_item.quantity < 5:
        cart_item.quantity += 1
        cart_item.save()
    else:
        messages.warning(request, "Maximum quantity limit of 5 reached.")
    
    return redirect(cart_display)

    
def remove_quantity(request, category_id):
    category = Categorys.objects.get( id=category_id)
    
    cart_item = Cart.objects.filter(user=request.user, category=category).first()
    
    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            messages.warning(request, "Minimum quantity limit of 1 reached.")


    else:
            return redirect('cart_display')

    
    return redirect(cart_display)

def cart_display(req):
    user = User.objects.get(username=req.session['username'])
    data = Cart.objects.filter(user=user)[::-1]
    category = Categorys.objects.select_related('product')
    cart_items = Cart.objects.filter(user=req.user)
    cart_items = []
    grand_total_price = 0 
    grand_dis_price=0 

    for item in data:
        product_price = (item.category.offer_price)
        total_price = product_price * item.quantity 
        grand_total_price += total_price  

        dis_price=float(item.category.price)
        total_dis_price=dis_price*item.quantity
        grand_dis_price+=total_dis_price
        
        cart_items.append({
            'cart_obj': item,
            'total_price': total_price,
            'total_dis_price':total_dis_price
        })
    
    context = {
        'data': data,
        'categories': category,
        'cart_items': cart_items, 
        'total_price': total_price
    }
    return render(req, 'user/cart.html', context)



def cart_delete(req,id):
    data=Cart.objects.get(pk=id)
    data.delete()
    return redirect(cart_display)

def buy_pro(req,id):
    user = User.objects.get(username=req.session['username'])
   
    category = Categorys.objects.get(pk=req.session['cat'])  
    price = category.offer_price

    data = Buy.objects.create(user=user, category=category, price=price)
    data.save()

    return redirect(view_bookings)



def cart_buy(req, id):
    cart = Cart.objects.get(pk=id)

    
    category = Categorys.objects.select_related('product').filter(id=cart.category_id).first()

    if not category:
        return redirect('error_page') 
    
    total_price = category.offer_price * cart.quantity

    buy = Buy.objects.create(category=cart.category, user=cart.user, price=total_price)
    buy.save()



    return redirect(view_bookings)


def view_bookings(req):
    user = User.objects.get(username=req.session['username'])
    data1 = Buy.objects.filter(user=user).select_related('category', 'category__product')[::-1]
    category_id = [item.category.id for item in data1]

    categories = Categorys.objects.filter(id__in=category_id).select_related('product')

    # cart_items = Cart.objects.filter(user=user)
    # for booking in data1:
    #     cart_item = Cart.objects.filter(user=user, category=booking.category).first()
    #     quantity = cart_item.quantity if cart_item else 1
    #     price = float(booking.category.offer_price or booking.category.price)
    #     booking.total_price = price * quantity
    #     booking.quantity = quantity

    context = {
        'data1': data1,
        'categories': categories,
    }
    return render(req, 'user/user_bookings.html', context)


def confirm_order(order_id):
    order = Buy.objects.get(id=order_id)
    order.is_confirmed = True
    order.save()

def user_orders(request):
    user = User.objects.get(username=request.session['username'])
    orders = Buy.objects.filter(user=user)
    for order in orders:
        print(f"Order ID: {order.id}, Is Confirmed: {order.is_confirmed}")
    
    
    return render(request, 'user/user_bookings.html', {'data1': orders})

def delete_order(req,id):
    data=Buy.objects.get(pk=id)
    data.delete()
    return redirect(view_bookings)


def see_more(req, a=None):
    file_type = req.GET.get('type', a or 'default')

    if file_type == 'phone':
        files = Products.objects.filter(phone=True)
    elif file_type == 'dress':
        files = Products.objects.filter(dress=True)
    elif file_type == 'laptop':
        files = Products.objects.filter(laptop=True)
    elif file_type == 'others':
        files = Products.objects.filter(others=True)
    else:
        files = Products.objects.all()

    context = {'files': files, 'file_type': file_type}
    return render(req, 'user/see_more.html', context)



