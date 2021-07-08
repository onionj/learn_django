from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'name'
                                      }))

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'email'
                                       }))

    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control',
                                     'placeholder': 'message'
                                     }))

    def clean_email(self):

        email = self.cleaned_data['email']

        if 'gmail.com' not in email:
            raise forms.ValidationError('باید ایمیل شما یک جیمیل باشد')

        return email


class LoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'user name'}))

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'password'}))


class RegisterForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'user name'}))

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'email'}))

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'password'}))

    password2 = forms.CharField(
        label='confirm password',
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'placeholder': 'confirm password'}))

    def clean_username(self):
        data = self.cleaned_data
        username = data.get('username')
        qr = User.objects.filter(username=username)
        if qr.exists():
            raise forms.ValidationError(
                'این نام کاربری قبلا استفاده شده است لطفا یک نام دیگر انتخاب کنید')

    def clean_email(self):
        data = self.cleaned_data
        email = data.get('email')
        qr = User.objects.filter(email=email)
        if qr.exists():
            raise forms.ValidationError(
                'این ایمیل قبلا استفاده شده است لطفا یک ایمیل دیگر انتخاب کنید')

    def clean_password(self):
        data = self.cleaned_data
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise forms.ValidationError('پسورد ها باید یکسان باشند')

        if len(password) < 8:
            raise forms.ValidationError('پسورد باید بزرگ تر از 8 کاراکتر باشد')
