from django import forms

from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'first_name', 'phone', 'address', 'oplata', 'buying_type', 'comment'
        )
