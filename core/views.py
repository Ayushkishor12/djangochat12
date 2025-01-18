# from django.shortcuts import render,redirect
# from .forms import SignUpForm
# from django.contrib.auth import login
# # Create your views here.
# def frontpage(request):
#     return render(request, 'core/frontpage.html')

# def signup(request):
#     if request.method =='POST':
#         form=SignUpForm(request.POST)
        
#         if form.is_valid():
#             user=form.save()
            
#             login(request,user)
            
#             return redirect('frontpage')
#         else:
#             form=SignUpForm()
            
#         return render(request, 'core/signup.html', {'form':form})

from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user instance
            login(request, user)  # Log in the newly created user
            return redirect('frontpage')  # Redirect to the front page after signup
    else:
        form = SignUpForm()  # Instantiate an empty form for GET requests

    # Render the signup form for both GET requests and invalid POST submissions
    return render(request, 'core/signup.html', {'form': form})