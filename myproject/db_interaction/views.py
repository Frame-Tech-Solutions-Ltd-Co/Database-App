from django.shortcuts import render

# Create your views here.

def database_records(request):
    # Retrieve and display database records
    return render(request, 'db_interaction/database_records.html')

def search_filter(request):
    if request.method == 'POST':
        # Handle search and filter form submission and display filtered records
        return render(request, 'db_interaction/search_filter.html')
    else:
        return render(request, 'db_interaction/search_filter.html')
