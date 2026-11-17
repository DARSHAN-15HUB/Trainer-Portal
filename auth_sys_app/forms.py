
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Re-Enter Password'}
        )
    )

    class Meta:
        model = User

        fields = ['username', 'email', 'password']

        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Enter Username'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Enter Email'}
            ),
            'password': forms.PasswordInput(
                attrs={'placeholder': 'Enter Password'}
            )
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "Username already exists"
            )

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Email already exists"
            )

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 8:
            raise forms.ValidationError(
                'Password must be at least 8 characters'
            )

        having_uc = False
        having_lc = False
        having_digit = False

        for char in password:
            if char.islower():
                having_lc = True

            if char.isupper():
                having_uc = True

            if char.isdigit():
                having_digit = True

        if not having_lc or not having_uc or not having_digit:
            raise forms.ValidationError(
                'Password must contain one digit, '
                'one uppercase and one lowercase letter'
            )

        return password

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                self.add_error(
                    'confirm_password',
                    'Password Mismatch'
                )

        return cleaned_data

    def create(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return user


class UserLoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Username'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter Password'}
        )
    )
