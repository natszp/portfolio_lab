from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from my_app.forms import *
from my_app.models import *


class LandingPageView(View):
    def get(self, request):
        donation_counter = Donation.objects.all().count()
        organisation_counter = Institution.objects.all().count()

        institutions = Institution.objects.all()
        categories = Category.objects.all()

        # fundations = Institution.objects.filter(type='fundacja')
        # fundation= Institution.objects.filter(type='fundacja')
        #
        # organisations = Institution.objects.filter(type='organizacja').all()
        # organisation = Institution.objects.filter(type='organizacja')
        #
        # collections = Institution.objects.filter(type='zbiorka').all()
        # collection = Institution.objects.filter(type='zbiorka')
        #
        # institution_list = fundations
        # paginator = Paginator(institution_list, 5)
        #
        # page = request.GET.get('page')
        # pages = paginator.get_page(page)

        return render(request, 'index.html', context={'institutions': institutions, 'categories': categories,
                    'donation_counter': donation_counter, 'organisation_counter': organisation_counter})
                      #                                  'pages': pages})


def get_institution(request):
    type_id = request.GET.get('type_id')
    if type_id:
        institutions = Institution.objects.filter(type='fundacja')
    else:
        institutions = Institution.objects.all()

    return render(request, 'index.html', context={'institutions':institutions})



class RegisterUserView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        userForm = RegisterUserForm(request.POST)
        if userForm.is_valid():
            user = User()
            user.first_name = userForm.cleaned_data['name']
            user.last_name = userForm.cleaned_data['surname']
            user.email = userForm.cleaned_data['email']
            user.username = user.email
            user.password = userForm.cleaned_data['password']
            user.set_password(user.password)
            user.password2 = userForm.cleaned_data['password2']
            user.save()
        return render(request, 'login.html')

class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('landing_page')
            else:
                return render(request, "register.html", context={'form':form})
        return HttpResponse('something went terribly wrong')

class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('landing_page')

class AddDonationView(LoginRequiredMixin, View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'form.html', {'categories':categories})

class TestView(View):
    def get(self, request):
        return render(request, 'testowo.html')

