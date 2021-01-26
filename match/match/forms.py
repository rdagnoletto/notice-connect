from django import forms
from . import models

class CreateForm(forms.Form):
    # Defining fields in this form so we know when we get the request that valid data has been sent.
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

    date_of_birth = forms.DateField(
        label = "Date of birth (MM/DD/YYYY)",
        widget=forms.DateInput(format='%m/%d/%Y'),
        input_formats=('%m/%d/%Y', ),
        required = True
    )

class DeleteForm(forms.Form):
    # Integer field for pk of record user wants to delete.
    record_id = forms.IntegerField(
        label= "Record ID to Delete",
        required= True
    )
