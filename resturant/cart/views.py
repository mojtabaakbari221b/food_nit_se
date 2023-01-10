from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from django_zarinpal.services import (
    verify_transaction
)
from django_zarinpal.signals import transaction_verified


class PayCallback(TemplateView):
    template_name = 'cart/callback.html'
    msg = None
    code = 0

    def get(self, request, *args, **kwargs):
        transaction = self._verify_transaction(request)
        self.verify_cart(transaction)
        return super().get(request, *args, **kwargs)
    
    def _verify_transaction(self, request):
        authority = request.GET.get("Authority")
        status = request.GET.get("Status")
        transaction = verify_transaction(status, authority)
        transaction_verified.send(sender=None, transaction=transaction)
        return transaction
    
    def verify_cart(self, transaction):
        if transaction.is_successful():
            cart = transaction.user.get_my_cart()
            cart.verify()
            self.set_successful_transaction()
            return
        
        self.set_unsuccessful_transaction()
    
    def set_successful_transaction(self):
        self.msg = 'successful paid'
        self.code = 200
    
    def set_unsuccessful_transaction(self):
        self.msg = 'invalid paid'
        self.code = 400
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            {
                'zarin_msg' : self.msg,
                'code' : self.code,
            },
        )

        return context