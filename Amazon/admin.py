from django.contrib import admin
from Amazon.models import *

# Register your models here.
admin.site.register(Orders)
admin.site.register(Customer)
admin.site.register(MfgToAccountNumber)
admin.site.register(AmazonOrderReport)
admin.site.register(TrackingNumbers)
admin.site.register(ZipCodes)


