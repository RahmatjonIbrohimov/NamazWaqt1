from django.shortcuts import render
from bs4 import BeautifulSoup
from requests import get


# Create your views here.
def home(request):
    # bs4 scraping
    url = "http://www.islom.uz"
    response = get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    element = soup.find('div', class_='in_header_p')

    result = element.text.split()
    return render(request, 'WaqtApp/index.html', {'vaqt': result})
