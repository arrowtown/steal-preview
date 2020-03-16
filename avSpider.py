import scrapy
from hanziconv import HanziConv

class AvSpider(scrapy.Spider):
    name = 'avspider'

    def __init__(self, name='', **kwargs):
        name = HanziConv.toTraditional(name)
        self.start_urls = [f'https://cn.ax101.vip/search?t=actress&q={name}']  # py36
        super().__init__(**kwargs)
        print("获取所有 {} 的视频预览...".format(name))


    def parse(self, response): 

        all = response.css('.list li h3 a::attr(href)').getall()

        for img in all:
            preview = img.replace("/watch?v=", "https://pvtc.mixiancn.com/")+"/preview/pv.m3u8"
            print(preview)

        for next_page in response.css('.row.center.fullpage>ul>li>a.pn'):
            yield response.follow(next_page, self.parse)
