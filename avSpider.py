import scrapy
from hanziconv import HanziConv

class AvSpider(scrapy.Spider):
    name = 'avspider'

    def __init__(self, name='', mode='',**kwargs):
        name = HanziConv.toTraditional(name).replace("鼕","冬")
        self.start_urls = ([f'https://cn.ax101.vip/search?t=actress&q={name}'] if bool(mode) else [f'https://cn.ax101.vip/search?q={name}'])
        super().__init__(**kwargs)
        print(("名字匹配模式：" if  bool(mode) else "粗略查询模式：")+"获取所有 {} 的视频预览...<br>".format(name))


    def parse(self, response): 

        all = response.css('.list li h3 a::attr(href)').getall()

        for idx,img in enumerate(all):
            preview = img.replace("/watch?v=", "https://pvtc.mixiancn.com/")+"/preview/pv.m3u8"
            print("<a href=\""+ preview +"\">"+ str(idx) +": "+ preview + "</a><br>")

        for next_page in response.css('.row.center.fullpage>ul>li>a.pn'):
            yield response.follow(next_page, self.parse)
