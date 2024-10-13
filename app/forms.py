from django import forms

from .models import Item
from core.models import CustomUser


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['description',]


class ColorForm(forms.ModelForm):
    #colors = forms.ChoiceField(choices=CustomUser.COLORS, required=False, widget=forms.Select(attrs={"class":"form-control form-control-sm"}))
    class Meta:
        model = CustomUser
        fields = ['colors',]
