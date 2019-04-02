import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import ScrapyRedisSpiderItem


class Scrapy_Redis_Spider(RedisSpider):
    name = 'Scrapy_Redis_Spider'
    redis_key = 'start_urls'

    # 列表页面解析函数
    def parse(self, response):
        # 提取详情页链接
        for page_url in response.xpath('//div[@class="el"]/p/span/a[@target="_blank"]/@href').extract():
            page_url = response.urljoin(page_url)
            yield scrapy.Request(url=page_url, callback=self.parse)
        # 提取“下一页”链接
        for page_url in response.xpath('//li[@class="bk"]/a/@href').extract():
            page_url = response.urljoin(page_url)
            yield scrapy.Request(url=page_url, callback=self.parse)

        # # 详情页解析函数
        Item = ScrapyRedisSpiderItem()
        Item['position'] = response.xpath('//div[@class="cn"]/h1/@title').extract()
        Item['company'] = response.xpath('//div[@class="cn"]/p/a/@title').extract()
        Item['address'] = response.xpath('//div[@class="cn"]/span//text()').extract()
        Item['money'] = response.xpath('//div[@class="cn"]/strong//text()').extract()
        Item['content'] = response.xpath(
            '//div[@class="bmsg job_msg inbox"]/p/text()|//div[@class="bmsg job_msg inbox"]//li/text()|//div[@class="bmsg job_msg inbox"]//text()').extract()
        Item['content'] = ''.join(Item['content']).replace('\t', '').replace('\r\n', '').replace(' ', '').replace(
            '\xa0', '').replace(
            '分享微信邮件', '')
        if Item['position'] == []:
            Item['position'] = '无关值'
        if Item['company'] == []:
            Item['company'] = '无关值'
        if Item['address'] == []:
            Item['address'] = '无关值'
        if Item['money'] == []:
            Item['money'] = '无关值'
        if Item['content'] == '':
            Item['content'] = '无关值'
        yield Item