#!/usr/bin/python
# -*- coding:utf-8 -*-
# 抓取配置

# 页面URL及传参示例： 
url = 'https://sjipiao.fliggy.com/flight_search_result.htm?'
# JSON初始化数据 
jsondata = {"flights":[]}
# 出发城市
dcity = 'SHA'
# 到达城市
acity = 'NKG'
# 城市中文名及三字码
# city_name = {'BJS':u'北京', 'SHA':u'上海', 'CAN':u'广州', 'SZX':u'深圳', 'CTU':u'成都', 'HGH':u'杭州',
#            'WUH':u'武汉', 'TYN':u'太原', 'SIA':u'西安', 'CSX':u'长沙', 'SHE':u'沈阳', 'XMN':u'厦门',
#            'NKG':u'南京', 'WUX':u'无锡', 'CKG':u'重庆', 'TSN':u'天津', 'NGB':u'宁波', 'HFE':u'合肥',
#            'KHN':u'南昌', 'CGO':u'郑州', 'CZX':u'常州'}

city_name = {'BJS':'北京', 'SHA':'上海', 'CAN':'广州', 'SZX':'深圳', 'CTU':'成都', 'HGH':'杭州',
           'WUH':'武汉', 'TYN':'太原', 'SIA':'西安', 'CSX':'长沙', 'SHE':'沈阳', 'XMN':'厦门',
           'NKG':'南京', 'WUX':'无锡', 'CKG':'重庆', 'TSN':'天津', 'NGB':'宁波', 'HFE':'合肥',
           'KHN':'南昌', 'CGO':'郑州', 'CZX':'常州'}
