from django import forms

class CartAddForm(forms.Form):
    """ adding new products to cart"""
    quantity = forms.IntegerField(min_value=1, max_value=9)
    