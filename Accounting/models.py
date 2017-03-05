from django.db import models


class IncomeSource(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True, primary_key=True)
    amount = models.BigIntegerField()
    period = models.IntegerField()


class CreditCard(models.Model):
    id = models.BigIntegerField(db_index=True, unique=True, primary_key=True)
    owner_full_name = models.CharField(max_length=255)
    pass


class Transaction(models.Model):
    source_creditcard = models.ForeignKey(CreditCard, on_delete=models.CASCADE, related_name='TransactionSource')
    destination_creditcard = models.ForeignKey(CreditCard, on_delete=models.CASCADE, related_name='TransactionDestination')
    behalf = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    date_time = models.DateField(auto_now_add=True)


class CheckLeaf(models.Model):
    source_creditcard = models.ForeignKey(CreditCard, on_delete=models.CASCADE, related_name='CreditSource')
    destination_creditcard = models.ForeignKey(CreditCard, on_delete=models.CASCADE, related_name='CreditDestination')
    amount = models.BigIntegerField(default=0,blank=True,null=True)
    date_time = models.DateField(auto_now_add=True)


class LoanPayment(models.Model):
    destination_creditcard = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    date_time = models.DateField(auto_now_add=True)
