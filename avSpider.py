import scrapy
from hanziconv import HanziConv

class AvSpider(scrapy.Spider):
    name = 'avspider'
    # start_urls = ['https://avhd101.com/search?q=%E6%A9%8B%E6%9C%AC%E6%9C%89%E8%8F%9C&t=actress']

    def __init__(self, name='', **kwargs):
        name = HanziConv.toTraditional(name)
        self.start_urls = [f'https://avhd101.com/search?t=actress&q={name}']  # py36
        super().__init__(**kwargs)
        print("获取所有 {} 的视频预览...".format(name))


    def parse(self, response):

        f4 = response.css('.cover>img::attr(src)').getall()
        for i in range(len(f4)):
            if i < 4:
                print(f4[i].replace("m2", "s2").replace("images/cover_s.jpg", "preview/pv.m3u8"))

        all = response.css('.b-lazy::attr(data-src)').getall()

        for img in all:
            preview = img.replace("m2", "s2").replace("images/cover_s.jpg", "preview/pv.m3u8")
            print(preview)

        for next_page in response.css('.row.center.fullpage>ul>li>a.pn'):
            yield response.follow(next_page, self.parse)
