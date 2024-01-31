from django.shortcuts import render, redirect
from .models import Shortner
from django.http import HttpResponseNotFound



from django.utils.crypto import get_random_string

def index(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        existing_mapping = Shortner.objects.filter(long_url=long_url).first()

        if existing_mapping:
            # If the long URL already exists, return the existing short code
            short_code = existing_mapping.short_code
        else:
            # Generate a unique short code
            short_code = get_random_string(length=8)  # Change the length as needed

            # Create a new mapping
            mapping = Shortner.objects.create(long_url=long_url, short_code=short_code)
        
        shortened_url = request.build_absolute_uri('/') + short_code
        return render(request, 'index.html', {'shortened_url': shortened_url})

    return render(request, 'index.html')



def redirect_to_long_url(request, short_code):
    try:
        mapping = Shortner.objects.get(short_code=short_code)
        return redirect(mapping.long_url)
    except Shortner.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')  # Render a 404 error page