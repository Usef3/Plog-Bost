from django.shortcuts import render
from .models import Profile
from .forms import UserRegistrationForm, UserEditForm, ProfileditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def dashboard(request):
    return render(request, "Authentication/dashboard.html", {"section": "dashboard"})


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(
                request, "Authentication/register_done.html", {"new_user": new_user}
            )
    else:
        user_form = UserRegistrationForm()
    return render(request, "Authentication/register.html", {"user_form": user_form})


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile has been ubdate successfully .")
        else:
            messages.success(request, "Error updaing your profile.")

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileditForm(instance=request.user.profile)

    return render(
        request,
        "Authentication/edit.html",
        {"user_form": user_form, "profile_form": profile_form},
    )
