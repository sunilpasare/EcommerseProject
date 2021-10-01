from django.contrib import messages
from django.shortcuts import redirect, render
from .models import CustomUser, Customer, Seller
from .forms import CustomerCreationForm,SellerCreationForm
from django.contrib.auth import authenticate,login,logout

def RegisterView(request):
    form=CustomerCreationForm()
    if request.method == 'POST':
        form=CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name='Account/Register.html'
    context={'form':form}
    return render(request,template_name,context)

def LoginView(request):
    if request.method == 'POST':
        no=request.POST.get('mobile')
        p=request.POST.get('password')
        user=authenticate(username=no,password=p)
        if user and user.is_customer:
            login(request,user)
            return redirect('show')
        messages.error(request,'You are not a customer')
    template_name='Account/Login.html'
    context={}
    return render(request,template_name,context)
    
def ShowView(request):
    usr=Customer.objects.all()
    print(usr)
    tempalte_name='Account/Show.html'
    context={'user':usr}
    return render(request,tempalte_name,context)


def SellerRegisterView(request):
    form=SellerCreationForm()
    if request.method == 'POST':
        form=SellerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sellerlogin')
    template_name='Account/SellerRegister.html'
    context={'form':form}
    return render(request,template_name,context)

def SellerLoginView(request):
    if request.method == 'POST':
        no=request.POST.get('mobile')
        p=request.POST.get('password')
        user=authenticate(username=no,password=p)
        if user and user.is_seller:
            login(request,user)
            return redirect('sellershow')
        messages.error(request,'You are not a Seller')
    template_name='Account/SellerLogin.html'
    context={}
    return render(request,template_name,context)
    
def SellerShowView(request):
    usr=Seller.objects.all()
    print(usr)
    tempalte_name='Account/SellerShow.html'
    context={'user':usr}
    return render(request,tempalte_name,context)


