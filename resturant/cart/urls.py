from django.urls import path
from rest_framework.routers import DefaultRouter
from .api import viewsets
from .views import PayCallback

app_name = "cart"

router = DefaultRouter()
router.register('api/cart', viewsets.CartViewset, basename='cart')

urlpatterns = router.urls
urlpatterns = urlpatterns + [
    path('cart/pay/callback', PayCallback.as_view(), name='verify_transaction')
]
