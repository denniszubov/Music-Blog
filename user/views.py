from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, UserProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}. You are now able to login")
            return redirect("user-login")
    else:
        form = UserRegisterForm()
    return render(request, "user/register.html", {"form": form})


@login_required()
def profile(request):
    if request.method == "POST":
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        user_profile_update_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_update_form.is_valid() and user_profile_update_form.is_valid():
            user_update_form.save()
            user_profile_update_form.save()
            messages.success(request, f"Your account has been updated")
            return redirect("user-profile")
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        user_profile_update_form = UserProfileUpdateForm(instance=request.user.userprofile)

    context = {
        "user_update_form": user_update_form,
        "user_profile_update_form": user_profile_update_form,
    }
    return render(request, "user/profile.html", context)
