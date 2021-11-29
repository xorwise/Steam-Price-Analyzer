import json
import requests


url = 'https://wiki.cs.money/weapons/cz75-auto/nitro'

proxies = {
    'http': f'http://rtbejxaa:p1gby5n0qv3o@45.192.155.84:7095',
    'https': f'http://rtbejxaa:p1gby5n0qv3o@45.192.155.84:7095'
}
count = 0
while True:
    response = requests.get(url)
    print(response, count)
    count += 1