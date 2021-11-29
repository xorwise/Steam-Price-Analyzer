from .models import Skin
import requests
import json
import time
from django.db import transaction
from bs4 import BeautifulSoup
from currency_converter import CurrencyConverter


def proxy_check(proxy_list):
    for i, proxy in enumerate(proxy_list):
        proxies = {
            'http': f'http://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}',
            'https': f'http://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}'
        }
        try:
            response = requests.get('https://icanhazip.com/', proxies=proxies)
            print(proxies, 'OK')
        except:
            print(proxies, 'deleted')
            del proxy_list[i]
    return proxy_list

def price_api_upgrade_with_proxy():
    names = Skin().__class__.objects.all().values_list('name', flat=True)
    proxy_list = list()
    with open('D:/Programming/Visual Studio Code/Projects/Steam Price Analyzer/steam_analyzer/main/proxy_logins.txt') as proxy_file:
        for proxy in proxy_file.readlines():
            proxy_list.append(proxy.split(':'))
    proxy_list = proxy_check(proxy_list)
    print(len(proxy_list))
    proxies = {
        'http': f'http://{proxy_list[0][2]}:{proxy_list[0][3]}@{proxy_list[0][0]}:{proxy_list[0][1]}',
        'https': f'http://{proxy_list[0][2]}:{proxy_list[0][3]}@{proxy_list[0][0]}:{proxy_list[0][1]}'
    }
    
    for i, name in enumerate(names):
        if 'MAC-10 | Graven (Field-Tested)' in name:
            names = names[i:]
            break

    i = count = 1
    for name in names:
        if i == len(proxy_list) - 1:
            i = 0
        if count % 100 == 0:
            proxies = {
                'http': f'http://{proxy_list[i][2]}:{proxy_list[i][3]}@{proxy_list[i][0]}:{proxy_list[i][1]}',
                'https': f'http://{proxy_list[i][2]}:{proxy_list[i][3]}@{proxy_list[i][0]}:{proxy_list[i][1]}'
            }
            i += 1
            print(proxies['http'])
        
        name_fixed = name.replace('\n', '')
        print(name_fixed, end=' ')
        url = f'https://steamcommunity.com/market/priceoverview/?currency=5&appid=730&market_hash_name={name_fixed}'
        response = requests.get(url, proxies=proxies)
        try:
            content = response.content.decode(encoding=response.encoding)
        except:
            time.sleep(3)
            continue
        data = json.loads(content)
        if type(data) != type(None):
            if data.get('lowest_price') is not None:
                print('saved...')
                obj = Skin().__class__.objects.get(name=name)
                obj.current_price = data.get('lowest_price')
                obj.save()
            else:
                print('failed')
        else:
            proxies = {
                'http': f'http://{proxy_list[i+1][2]}:{proxy_list[i+1][3]}@{proxy_list[i+1][0]}:{proxy_list[i+1][1]}',
                'https': f'http://{proxy_list[i+1][2]}:{proxy_list[i+1][3]}@{proxy_list[i+1][0]}:{proxy_list[i+1][1]}'
            }
            i += 1
            print('blocked...')
            print(count - 1)
        
        count += 1
        time.sleep(3)