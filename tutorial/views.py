from django.shortcuts import redirect

# Create your views here.

def login_redirect_to_welcome_page(request):
    return redirect('account/')
