from django.shortcuts import render
from basic_app.forms import UserForm,UserContactForm
from basic_app.models import UserContacts
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request,'basic_app/registration.html',
                            {'user_form':user_form,
                            'registered':registered })

@login_required
def special(request):
    return HttpResponse("You are logged in!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed")
            print("Username:{} and password: {}".format(username,password))

            return HttpResponse("Invalid login details supplied")
    else:
        return render(request,'basic_app/login.html',{})


@login_required
def new_contact(request):

    if request.method == "POST":
        form = UserContactForm(request.POST)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return HttpResponseRedirect(reverse('basic_app:view_contact', kwargs={'contact_id':contact.id}))
        else:
            print('Error Form Invalid')
    else:
        form = UserContactForm()

    return render(request,'basic_app/create.html',{'form':form})

@login_required
def contact(request,contact_id):
    contact = get_object_or_404(UserContacts, id=contact_id, owner=request.user)

    return render(request,'basic_app/contact.html',{'contact':contact})

@login_required
def view_contacts(request):
    contacts = UserContacts.objects.filter(owner=request.user)
    count = contacts.count()
    my_dict = {'contacts':contacts,'number': count}

    return render(request,'basic_app/view_contacts.html',my_dict)


@login_required
def update_contact(request,contact_id):
    contact = get_object_or_404(UserContacts, id=contact_id, owner=request.user)

    if request.method == "POST":
        form = UserContactForm(request.POST, instance=contact)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return HttpResponseRedirect(reverse('basic_app:view_contact', kwargs={'contact_id':contact_id}))
        else:
            print('Error Form Invalid')
    else:
        form = UserContactForm(instance=contact)
    return render(request,'basic_app/update.html',{'form':form})


@login_required
def delete_contact(request,contact_id):
    contact = get_object_or_404(UserContacts, id=contact_id, owner=request.user)
    contact.delete()

    return HttpResponseRedirect(reverse('basic_app:view_contacts'))


