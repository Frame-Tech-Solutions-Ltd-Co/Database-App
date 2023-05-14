from django.shortcuts import render

# Create your views here.
def record_details(request):
    # Retrieve and display record details
    return render(request, 'record_access/record_details.html')

def record_api_access(request):
    if request.method == 'POST':
        # Handle record API access form submission and grant access
        return render(request, 'record_access/record_api_access.html')
    else:
        return render(request, 'record_access/record_api_access.html')
