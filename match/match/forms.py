from django import forms
from . import models

class CreateForm(forms.Form):

    first_name = forms.CharField(
		label = "First Name",
		max_length = 100,
		required = True
	)

    last_name = forms.CharField(
		label = "Last Name",
		max_length = 100,
		required = True
	)

    province = forms.CharField(
        label= "Province", 
        widget=forms.Select(choices=models.PROVINCES),
        required = True
    )

    date_of_birth = forms.DateField(required = True)

class DeleteForm(forms.Form):
    record_id = forms.IntegerField(
        label= "Record ID to Delete",
        required= True
    )
