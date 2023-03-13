from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, SignupForm, UpdateProfileForm


class UsersLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'accounts/login.html'

def signup_view(request):
    form = SignupForm()
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Acoount created succesfully!')
            return redirect('user_login')

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

@login_required(login_url='user_login')
@user_passes_test(lambda user: user.is_superuser is False)
def userprofile_view(request):
    form = UpdateProfileForm(instance=request.user)

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, 'Profile updated successfully!')
            return redirect('user_profile')


    context = {'form': form}
    return render(request, 'accounts/profile.html', context)


class LogoutUser(LogoutView):
    template_name = 'accounts/logout.html'