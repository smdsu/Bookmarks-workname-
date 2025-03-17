# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import render

# from django.http import HttpResponse

from .forms import UserRegistrationForm

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(
#                 request,
#                 username=cd['username'],
#                 password=cd['password'],
#             )
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(
#         request,
#         'account/login.html',
#         {
#             'form': form,
#         }
#     )


@login_required
def dashboard(request) -> HttpResponse:
    return render(
        request,
        'account/dashboard.html',
        {'section': 'dashboard',},
    )

def register(request) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user, but avoid saving at it
            new_user = form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                form.cleaned_data['password']
            )
            # Save the User object
            new_user.save()
            return render(
                request,
                'account/register_done.html',
                {'new_user': new_user}
            )
    else:
        form = UserRegistrationForm()
    return render(
        request,
        'account/register.html',
        {'form': form}
    )
