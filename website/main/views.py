from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

 
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('home')  # Redirect to a success page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


User  = get_user_model()

 