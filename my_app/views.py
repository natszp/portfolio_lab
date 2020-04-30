from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
import json
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

        fundacje = Institution.objects.filter(type='fundacja')
        organizacje = Institution.objects.filter(type='organizacja')
        lokalne_zbiorki = Institution.objects.filter(type='zbiorka')
        types = TYPES_OF_INSTITUTION
        categories = Category.objects.all()

        # institution_list = fundations
        # paginator = Paginator(institution_list, 5)
        # page = request.GET.get('page')
        # pages = paginator.get_page(page)

        return render(request, 'index.html', context={'fundacje': fundacje, 'organizacje':organizacje, 'zbiorki':lokalne_zbiorki,
                                                      'categories': categories,
                    'donation_counter': donation_counter, 'organisation_counter': organisation_counter, 'types':types})
                      #                                  'pages': pages})


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

class TestView(View):
    def get(self, request):
        fruits = request.GET.getlist('fruits')
        print(fruits)
        return render(request, 'testowo.html')

class AddDonationView(LoginRequiredMixin, View):
    def get(self, request):
        all_categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, 'form.html', context={'all_categories':all_categories, 'institutions':institutions})

    def post(self, request):
        form= DonationForm(request.POST)
        if form.is_valid():
            categories = form.cleaned_data['categories']
            quantity = form.cleaned_data['bags']
            institution = form.cleaned_data['organization']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            phone_number = form.cleaned_data['phone']
            zip_code = form.cleaned_data['postcode']
            dupa = form.cleaned_data['data']
            pick_up_time = form.cleaned_data['time']
            pick_up_comment = form.cleaned_data['more_info']
            new_donation = Donation.objects.create( quantity=quantity, institution=institution,
                                    address=address, city=city, phone_number=phone_number, zip_code=zip_code,
                                    pick_up_date=dupa, pick_up_time=pick_up_time, pick_up_comment=pick_up_comment)
            new_donation.categories.set(categories)
            new_donation.user = request.user
            new_donation.save()

            return render(request, 'form-confirmation.html', context={'form':form})

        return HttpResponse('sth went terribly wrong')

def get_institutions(request):

    list_of_id = request.GET.getlist('categories')
    print(list_of_id)
    print('test')

    if list_of_id :
        id_cat = Category.objects.filter(id__in=list_of_id)
        selected_institutions = Institution.objects.filter(categories__id__in=id_cat)
    else:
        selected_institutions = Institution.objects.all()
    return render(request, 'institution_list.html', context={'institutions': selected_institutions})


class UserPersonalView(View):

    def get(self, request):
        donations = Donation.objects.filter(user=request.user).order_by('pick_up_date')
        return render(request, 'profil.html', context={'donations': donations})

    def post(self, request):
        id = request.POST.get('donation')
        donation = Donation.objects.get(pk=id)
        donation.is_taken = True
        donation.save()
        return redirect('/profil/')

