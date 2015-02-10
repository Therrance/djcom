from django import forms
from djcom.catalog.models import Product

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product

    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('Price must be grreater than zero.')
        return self.cleaned_data['price']
