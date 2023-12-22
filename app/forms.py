# from django import forms
# from .models import DynamicFormData

# dynamicformapp/forms.py
from django import forms
from .models import DynamicFormData
from django.core.validators import DecimalValidator

class DynamicFormDataForm(forms.ModelForm):
    # Use CharField for item
    item = forms.CharField(max_length=255, required=True)

    # Use DecimalField for price with DecimalValidator
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[DecimalValidator(max_digits=10, decimal_places=2)],
        required=True
    )




class DynamicFormDataForm(forms.ModelForm):
    class Meta:
        model = DynamicFormData
        fields = ['item', 'price']

DynamicFormDataFormSet = forms.modelformset_factory(DynamicFormData, form=DynamicFormDataForm, extra=1)



