import requests
import random
from bs4 import BeautifulSoup as bs

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # get the HTTP response and construct soup object
    soup = bs(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return proxies
def get_session(proxies):
    # construct an HTTP session
    session = requests.Session()
    # choose one random proxy
    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session
proxies=[
    '23.94.98.201:8080',
    '139.99.237.62:80',
    '161.97.126.37:8118',
    '148.204.171.217:80',
    '49.0.2.242:8090',
    
    
    ]
for i in range(5):
    s = get_session(proxies)
    try:
        print("Request page with IP:", s.get("http://icanhazip.com", timeout=1.5).text.strip())
    except Exception as e:
        continue
