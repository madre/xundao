# zhidao_scrapy
zhidao.baidu.com scrapy project

知道问答爬虫

## 技术选型说明


> 百度的爬虫方向确定：

1. 百度所有的问答url格式均为 http://zhidao.baidu.com/question/<qid>.html， 可以按id遍历，但知道答案新id已经是625792527174498444这样的位数级，按这个遍历所有，并不现实；
2. 问答有分类，但是各分类下只有最新问答和难题榜；每种分类只能得到前100页数据，每页25条，即最多可得到2500条数据；
3. 百度知道有用户排行榜 http://zhidao.baidu.com/misc/alltop?type=week ，可能通过爬取排行榜上靠前的用户答案（每个用户可以爬3000个问答）；通过爬取各分类的优质答案，可以最大限度的得到各分类的最优质答案〜

因为时间问题，最后采用最简单的遍历一定范围的id，减少爬虫实现的时间；把主要精力放在解决搜索引擎的搭建上！


## 爬虫说明

> scrapy shell http://zhidao.baidu.com/question/143477925.html

进入debug模式，测试页面解析部分

> scrapy crawl question

执行 爬虫测试项目
