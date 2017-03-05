from django.shortcuts import render
from Accounting.models import CreditCard
from .form import *


def ShowCreditCard(request):
    CreditCards = CreditCard.objects.all()
    context = {'CreditCards': CreditCards}
    return render(request, 'ShowCreditCard.html', context=context)




# created by mohammad
def add_income_source(request):
    if request.method == 'POST':
        form = AddIncomeSource(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AddIncomeSource()
    context = {'form':form}
    return render(request, 'add_income_source.html', context)



def show_costs_graphical(request):
    transactions = None
    #TODO: Uncomment this
    # transactions = Transaction.objects.all()
    context = {'CreditCards': transactions}
    return render(request, 'ShowCostsGraphical.html', context=context)
