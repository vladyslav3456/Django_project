from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib.auth import logout


def authentication(request):
    errors = None
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:home')
        errors = form.non_field_errors()
        form = AuthenticationForm()
        form.non_field_errors = lambda: errors
    else:
        form = AuthenticationForm()
    return render(request, 'users/authentication.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:home'))
