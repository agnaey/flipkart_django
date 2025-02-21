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
    path('cart_address/', views.cart_address, name='cart_address'),  # For all items
    # path('cart_address/<id>/', views.cart_address, name='cart_address_single'),  # For single item
    path('sec/<id>', views.secpage,name='sec'),
    path('add_to_cart/<pid>', views.add_to_cart),
  path('add_quantity/<category_id>/', views.add_quantity, name='add_quantity'),
    path('remove_quantity/<category_id>/', views.remove_quantity, name='remove_quantity'),    
    path('cart_disp', views.cart_display,name='cart_display'),
    path('delete_cart/<id>', views.cart_delete),
    path('delete_all', views.delete_all,name='delete_all'),

    path('cart_buy/<id>',views.cart_buy),
    path('buy_product/<id>',views.buy_pro),
    path('user_vew_booking',views.view_bookings ,name='view_bookings'),
    path('delete_order/<id>',views.delete_order),
    path('orders/', views.user_orders, name='user_orders'),
    path('confirm_order/<order_id>', views.confirm_order),
    path('see_more/<a>',views.see_more),
    path('demo/<id>',views.demo),
    path('checkout_all', views.checkout_all, name='checkout_all'),
    path('pay', views.pay, name='pay'),
    path('cart_single_address/<id>',views.cart_single_address, name='cart_single_address'),
    path('single_buy/<id>',views.single_buy,name='single_buy'),
    path('delete_address/<int:id>/', views.delete_address, name='delete_address'),
    path('select_address/<int:id>/', views.select_address, name='select_address'),
    path('profile_view', views.profile_view, name='profile_view'),
    path('edit_address/<int:id>/', views.edit_address, name='edit_address'),
    path('delete_profile_address/<int:id>', views.delete_profile_address, name='delete_profile_address'),
    path('delete_account', views.delete_account, name='delete_account'),
    path("update_profile/", views.update_profile, name="update_profile"),
    path('add_address', views.add_address, name='add_address'),




    path('delete_cart_address/<int:id>/', views.delete_cart_address, name='delete_cart_address'),
    path('select_cart_address/<int:id>/', views.select_cart_address, name='select_cart_address'),

    path('delete_single_address/<int:id>/', views.delete_single_address, name='delete_single_address'),
    path('select_single_address/<int:id>/', views.select_single_address, name='select_single_address'),

    path('order_payment', views.order_payment, name='order_payment'),
    path('callback/', views.callback, name='callback'),

    path('order_payment2', views.order_payment2, name='order_payment2'),
    path('callback2/', views.callback2, name='callback2'),

    path('order_payment3/<id>', views.order_payment3, name='order_payment3'),
    path('callback3/', views.callback3, name='callback3'),
    # path('demo1/<id>',views.demo1),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_form.html', extra_context={'reset_done': True}), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_form.html', extra_context={'reset_complete': True}), name='password_reset_complete'),
    
]