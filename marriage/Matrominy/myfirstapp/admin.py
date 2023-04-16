from django.contrib import admin
import datetime
from django.contrib.auth.models import User
from .models import *
#
# # Register your models here.

admin.site.register(Customer)
admin.site.register(Family_info)
admin.site.register(Religious)
admin.site.register(Professional_detail)
admin.site.register(Physical_details)
admin.site.register(Customer_expectation)
admin.site.register(Address)
admin.site.register(Photo_id)
admin.site.register(Image_gallary)
admin.site.register(Profile_feedback)
admin.site.register(System_feedback)