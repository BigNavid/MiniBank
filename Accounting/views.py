from django.shortcuts import render

from Accounting.models import CreditCard


def ShowCreditCard(request):
    CreditCards = CreditCard.objects.all()
    context = {'CreditCards': CreditCards}
    return render(request, 'ShowCreditCard.html.html', context=context)