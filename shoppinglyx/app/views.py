from django.shortcuts import render
from django.views import View
from .models import Customer,Product,Cart,Orderplaced 
from .forms import CustomerRegistrationForm
from django.contrib import messages

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        Allcategory = Product.objects.all()
        return render(request, 'app/home.html',{'topwears':topwears,'bottomwears':bottomwears,'mobiles':mobiles, 'Allcategory':Allcategory})

class ProductDetailView(View):
    def get(self,request,pk):
        product= Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',{'product':product})


def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
    if data==None:
      mobiles = Product.objects.filter(category ='M' )
    elif data == 'OPPO' or data == 'Redmi' or data == 'Poco' or data == 'Realme':
      mobiles = Product.objects.filter(category ='M' ).filter(brand = data)
    elif data == 'Below20000':
      mobiles = Product.objects.filter(category ='M' ).filter(discounted_price__lt=20000)
    elif data == 'Above20000':
      mobiles = Product.objects.filter(category ='M' ).filter(discounted_price__gt=20000)
    return render(request, 'app/mobile.html', {'mobiles':mobiles})

def login(request):
 return render(request, 'app/login.html')

class CustomerRegistrationView(View):
    def get(self,request):
      form = CustomerRegistrationForm()
      return render(request,'app/customerregistration.html',{'form':form})
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
          messages.success(request,"Congratulations You have been Successfully Registered")
          form.save()
        return render(request,'app/customerregistration.html',{'form':form})

def checkout(request):
 return render(request, 'app/checkout.html')
