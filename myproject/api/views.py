from django.shortcuts import render

# Create your views here.
def api_endpoints(request):
    # Display API documentation and available endpoints
    return render(request, 'api/api_endpoints.html')
