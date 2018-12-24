# from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib import messages

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from users.forms import CustomUserCreationForm

class SignUp(View):

    form_class = CustomUserCreationForm
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Error")
        else:
            form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})
