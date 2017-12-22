import requests
from bs4 import BeautifulSoup

# get proxies save to file(proxies.txt)
for page in range(1, 50):
    url = 'http://www.xicidaili.com/nn/%s' % page
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"
    headers = {'user-agent': user_agent}

    r = requests.get(url, headers=headers)
    print 'opening %s\n' % url

    soup = BeautifulSoup(r.content, 'lxml')
    # print soup.prettify()

    trs = soup.find('table', id='ip_list').findAll('tr')
    #   print trs[1]

    for tr in trs[1:]:
        tds = tr.findAll('td')
        ip = tds[1].text.strip()
        port = tds[2].text.strip()
        with open('proxies.txt', 'a') as f:
            f.write('http://%s:%s\n' % (ip, port))
        print 'Adding http://%s:%s to table' % (ip, port)
