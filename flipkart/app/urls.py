from django.urls import path
from . import views

urlpatterns = [

    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register',views.register),
    # ----------------------admin--------------------------------------

    path('admin_home', views.admin_home),
    path('add_pro', views.add_product),
    path('delete_pro/<id>', views.delete_product),
    path('edit_pro/<id>', views.edit_product),
    path('admin_booking', views.admin_bookings),
    path('view_pro',views.view_pro),
    path('cancel_order/<id>',views.cancel_order),
    path('product_details/<id>',views.pro_details),

    # ----------------------user--------------------------------------

    path('index', views.index, ),
    path('sec/<id>', views.secpage),
    path('add_to_cart/<pid>', views.add_to_cart),
    path('cart_disp', views.cart_display),
    path('delete_cart/<id>', views.cart_delete),
    path('buy_product/<id>',views.buy_pro),
    path('user_vew_booking',views.view_bookings),
    path('delete_order/<id>',views.delete_order),
]