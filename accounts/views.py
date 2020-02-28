from django.shortcuts import render, redirect


def welcome_page(request):
    numbers = [1,2,3,4,5]
    skills = "Blog"
    dictionary = {'numbers' : numbers, 'skills' : skills}
    return render(request, 'accounts/welcome.html', dictionary)


def about_profile(request):
    return render(request, 'accounts/about.html', {'user': request.user})








