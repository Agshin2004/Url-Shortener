from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Url
from .bijective import idToShortURL

def home(request):
    last_ten_shortened = Url.objects.all().order_by('-id')[:10]

    if request.method == 'POST':
        long_url = request.POST.get('url')
        # Adding url to DB  
        initial_url_create = Url.objects.create(url=long_url)
        initial_url_create.shortened_url = idToShortURL(initial_url_create.id)
        initial_url_create.save()
        
        return render(request, 'shortener/home.html', {
            'initial_url': long_url,
            'shortened_url': initial_url_create.shortened_url,
            'last_ten_shortened': last_ten_shortened,
        })
    
    return render(request, 'shortener/home.html', {
        'last_ten_shortened': last_ten_shortened
    })


def redirect_me(request, shortened_url):
    url = Url.objects.get(shortened_url=shortened_url).url
    return HttpResponseRedirect(url)
