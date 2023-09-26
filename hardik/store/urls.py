from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('forget',views.forget,name="forget"),
    path('confirm_password',views.confirm_password,name="confirm_password"),
    path('logout',views.logout,name="logout"),
    path('blog_details',views.blog_details,name="blog_details"),
    path('blog',views.blog,name="blog"),
    path('check_out',views.check_out,name="check_out"),
    path('contact',views.contact,name="contact"),
    path('faq',views.faq,name="faq"),
    path('main',views.main,name="main"),
    path('product',views.product,name="product"),
    path('shop',views.shop,name="shop"),
    path('shopping_cart',views.shopping_cart,name="shopping_cart"),
    path('collection/<int:id>',views.collection,name="collection"),
    path('cart/<int:id>',views.cart,name="cart"),
    path('increment/<str:id>',views.increment,name="increment"),
    path('decrement/<str:id>',views.decrement,name="decrement"),
    path('apply_coupon',views.apply_coupon,name="apply_coupon"),
    path('remove/<str:id>',views.remove,name="remove"),
    path('order',views.order,name="order"),
    path('placeorder',views.placeorder,name="placeorder"),
    path('add_to_wishlist/<str:id>',views.add_to_wishlist,name="add_to_wishlist"),
    path('show_wishlist',views.show_wishlist,name="show_wishlist"),
    path('wishlist_remove/<str:id>',views.wishlist_remove,name="wishlist_remove"),
    path('remove_order/<str:id>',views.remove_order,name="remove_order"),
    path('profile',views.profile,name="profile"),
    
    path('search',views.search,name="search"),
    path('invoice',views.invoice,name="invoice"),
]