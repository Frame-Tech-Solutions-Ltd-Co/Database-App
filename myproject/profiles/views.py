from django.shortcuts import render

# Create your views here.
def user_profile(request):
    # Retrieve and display user profile information
    return render(request, 'profiles/user_profile.html')

def company_profile(request):
    # Retrieve and display company profile information
    return render(request, 'profiles/company_profile.html')
