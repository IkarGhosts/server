from django import forms


class AccountUserForm(forms.Form):
    username = forms.CharField(
        label='Login', max_length=150,
        widget=forms.widgets.TextInput(
            attrs={'class': 'field_username'}
        )
    )
    password = forms.CharField(
        max_length=250, 
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'field_password'}
        )
    )
