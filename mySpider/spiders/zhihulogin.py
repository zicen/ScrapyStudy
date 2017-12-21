import scrapy
from scrapy import log


class ZhihuLoginSpider(scrapy.Spider):
    name = "zhihu.com"
    start_urls = ['https://www.zhihu.com/#signin']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'account': '1140377034@qq.com', 'password': '320316www'},
            callback=self.after_login
        )

    def after_login(self, response):
        if "authentication failed" in response.body:
            self.log("Login failed", level=log.ERROR)
            return
