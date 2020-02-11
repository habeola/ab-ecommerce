from django.urls import path
from .views import (
    Home, 
    ItemDetail, 
    CheckOut,
    add_item_to_cart,
    remove_item_from_cart,
    OrderSummary,
    remove_single_item_from_cart,
    PaymentView,
    AddCoupon,
    RequestRefund
    )

app_name = 'shopping'

urlpatterns = [
    path('', Home.as_view(), name='home-page'),
    path('product/<slug>/', ItemDetail.as_view(), name='product'),
    path('order-summary/', OrderSummary.as_view(), name='order-summary'),
    path('checkout/', CheckOut.as_view(), name='checkout-page'),
    path('add-item-to-cart/<slug>/', add_item_to_cart, name='add-item-to-cart'),
    path('remove-item-from-cart/<slug>/', remove_item_from_cart, name='remove-item-from-cart'),
    path('add-coupon/', AddCoupon.as_view(), name='add-coupon'),
    path('remove-single-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefund.as_view(), name='request-refund'),
]