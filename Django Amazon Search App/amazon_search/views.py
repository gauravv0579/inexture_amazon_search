import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from autoscraper import AutoScraper

def search_keyword(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword')
        if not keyword:
            return render(request, 'index.html')
        HEADERS = {
            'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64)'
                           'AppleWebKit/537.36 (KHTML, like Gecko)'
                           'Chrome/44.0.2403.157 Safari/537.36'),
            'Accept-Language': 'en-US, en;q=0.5'
        }
        url = f'https://www.amazon.com/s?k={keyword}'
        response = requests.get(url,headers=HEADERS)
        soup = BeautifulSoup(response.text, 'html.parser')
        products = []
        for product in soup.find_all('div', {'class': 's-result-item'}):
            name = product.find('h2').text.strip()
            price = product.find('span', {'class': 'a-price-whole'}).text.strip()
            products.append({'name': name, 'price': price})
        return render(request, 'index.html', {'keyword': keyword, 'products': products})