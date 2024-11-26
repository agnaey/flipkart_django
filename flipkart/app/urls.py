from django.urls import path
from . import views

urlpatterns = [

    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register',views.register),
    # ----------------------admin--------------------------------------

    path('admin_home', views.admin_home, ),

    # ----------------------user--------------------------------------

    path('index', views.index, ),
    path('sec/<id>', views.secpage),
    path('add_to_cart/<pid>', views.add_to_cart),
    path('cart_disp', views.cart_display),
    path('delete_cart/<id>', views.cart_delete),
]