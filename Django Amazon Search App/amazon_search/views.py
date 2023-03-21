import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

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
        #url = f'https://www.amazon.in/s?k={keyword}&crid=UECC134EG63U&sprefix={keyword}%2Caps%2C195&ref=nb_sb_noss_1'
        #url = f'https://www.amazon.com/s?k={keyword}'
        url = "https://www.amazon.com/iPhone-13-128GB-Pink-Unlocked/dp/B0BGQS8YV4/ref=sr_1_2?keywords=iphone&qid=1679393336&sr=8-2"
        response = requests.get(url,headers=HEADERS)
        soup = BeautifulSoup(response.text)
        #soup = soup.find('span', {'id': "productTitle"}).text.strip()
        #soup = BeautifulSoup(response.text, 'html.parser')
        products = []
        for product in soup.find_all('div', {'class': 's-result-item'}):
            name = product.find('h2').text.strip()
            price = product.find('span', {'class': 'a-price-whole'}).text.strip()
            image_url = product.find('img')['src']
            products.append({'name': name, 'price': price, 'image_url': image_url})
        products = ["Samsung","Apple"]
        return render(request, 'index.html', {'keyword': keyword, 'products': products})