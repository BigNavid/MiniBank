from django import forms
from .models import *

class AddIncomeSource(forms.Form):
    name = forms.CharField(max_length=255, required=True, label='نام شرکت')
    amount = forms.IntegerField(required=True, label='حقوق')
    days = forms.IntegerField(required=True, label='بازه پرداختی')

    def save(self):
        name = self.cleaned_data['name']
        amount = self.cleaned_data['amount']
        days = self.cleaned_data['days']
        income_source = IncomeSource.objects.create(name)
        income_source.amount = amount
        income_source.period = days
        income_source.save()


class AddCreditCard(forms.Form):
    owner_full_name = forms.CharField(required=True, label='نام')
    id = forms.IntegerField(required=True, label='شماره کارت')

    def save(self):
        owner_full_name = self.cleaned_data['owner_full_name']
        id = self.cleaned_data['id']
        credit_card = CreditCard.objects.create(id)
        credit_card.owner_full_name = owner_full_name
        credit_card.save()


class Transaction(forms.Form):
    source_creditcard = forms.IntegerField(required=True, label='شماره کارت مبدا')
    destination_creditcard = forms.IntegerField(required=True, label='شماره کارت مقصد')
    behalf_choices=(
        ('loan', 'وام'),
        ('debt', 'قرض')
    )
    behalf = forms.ChoiceField(required=True, choices=behalf_choices, label='دلیل')
    amount = forms.IntegerField(required=True, label='مبلغ')
    date_time = forms.DateField(required=True, label='تاریخ')

    def save(self):
        transaction = Transaction.objects.create()
        source_credit_card = CreditCard.objects.get(id=self.cleaned_data['source_creditcard'])
        destination_credit_card = CreditCard.objects.get(id=self.cleaned_data['destination_creditcard'])
        transaction.source_creditcard = source_credit_card
        transaction.destination_creditcard = destination_credit_card
        transaction.behalf = self.cleaned_data['behalf']
        transaction.amount = self.cleaned_data['amount']
        transaction.date_time = self.cleaned_data['date_time']
        transaction.save()


class CheckLeaf(forms.Form):
    source_creditcard = forms.IntegerField(required=True, label='شماره کارت')
    destination_creditcard = forms.IntegerField(required=True, label='شماره کارت مقصد')
    amount = forms.IntegerField(required=True, label='مبلغ')
    date_time = forms.DateField(required=True, label='تاریخ')

    def save(self):
        check_leaf = CheckLeaf.objects.create()
        source_credit_card = CreditCard.objects.get(self.cleaned_data['source_creditcard'])
        destination_credit_card = CreditCard.objects.get(self.cleaned_data['destination_creditcard'])
        check_leaf.source_creditcard = source_credit_card
        check_leaf.destination_creditcard = destination_credit_card
        check_leaf.amount = self.cleaned_data['amount']
        check_leaf.date_time = self.cleaned_data['date_time']
        check_leaf.save()


class LoanPayment(forms.Form):
    destination_creditcard = forms.IntegerField(required=True, label='شماره کارت مقصد')
    amount = forms.IntegerField(required=True, label='مبلغ')
    date_time = forms.DateField(required=True, label='تاریخ')

    def save(self):
        loan_payment = LoanPayment.objects.create()
        destination_credit_card = CreditCard.objects.get(self.cleaned_data['destination_creditcard'])
        loan_payment.destination_creditcard = destination_credit_card
        loan_payment.amount = self.cleaned_data['amount']
        loan_payment.date_time = self.cleaned_data['date_time']
        loan_payment.save()
