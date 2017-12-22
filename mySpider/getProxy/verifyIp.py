import re
import requests
import threading

srcfile = open('proxies.txt', 'r')
outfile = open('verified.txt', 'w')

url = 'http://pv.sohu.com/cityjson?ie=utf-8'
user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"
headers = {'user-agent': user_agent}

mutex = threading.Lock()


def verify():
    try:
        mutex.acquire()
        proxy = srcfile.readline().strip()
        mutex.release()

        print proxy
        proxies = {'http': proxy}

        r = requests.get(url, proxies=proxies, headers=headers, timeout=5)
        print r.content

        mutex.acquire()
        outfile.write('%s\n' % proxy)
        mutex.release()

    except requests.RequestException, e:
        print e


childthread = []

for i in range(4900):
    t = threading.Thread(target=verify)
    childthread.append(t)
    t.start()

for t in childthread:
    t.join()

srcfile.close()
outfile.close()
