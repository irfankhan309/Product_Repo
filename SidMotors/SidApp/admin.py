from django.contrib import admin
from SidApp.models import Motors


class MotorAdmin(admin.ModelAdmin):
    list_display =['Customer_Name',
                   'Mobile_Number',
                   'Reg_No',
                   'Engine_Numer',
                   'Bike_Model',
                   'Color',
                   'Remarks',
                   'Valid_From',
                   'Valid_To']



admin.site.register(Motors,MotorAdmin)
