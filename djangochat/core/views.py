# -- login functionality
from django.contrib.auth import login
# -----------------------------------------
from django.shortcuts import render, redirect

# -------import from core/form.py-------------------
from .forms import SignUpForm

# --------FRONTPAGE--------------------------------
def frontpage(request):
    return render(request, 'core/frontpage.html')

# -------SIGNUP------------------------------------
def signup(request):
    # form is clicked
    if request.method == 'POST':
        #create the new user (request.data)
        form = SignUpForm(request.POST)
        # checking the data inserted
        if form.is_valid():
            user = form.save()

            # authenticate the user
            login(request, user)
            # redirect to frontpage (in urls.py name="frontpage")
            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form':form})



