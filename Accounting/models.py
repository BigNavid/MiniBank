from django.db import models


class Periods(models.Model):
    days = models.IntegerField(primary_key=True, unique=True, db_index=True)
    name = models.CharField(max_length=255)


class IncomeSource(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True,primary_key=True)
    amount = models.BigIntegerField()
    period = models.ForeignKey(Periods, on_delete=models.CASCADE)


class CreditCard(models.Model):
    id = models.BigIntegerField(db_index=True, unique=True, primary_key=True)
    owner_full_name = models.CharField(max_length=255)
    pass


class Transaction(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True, db_index=True)
    source_creditcard = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
    destination_creditcard = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
    behalf = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    date_time = models.DateField(auto_now_add=True)


class CheckLeaf(models.Model):
    checkleaf_id = models.BigIntegerField(primary_key=True, unique=True, db_index=True)
    source_creditcard = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
    destination_creditcard = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
    amount = models.BigIntegerField(default=0,blank=True,null=True)
    date_time = models.DateField(auto_now_add=True)


class LoanPayment(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True, db_index=True)
    destination_creditcard = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
    amount = models.BigIntegerField()
    date_time = models.DateField(auto_now_add=True)
