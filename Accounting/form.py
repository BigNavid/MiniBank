from django import forms


class AddIncomeSource(forms.Form):
    name = forms.CharField(max_length=255, required=True, label='نام شرکت')
    amount = forms.IntegerField(required=True, label='حقوق')
    days = forms.IntegerField(required=True, label='بازه پرداختی')


class AddCreditCard(forms.Form):
    owner_full_name = forms.CharField(required=True, label='نام')
    id = forms.IntegerField(required=True, label='شماره کارت')


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


class CheckLeaf(forms.Form):
    source_creditcard = forms.IntegerField(required=True, label='شماره کارت')
    destination_creditcard = forms.IntegerField(required=True, label='شماره کارت مقصد')
    amount = forms.IntegerField(required=True, label='مبلغ')
    date_time = forms.DateField(required=True, label='تاریخ')


class LoanPayment(forms.Form):
    destination_creditcard = forms.IntegerField(required=True, label='شماره کارت مقصد')
    amount = forms.IntegerField(required=True, label='مبلغ')
    date_time = forms.DateField(required=True, label='تاریخ')



