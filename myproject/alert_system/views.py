from django.shortcuts import render

# Create your views here.
def alerts(request):
    # Retrieve and display user alerts
    return render(request, 'alert_system/alerts.html')
