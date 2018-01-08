# -*- coding: utf-8 -*-
import scrapy
from scrapy import cmdline

from mySpider.items import FeizhuItem
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://sjipiao.fliggy.com/homeow/trip_flight_search.htm?depCity=SHA&arrCity=NKG&depDate=2017-12-27")


class FliggySpider(scrapy.Spider):
    name = 'fliggy'
    allowed_domains = ['sjipiao.fliggy.com']
    city_name = {'BJS': '北京', 'SHA': '上海', 'CAN': '广州', 'SZX': '深圳', 'CTU': '成都', 'HGH': '杭州',
                 'WUH': '武汉', 'TYN': '太原', 'SIA': '西安', 'CSX': '长沙', 'SHE': '沈阳', 'XMN': '厦门',
                 'NKG': '南京', 'WUX': '无锡', 'CKG': '重庆', 'TSN': '天津', 'NGB': '宁波', 'HFE': '合肥',
                 'KHN': '南昌', 'CGO': '郑州', 'CZX': '常州'}

    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.start_urls = [
            'https://sjipiao.fliggy.com/homeow/trip_flight_search.htm?depCity=SHA&arrCity=NKG&depDate=2017-12-27'
        ]

    def parse(self, response):
        # //*[@id="J_FlightListBox"]/div/table/tbody/tr/td/div/p[@class="airline-name"]/span/text()   航班信息
        # //*[@id="J_FlightListBox"]/div/table/tbody/tr/td/div/p[2]/text()   中型机
        driver.implicitly_wait(10)
        self.driver.get(response.url)
        try:
            element = WebDriverWait(self.driver, 10).until(
                self.driver.find_element_by_id('J_FlightListBox')
                # EC.presence_of_all_elements_located(By.CLASS_NAME, "flight-line")
            )
            for each in response.xpath('//*[@id="J_FlightListBox"]'):
                print each
                item = FeizhuItem()
                fno = each.xpath(
                    './div/table/tbody/tr/td[@class="flight-line"]/div/p[@class="airline-name"]/span/text()').extract()
                # company = each.xpath(
                #     './table/tbody/tr/td[@class="flight-line"]/div/p[@class="airline-name"]/span/text()').extract()
                acity = each.xpath('./div/table/tbody/tr/td[@class="flight-port"]/div/p[1]/text()').extract()
                dcity = each.xpath('./div/table/tbody/tr/td[@class="flight-port"]/div/p[2]/text()').extract()
                date = each.xpath('./div/table/tbody/tr/td[@class="flight-time"]/p[1]/text()').extract()
                price = each.xpath(
                    './div/table/tbody/tr/td[contains(@class,flight-price)]/span/span[@class="J_FlightListPrice"]/text()').extract()
                item['fno'] = fno[0]
                item['acity'] = acity[0]
                item['dcity'] = dcity[0]
                item['date'] = date[0]
                item['price'] = price[0]

            yield item
        finally:
            self.driver.quit()

# if __name__ == '__main__':
#     cmdline.execute('scrapy crawl fliggy'.split())
