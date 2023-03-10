from django.urls import path
from customer import views

urlpatterns = [
    path('register/',views.SignupView.as_view(), name='signup'),
    path('login/',views.SigninView.as_view(), name='signin'),
    path('home/',views.IndexView.as_view(),name='home'),
    path('product/<int:id>',views.ProductDetailView.as_view(),name='product-detail'),
    path('products/<int:id>/carts/add',views.AddToCartView.as_view(),name='cart-add'),
    path('customer/carts/all',views.CartListView.as_view(),name='cart-list'),
    path('carts/<int:id>/change',views.CartRemoveView.as_view(),name='cart-change'),
    path('orders/add/<int:id>',views.MakeOrderView.as_view(),name="create-order"),
    path('orders/all',views.MyOrderView.as_view(),name='my-orders'),
    path('orders/<int:id>/change',views.OrderCancelView.as_view(),name='order-cancel'),
    path('offers/all',views.OfferProductsView.as_view(),name='offer-list'),
    path('reviews/<int:id>/add',views.ReviewCreateView.as_view(),name='review-add'),
    path('logout',views.signout_view,name='signout'),    #dont need to give .as_view() becoz signout_view is not a class it is a function
    
]