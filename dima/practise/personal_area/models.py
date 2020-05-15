from django.db import models
import django.utils.timezone
from random import randint
from django.contrib.auth.models import User


'''
Не дописаны репры
Добавить историю операций
'''


class Account(models.Model):
    number = models.CharField(max_length=32,
                              default=str(randint(100000000, 999999999)),
                              unique=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    date_open = models.DateTimeField(default=django.utils.timezone.now)

    def __repr__(self):
        return '<Object Account: id = {}, number = {}, balance = {}>'.format(self.id,
                                                                             self.number,
                                                                             self.balance)


class DepositType(models.Model):
    title = models.CharField(max_length=32, unique=True)
    percent = models.IntegerField()

    def __repr__(self):
        return '<Object DepositType: id = {}, title = {}, percent = {}>'.format(self.id,
                                                                                self.title,
                                                                                self.percent)


class Deposit(models.Model):
    type = models.ForeignKey(DepositType, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)


class CreditType(models.Model):
    title = models.CharField(max_length=32, unique=True)
    percent = models.IntegerField()

    def __repr__(self):
        return '<Object DepositType: id = {}, title = {}, percent = {}>'.format(self.id,
                                                                                self.title,
                                                                                self.percent)


class Credit(models.Model):
    type = models.ForeignKey(CreditType, on_delete=models.CASCADE)
    date_open = models.DateTimeField(default=django.utils.timezone.now)
    start_sum = models.IntegerField()
    loan = models.IntegerField()
