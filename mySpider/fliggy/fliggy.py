#!/usr/bin/python
# -*- coding:utf-8 -*-
# 飞猪航班数据抓取 

import os, sys, time, re, json
import fliggy_config as cf
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

reload(sys)
sys.setdefaultencoding('utf-8')


class Fliggy(object):
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(__file__) + '\\fliggy.txt')
        self.err = 'Exception: Fliggy.'
        self.driver = None
        self.jsondata = cf.jsondata
        self.url = cf.url
        self.city = cf.city_name
        self.search_info = []
        self.print_debug = 1  # 大于0时输出脚本调试信息
        self.print_result = 0  # 大于0时输出航班抓取结果信息
        self.print_read = 0  # 大于0时读取并输出抓取数据

    def main(self):
        try:
            self.printf2('\n', '*' * 20, 'Begin', '*' * 20, '\n')
            dr = self.ptsdriver()
            self.printf('Webdriver:', dr)
            self.open_page(dr)
            jsdt = json.dumps(self.jsondata)
            if self.print_read > 0:
                self.save()
                self.read()
            self.printf2('*' * 20, 'End', '*' * 20, '\n')
            print jsdt
            self.printf2('\n')
            return jsdt
        except Exception as e:
            self.printf(self.err + 'main()', e)
        finally:
            if self.driver != None: self.driver.quit()

    def get_search_info(self):
        try:
            infos = sys.argv
            if len(infos) < 4: infos = ['', 'sha', 'nkg', time.strftime('%Y-%m-%d', time.localtime())]
            infos.remove(infos[0])
            len_infos = len(infos)
            if len_infos == 3:
                for i in range(len_infos):
                    info = infos[i]
                    if info.isalpha() or info.replace('-', '').isdigit():
                        pass
                    else:
                        break
            return infos
        except Exception as e:
            self.printf(self.err + 'get_search_info()', e)

    def get_url(self):
        try:

            infos = self.get_search_info()
            self.printf('SearchInfo:', infos)
            dcity = str(infos[0]).upper()
            acity = str(infos[1]).upper()
            ddate = str(infos[2])
            self.search_info = [dcity, acity, ddate]
            url = self.url + 'depCity=' + dcity + '&arrCity=' + acity + '&depDate=' + ddate
            self.printf('Get_URL:', url)
            return url
        except Exception as e:
            self.printf(self.err + 'get_url()', e)

    def open_page(self, dr=None):
        try:
            if dr == None: dr = self.driver
            url = self.get_url()
            dr.get(url)
            dr.implicitly_wait(10)
            self.printf('OpenURL:', url)
            self.flights(dr)
        except Exception as e:
            self.printf(self.err + 'open_page()', e)

    def tips_in(self, dr):
        try:
            tips = dr.find_element_by_class_name('tips-in')
            self.printf(tips.text)
            return True
        except Exception as e:
            return False

    # 所有航班列表
    def flights(self, dr):
        try:
            flights = None
            tips = self.tips_in(dr)
            self.printf('Tips-in-result:', tips)
            if tips == False:
                flight_box = self.elmt_flight_list_box(dr)
                self.printf('J_FlightListBox:', flight_box)
                if flight_box != None:
                    self.elmt_loading(dr)
                    flights = self.elmt_flight_list_item(dr, flight_box)
                    if flights == None:
                        lll = 'None'
                    else:
                        lll = len(flights)
                    self.printf('\n共计[', lll, ']个航班 ')
                    self.flight(flights)
        except Exception as e:
            self.printf(self.err + 'flights()', e)
        return flights

    def elmt_flight_list_box(self, dr):
        try:
            flight_box = None
            flight_box = WebDriverWait(dr, 5, 0.5).until(lambda d: d.find_element_by_id('J_FlightListBox'))
        except Exception as e:
            self.printf(self.err + 'elmt_flight_list_box()', e)
        return flight_box

    def elmt_flight_list_item(self, dr, flight_box):
        try:
            flights = None
            css_elmt = 'div[class="flight-list-item clearfix J_FlightItem"]'
            flights = WebDriverWait(dr, 10, 0.5).until(lambda d: d.find_elements_by_css_selector(css_elmt),
                                                       'flight-list-item.超时 ')
        except Exception as e:
            self.printf(self.err + 'elmt_flight_list_item()', e)
        return flights

    def elmt_loading(self, dr):
        try:
            flight_loading = None
            flight_loading = dr.find_element_by_id('J_DefaultLoading')
            for i in range(10):
                if flight_loading != None:
                    txt = flight_loading.text
                    self.printf('第 ', i + 1, ' 次: ', txt)
                else:
                    break
                i = i + 1
                if i > 9:
                    break
                else:
                    time.sleep(2)
        except Exception as e:
            self.printf(self.err + 'flight_loading()', e)

    # 循环定位单个航班
    def flight(self, flights):
        try:
            self.jsondata = {"flights": []}
            flights_list = self.jsondata['flights']
            count_flights = len(flights)
            for i in range(count_flights):
                self.printf('Flight', '-' * 40, i + 1)
                flight = flights[i]
                table = flight.find_element_by_tag_name('table')
                tbody = table.find_element_by_tag_name('tbody')
                tr = tbody.find_element_by_tag_name('tr')
                flt = self.flight_info(tr)
                flights_list.append(flt)
                self.print_flight(flt)
        except Exception as e:
            self.printf(self.err + 'flight()', e)

            # 航班详细信息

    def flight_info(self, tr):
        try:
            info_list = {}
            name, fno = self.flight_name_and_fno(tr)
            price = self.flight_price(tr)
            info_list['dcity'] = self.city[self.search_info[0]]
            info_list['acity'] = self.city[self.search_info[1]]
            info_list['date'] = self.search_info[2]
            info_list['company'] = name
            info_list['fno'] = fno
            info_list['price'] = price
        except Exception as e:
            self.printf(self.err + 'flight_info()', e)
        return info_list

    # 航空公司名称和航班号
    def flight_name_and_fno(self, tr):
        try:
            name, fno = '-', '-'
            td = tr.find_element_by_class_name('flight-line')
            div = td.find_element_by_tag_name('div')
            p = div.find_elements_by_tag_name('p')[0]
            info = p.find_element_by_tag_name('span').text
            name, fno = self.flight_fno(info)
        except Exception as e:
            self.printf(self.err + 'flight_name_and_fno()', e)
        return name, fno

    # 分割航空公司名称和航班号
    def flight_fno(self, info):
        try:
            name, fno = '-', '-'
            fno = ''.join(re.findall(r"[A-Za-z0-9]", info))
            name = info.replace(fno, '')
        except Exception as e:
            self.printf(self.err + 'flight_fno()', e)
        return name, fno

    # 机票价格
    def flight_price(self, tr):
        try:
            price = '-'
            td = tr.find_element_by_css_selector('td[class="flight-price J_FlightPriceWrap"]')
            span = td.find_element_by_tag_name('span')
            price = span.find_element_by_tag_name('span').text
        except Exception as e:
            self.printf(self.err + 'flight_price()', e)
        return price

    def now_day(self, st=None):
        if st == None: st = time.localtime()
        now_day = time.strftime('%Y-%m-%d', st)
        return now_day

    def ptsdriver(self):
        try:
            driver = webdriver.PhantomJS()
            self.driver = driver
            return driver
        except Exception as e:
            self.printf(self.err + 'driver()', e)

    def save(self):
        try:
            file = open(self.path, 'a+')
            file.truncate()
            file.write(str(self.jsondata))
            file.close()
        except Exception as e:
            self.printf(self.err + 'save()', e)

    def read(self):
        try:
            file = open(self.path, 'r')
            cots = file.readlines()
            file.close()
            dict = eval(cots[0])
            list = dict['flights']
            for i in range(len(list)):
                lst = list[i]
                self.print_flight(lst)
        except Exception as e:
            self.printf(self.err + 'read()', e)

    # 输出
    def print_flight(self, flt):
        try:
            # 基本信息输出
            self.printf2(' 出发城市: ', flt['dcity'])
            self.printf2(' 到达城市: ', flt['acity'])
            self.printf2(' 出发日期: ', flt['date'])
            # self.printf2(' 航空公司: ', flt['company'])
            self.printf2(' 航班号码: ', flt['fno'])
            self.printf2(' 机票价格: ', flt['price'])
            self.printf2('')
        except Exception as e:
            self.printf(self.err + 'print_flight()', e)

    def printf(self, *msg):
        try:
            if self.print_debug > 0:
                for i in range(len(msg)): print msg[i],
                print
        except Exception as e:
            print self.err + 'printf()', e

    def printf2(self, *msg):
        try:
            if self.print_result > 0:
                for i in range(len(msg)):
                    s = msg[i]
                    print s,
                print
        except Exception as e:
            print self.err + 'printf2()', e


if __name__ == "__main__":
    fy = Fliggy()
    fy.main()
