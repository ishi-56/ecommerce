from django.urls import path
from . import views
from . import auth_views


urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',auth_views.signup,name='signup'),
    path('login/', auth_views.signin, name='login'),
    path('logout/', auth_views.signout, name='logout'),
    # path('total_cart_items/', views.total_cart_count, name='total_cart_items'),
    
    path('shop/<str:category>/', views.category_view, name='category_view'),
    path('cart/',views.cart,name='cart'),
    path('<slug:cat_slug>/<slug:prod_slug>/', views.product_view, name='product_view'),
    path('category/',views.category,name='category'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('update_quantity/', views.update_quantity, name='update_quantity'),
    path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    path('update_cart_total/', views.update_cart_total, name='update_cart_total'),
    path('checkout/',views.checkout,name="placeorder"),
    path('order_summary/',views.order_summary,name="order_summary"),
    
    
    path('shop/',views.shop,name='shop'),
]