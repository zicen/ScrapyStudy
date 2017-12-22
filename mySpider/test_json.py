# -*- coding:utf-8 -*-
import json


def loadFont():
    f = open("doubantag.json", 'r')
    alljson = json.load(f)

    for each in alljson:
        url = each['tag_url']
        print url
    # family = setting['BaseSettings']['size']
    # size = setting['fontSize']
    return alljson


t = loadFont()

print t
