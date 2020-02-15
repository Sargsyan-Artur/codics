from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


def signup_view(request):
    form = SignUpForm(request.POST)
    print(request.POST)
    if form.is_valid():

        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        print('valid')
        return HttpResponseRedirect('/home/')
    else:
        print('else')
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})