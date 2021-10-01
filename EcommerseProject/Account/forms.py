from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Customer, Seller


class CustomerCreationForm(UserCreationForm):
    name=forms.CharField(max_length=50)
    class Meta:
        model = CustomUser
        fields = ('mobile_no','email')

    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        nm=self.cleaned_data.get('name')
        customer = Customer.objects.create(user=user,name=nm)
        return user

class SellerCreationForm(UserCreationForm):
    company_name=forms.CharField(max_length=50)
    gst_no=forms.CharField(max_length=200)
    address=forms.CharField(max_length=1000)
    bank_account=forms.IntegerField()
    class Meta:
        model = CustomUser
        fields = ('mobile_no','email')

    def save(self):
        user = super().save(commit=False)
        user.is_seller = True
        user.save()
        a=self.cleaned_data.get('address')
        b=self.cleaned_data.get('bank_account')
        c=self.cleaned_data.get('company_name')
        g=self.cleaned_data.get('gst_no')
        customer = Seller.objects.create(user=user,company_name=c,gst_no=g,address=a,bank_account=b)
        return user


