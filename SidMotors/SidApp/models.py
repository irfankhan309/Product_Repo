from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Motors(models.Model):
    Customer_Name = models.CharField(max_length=40)
    Mobile_Number = models.CharField(max_length=10,
                                     validators=[MinLengthValidator(10)],
                                     help_text='Please Enter Valid 10 Digit Mobile Number,If Not Consumer Data Wil Not Save.')
    Reg_No = models.CharField(max_length=11)
    Engine_Numer = models.CharField(max_length=40)
    Bike_Model = models.CharField(max_length=35)
    Color = models.CharField(max_length=25)
    Remarks = models.TextField(max_length=159)
    Valid_From = models.DateTimeField()
    Valid_To = models.DateTimeField()
