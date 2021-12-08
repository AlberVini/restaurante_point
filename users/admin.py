from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import User
from .forms import ClientSignUpForm, UserChangeForm


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = ClientSignUpForm
    model = User
    """ if User.is_client():
        fieldsets = auth_admin.UserAdmin.fieldsets + (
            ("Extra fields", {"fields": ("data_nascimento", "endereco",)}),
            )
    elif User.is_restaurant():
        fieldsets = auth_admin.UserAdmin.fieldsets + (
            ("Extra fields", {"fields":("cnpj", "endereco")}),
        ) """
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Extra fields", {"fields": ("is_client", "is_restaurant")}),
        )