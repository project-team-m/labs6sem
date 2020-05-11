from django.contrib import admin
from .models import Account, DepositType, Deposit, CreditType, Credit


admin.site.register(Account)
admin.site.register(DepositType)
admin.site.register(Deposit)
admin.site.register(CreditType)
admin.site.register(Credit)
