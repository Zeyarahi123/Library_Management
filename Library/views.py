from typing import Dict

from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from .models import BooksModel
from .forms import BooksForm,RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.template import context

# Create your views here.
def Home(request):
    return render(request,"Home.html")

def insert_Book(request):

    context={}
    form=BooksForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"]=form
    return render(request,"insert_Book.html",context)



def list_Book(request):
    datasets=BooksModel.objects.all()
    return render(request, "list_Book.html",{"dataset":datasets})

def detail_Book(request):
    context= {}
    context['data']=BooksModel.objects.get(id=id)

    return render(request, "detail_Book.html", context)




#update Books_details
def update_Book(request,id):
    context={}
    obj=get_object_or_404(BooksModel,id=id)

    form=BooksForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    context["form"]=form

    return render(request, "update_Book.html", context)




#delete Books_details
def delete_Book(request, id):

    context = {}
    obj = get_object_or_404(BooksModel, id=id)

    if request.method=="POST":
         obj.delete()


         return HttpResponseRedirect("/")

    return render(request, "delete_Book.html", context)




def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        # we are checking wheather password1 is same as password2 or nor(password1==password2)

        if password1 == password2:
            if User.objects.filter(username=username).exists():  # it will check wheather same username is available or not in database
                # print("User_Name is already available") #it will print on terminal
                messages.info(request, 'User_Name is already taken')  # it will give message on same form
                return redirect('registration')  # it will send again to register form

            elif User.objects.filter(email=email).exists():  # it will check same email is available in database or not
                # print("Email is already available")    #it will print on terminal
                messages.info(request, 'Email is already taken')  # it will give message on same form
                return redirect('registration')  # it will send again to register form

            else:
                user = User.objects.create_user(username=username, password=password1, email=email,name=name)
                user.save();
                # print("Created SuccessFully")    #it will print on terminal
                messages.info(request, 'User Created SuccessFully')  # it will give message on same form
                return redirect("login")
        else:
            # print("Password Not Matching")   #it will print on terminal
            messages.info(request, 'Password is Not Matching')  # it will give message on same form
            return redirect('registration')  # it will send again to register form
    else:

        return render(request, "registration.html")



def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user= authenticate(request, username=username, password=password)

        if user is not None:
             auth.login(request, user)
             return redirect("Home.html") #it will redirect to home page
        else:
            messages.info(request,"Invalid User_Name or Password")
            return redirect('login')

    else:

        return render(request, "login.html")

