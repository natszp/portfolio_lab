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


def get_institutions(request):
    category_id = request.GET.get('category_id')
    if category_id:
        institutions = Institution.objects.filter(types=category_id)
    else:
        institutions = Institution.objects.all()

    return render(request, 'ajax_institution.html', context={'institutions':institutions})


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
        donations = Donation.objects.all()
        return render(request, 'form.html', context={ 'categories':categories, 'donations':donations})

    def post(self, request):
        form= DonationForm(request.POST)
        if form.is_valid():
            categories = form.cleaned_data['categories']
            quantity = form.cleaned_data['bags']
            institution = form.cleaned_data['organization']
            address = form.cleaned_data['address']
            phone_number = form.cleaned_data['phone']
            zip_code = form.cleaned_data['postcode']
            pick_up_date = form.cleaned_data['data']
            pick_up_time = form.cleaned_data['time']
            pick_up_comment = form.cleaned_data['more_info']
            Donation.objects.create(categories=categories, quantity=quantity, institution=institution,
                                    address=address, phone_number=phone_number, zip_code=zip_code,
                                    pick_up_date=pick_up_date, pick_up_time=pick_up_time, pick_up_comment=pick_up_comment)

            return render(request, 'form-confirmation.html', context={'form':form})
        return HttpResponse('sth went terribly wrong')

def get_institution(request):
    category_id = request.GET.get('category_id')
    if category_id:
        institutions = Institution.objects.filter(categories=Category.objects.get(pk=category_id))
    else:
        institutions = Institution.objects.all()

    return render(request, 'ajax_institution.html', context={'institutions':institutions})

def create_json(institution):
    inst_lst = []
    for item in institution:
        inst_lst.append({'id': item.id, 'name': item.name, 'category': item.type.id})
    return json.dumps({'institution': inst_lst})


class UserPersonalView(View):
    def get(self, request):
        donations = Donation.objects.all()
        return render(request, 'profil.html', context={'donations':donations})

