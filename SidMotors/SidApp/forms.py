from django import forms
from SidApp.models import Motors



class MotorsForm(forms.ModelForm):
    class Meta:
        model = Motors
        fields = [
                'Customer_Name',
                'Mobile_Number',
                'Reg_No',
                'Engine_Numer',
                'Bike_Model',
                'Color','Remarks',
                'Valid_From',
                'Valid_To'

        ]
