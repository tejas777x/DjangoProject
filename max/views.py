from django.core.mail import send_mass_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Seller, Name, Electronics, UserProfileInfo
from .forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect  # importing decorator to exempt csrf protection



# view to send mail to seller and buyer
def subscribe(request):
    mail_id= request.GET.get('Seller_id')  # requesting mail id of sellers
    mail= Seller.objects.filter(name=mail_id).values_list('email_id', flat=True).last() # query to filter mail id of the selected seller
    emails = User.objects.filter(username=request.user).values_list('email', flat=True).last() # query to get mail id of the user
    message1 = ('PRODUCT', 'Successfully purchased the product', 'madatmmax@gmail.com', [emails]) # message to be send to the buyer
    message2 = ('BUYER', 'Found a seller for the product', 'madatmmax@gmail.com', [mail]) # message to be send to the seller
    send_mass_mail((message1, message2), fail_silently=False)  # function to send mass email
    return render(request, 'success.html')


# view to populate Select_Electronics.html
def test(request):
    nex = Electronics.objects.all()  # query to get all the object of Electronics module
    context = {
        "max": nex
    }
    nam = Name.objects.all() # query to get all the objects of Name module
    context = {
        "typ": nam
    }
    return render(request, 'Select_Electronics.html', locals())


@csrf_exempt # decorator to exempt csrf token
# view to populate the  confirmation.html
def load_list(request):
    id = request.GET.get('Seller_id')  # query to get seller_id from Seller module
    list = Seller.objects.filter(srno=id)  # query to filter the selected seller details
    c = UserProfileInfo.objects.filter(user=request.user).values_list('mobile_no', flat=True).last() # query to get the users mobile number
    w = UserProfileInfo.objects.filter(user=request.user).values_list('address', flat=True).last() # query to get the users address
    return render(request, 'confirmation.html', {"list": list, "c": c, "w": w})

# view to populate the drop down box in Select_Electronics.html
def load_electronics(request):
    category_id = request.GET.get('name_type_id')  # query to get name_type from Name module
    electronics = Electronics.objects.filter(name_type_id=category_id)   # query to filter selected name_type
    return render(request, 'electronics_dropdown.html', {'nex': electronics})


# view for the table present in Select_Electronics.html
def load_seller(request):  # function to load seller details in the table
    electronics_id = request.GET.get('model_seller_id')  # get the id of the selected seller
    sellers = Seller.objects.filter(model_seller_id=electronics_id).order_by('price')  # to filter the selected seller from other sellers
    return render(request, 'table.html', {'sell': sellers})


# view for index.html page
def index(request):  # function to render index.html page
    return render(request, 'index.html')



@login_required  # to render page after user gets login
# view to render Select_Electronics.html page
def special(request):
    return render(request, 'Select_Electronics.html')


# view for logout function present in base.html
@login_required
# to render page after user gets login
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



# view to define registration page
def register(request):
    registered = False
    if request.method == 'POST':  # if request to register details in registration form
        user_form = UserForm(data=request.POST)  # to post the data to the inbuilt django user form
        profile_form = UserProfileInfoForm(data=request.POST)  # to post data to the UserProfileInfo form
        if user_form.is_valid() and profile_form.is_valid(): # condition for if user entered correct details
            user = user_form.save()
            user.set_password(user.password)  # to set password
            user.save() # to save the user in database
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'mobile_no' in request.FILES:  # to register  mobile number
                print('found it')
                profile.mobile_no=request.FILES['mobile_no']
            profile.save()  # save the overall details in registration form
            registered=True
        else:  # if user entered invalid details
            print(user_form.errors, profile_form.errors)
    else: # condition to render login.html page
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


# view to render login page
# view to define login function
def user_login(request):
    if request.method == 'POST':  # if user wants to login
        username = request.POST.get('username')  # enter the username
        password = request.POST.get('password') # enter the password
        user = authenticate(username=username, password=password)   # for authentication
        if user.is_active:  # condition for the user if logged in with correct login data
            login(request, user)
            return HttpResponseRedirect(reverse('index'))  # redirect to index.html page
        else: # condition for wrong login data
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else: # condition to render login.html page
        return render(request, 'login.html', {})


