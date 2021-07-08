from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        "title": "صفحه ی اصلی",
        "content": "! به جنگو خوش آمدید"
    }
    if request.user.is_authenticated:
        context['new_content'] = 'this is new content'

    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "درباره ما",
        "content": "!!! اینجا جنگو است"
    }

    return render(request, "about_page.html", context)


def contact_page(request):
    contact_Form = ContactForm(request.POST or None)

    context = {
        "title": "تماس با ما",
        "content": "فرم تماس با ما",
        "form": contact_Form
    }
    if contact_Form.is_valid():
        contact_Form.cleaned_data
        print(contact_Form.cleaned_data)

    return render(request, "contact/view.html", context)


def login_page(request):

    print(f"user logged in: {request.user.is_authenticated}")

    login_form = LoginForm(request.POST or None)

    context = {
        "title": "ورود",
        "content": " ورود به حساب کاربری",
        "form": login_form
    }

    if login_form.is_valid():

        data = login_form.cleaned_data
        print(data)

        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')

        user = authenticate(
            request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            context['form'] = LoginForm()
            return redirect('/')

        else:
            print('login failed')

    return render(request, "auth/login.html", context)


# class
User = get_user_model()


def register_page(request):
    register_form = RegisterForm(request.POST or None)

    context = {
        "title": "ثبت نام",
        "content": "ساخت حساب کاربری",
        "form": register_form
    }

    if register_form.is_valid():

        username = register_form.cleaned_data.get('username')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')

        new_user = User.objects.create_user(
            username=username, email=email, password=password)
        print(new_user)
        return redirect('/')

    return render(request, "auth/register.html", context)
