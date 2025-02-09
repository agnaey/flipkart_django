from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('login', views.login ,name='login'),
    path('logout', views.logout),
    path('register',views.register),
    path('',views.fake_index,name='fake_index'),
    path('fake_sec/<id>',views.fake_sec),
    path('fake_demo/<id>',views.fake_demo),
    path('fake_see_more/<a>',views.fake_see_more),
    path('fake_search/', views.fake_search, name='fake_search'),

    # ----------------------admin--------------------------------------

    path('admin_home', views.admin_home),
    path('search_admin/', views.search_admin, name='search_admin'),

    path('add_pro', views.add_product),
    path('category/<id>',views.category,name='category'),
    path('delete_pro/<id>', views.delete_product),
    path('edit_pro/<id>', views.edit_product),
    path('edit_category/<id>', views.edit_category,name='edit_category'),
    path('del_cat/<category_id>', views.del_category),
    path('admin_booking', views.admin_bookings ,name='admin_booking'),
    path('view_pro',views.view_pro),
    path('cancel_order/<id>',views.cancel_order),
    path('confirm_order/<order_id>', views.confirm_order, name='confirm_order'),
    path('product_details/<id>',views.pro_details),
    path('demo2/<id>',views.demo2),
    # ----------------------user--------------------------------------

    path('index', views.index),
    path('search/', views.search, name='search'),
    path('address_page/<id>', views.address_page),
    path('cart_address/<id>', views.cart_address),
    path('sec/<id>', views.secpage,name='sec'),
    path('add_to_cart/<pid>', views.add_to_cart),
  path('add_quantity/<int:category_id>/', views.add_quantity, name='add_quantity'),
    path('remove_quantity/<int:category_id>/', views.remove_quantity, name='remove_quantity'),    path('cart_disp', views.cart_display,name='cart_disp'),
    path('delete_cart/<id>', views.cart_delete),
    path('delete_all', views.delete_all,name='delete_all'),

    path('cart_buy/<id>',views.cart_buy),
    path('buy_product/<id>',views.buy_pro),
    path('user_vew_booking',views.view_bookings),
    path('delete_order/<id>',views.delete_order),
    path('orders/', views.user_orders, name='user_orders'),
    path('confirm_order/<order_id>', views.confirm_order),
    path('see_more/<a>',views.see_more),
    path('demo/<id>',views.demo),

    path('order_payment', views.order_payment, name='order_payment'),
    path('callback/', views.callback, name='callback'),
    # path('demo1/<id>',views.demo1),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_form.html', extra_context={'reset_done': True}), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_form.html', extra_context={'reset_complete': True}), name='password_reset_complete'),
    
]