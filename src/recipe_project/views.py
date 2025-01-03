from django.shortcuts import render, redirect
# Django authentication libraries
from django.contrib.auth import authenticate, login
# Django Form for authentication
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    # Init default error message
    error_message = None
    # Object with username and password fields
    form = AuthenticationForm()

    # When user hits 'login' button, POST request is generated
    if request.method == 'POST':
        # Read the data sent from the form
        form = AuthenticationForm(data=request.POST)

        # Check if form is valid
        if form.is_valid():
            # Read username and password
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

        # Validate user using Django auth
        user = authenticate(username=username, password=password)

        # Check if user is authenticated
        if user is not None:
            login(request, user)
            # Send user to desired page
            return redirect('sales:records')

    else:
        error_message = 'Something went wrong'

    # Prepare data to send from view to template
    context = {
        'form': form,
        'error_message': error_message
    }
    # Load login page with context info
    return render(request, 'auth/login.html', context)