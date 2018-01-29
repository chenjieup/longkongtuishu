# longkongtuishu
龙空论坛推书板块2017数据分析
## 项目名称：
### 龙空论坛推书板块数据爬取，整理及分析
## 项目背景：
### 龙空论坛推书板块为国内网文作者及书评人的聚集地，每天有大量的书友及网文作者发帖讨论和推荐当下话题度较高，较热，比较火的小说。作为一名小说爱好者，我一般通过此途径去找到自己偏好的小说。但由于帖子的时效性和发帖人口味种类的多样性，很难找到中意的小说，除此之外，我也很好奇论坛龙友们关注的热点，希望通过数据挖掘来对论坛推书板块做些分析研究。
## 项目内容：
### 作为一名数据挖掘爱好者，我打算爬取龙空论坛2017年推书板块所有的帖子（将近2万个帖子，10万个页面）的内容，存入本地数据库，然后对数据进行分析和做自然语言处理方面的研究。爬取的内容主要有帖子标题，发帖人，发帖时间，回复数，帖子中涉及到的小说等等。
## 工具：
### Anaconda Pycharm
## 项目周期：
### 2017.12-2018.02
## 项目进度：
### 第一阶段：数据采集
日期：2017.12.20 <br/>
内容：已完成爬虫代码基本框架，对其测试，爬取500个帖子，爬取小说名称正常，但写入本地csv文件出现编码问题，主要是打开后乱码，用notepad打开，改变编码方式解决问题。<br/>
日期：2017.12.25<br/>
内容：对上次爬取下来的书名采用pandas库进行词频分析，然后用wordcloud做成标签云，进行可视化。wordcloud库首先会对文本做词频统计，统计时以空格区分单词，我得把爬取下来的书名先加空格然后存为txt文本。再做词云的时候，wordcloud不支持中文，但可以自定义字体。<br/>
日期：2017.1.5<br/>
内容：自己写的爬虫脚本在爬取的过程中会产生一些异常报错，比如连接超时，爬取速度过慢等。我打算采用scrapy框架爬虫，scrapy基于twisted异步工作模式，虽然爬取速度较快，但是由于自己不太精通，发现爬取下来想要的数据，保存的时候出现问题，标题，发帖人，发帖时间，回复数我都可以在一个页面上抓取，但小说名是需要爬取帖子的内容，进行页面分析得到，所以保存的时候不能与前面保持同步。暂时还没找到解决办法，我决定还是采用自己写的脚本进行爬取，对于异常报错及爬取速度过慢，我打算多进行异常检测和多线程来提高程序的健壮性。<br/>
日期：2017.1.10<br/>
内容：爬虫脚本初步完成，单线程，爬取速度感觉还行。话说python解析器都是单线程的，写python程序有必要多线程么。计划今晚爬虫测试。<br/>
日期：2017.1.11<br/>
内容：程序跑了一晚上，今儿一大早来看结果。emmmmm。。。timeouterror，exception。。。难道是爬取次数过多，拒绝访问了么。修改程序，设置timeout时间，超时直接换下一个。整个程序加一个异常采集，finally直接pass掉，这下总ok了么。测试测试。<br/>
日期：2017.1.12<br/>
内容：爬到三分之一，程序运行结束什么鬼，数据爬取了两千条。难受，异常也没出现，为嘛就自己停了。。。难道电脑自动休眠？自动断网了？<br/>
日期：2017.1.13<br/>
内容：还好我爬虫的时候，特意print爬取页面的url，我发现爬取到第99页正常，到100页就不行了。我用浏览器访问了一下，原来是要登陆才能查看信息。正好用上之前模拟登陆的知识，不多说，改代码ing。<br/>
日期：2017.1.14<br/>
内容：模拟登陆不外乎就是要post表单，有的时候需要验证码，之前我都这样认为的，之前做网站模拟登陆觉得挺简单。但现在是个论坛，表单里有一项为formhash。。。然后蒙圈了，查了资料才知道，只是为了防止重复提交表单特意设置的。真麻烦，不过可以在页面源码中可以得到。弄了半天，有点嫌麻烦，我直接网页登录，复制cookie，直接带cookies登陆了。<br/>
日期：2017.1.14<br/>
内容：项目第一阶段告一段落，五千多条数据爬取完毕。<br/>
### 第二阶段：数据清洗
日期：2017.1.21<br/>
内容：终于放寒假了，可以有更多的时间来完成这项工作了。对上次爬取到的将近六千条数据做清洗，使用pandas库。<br/>第一步，去除重复数据，有重复爬取的现象，导致爬取相同的数据。<br/>第二步，去除数据里的空值。isnull()函数，如果是空值就显示True。notnull()函数正好相反，如果是空值就显示False。然后通过value_counts()函数进行统计。对于空值有两种处理的方法：第一种是使用fillna()函数对空值进行填充，可以选择填充0值或者其他任意值。第二种方法是使用dropna()函数直接将包含空值的数据删除。根据这次爬取的内容，表有五列数据，有四列不能为空，最后一列name可为空。对空值进行统计后发现，第一列数据有两个空值，我索性丢掉这两条数据。<br/>第三步，处理数据的极端值与异常值。在数据表最后一列书名里面有些异常值，不是我们想要的书名，是一些乱码字符串，我们对其整行数据进行删除。因为乱码内容，是由于抓取数据时，匹配不严格，乱码多为href标签网址。所以要根据name列数据的内容进行判断，然后在处理。我打算先用正则表达式匹配找到乱码的行，再删除,re.search(pattern, string, flags=0)。<br/>第四步，更改数据格式。由于数据都是从页面抓取得到的，数据格式都是python型，也就是字符型。data数据列应为日期型，需修改。heat数据列应为数字型，需修改。更改和规范数据格式，所使用的函数是astype()。对heat列中的数据，通常为整数，因此我们数据格式改为int64。在数据格式中还要特别注意日期型的数据。日期格式的数据需要使用to_datatime函数进行处理。<br/>最后一步，重新建立索引。<br/>
数据清洗完成，还有5682条数据。
### 第三阶段：数据分析
日期：2017.1.21<br/>
内容：先从最简单的来，我对前面2017年所有帖子提到的小说名，提取出来，做成一个词云，直观的反应2017年度，最火，最具话题性的小说。标签云制作用wordcloud，因为识别的是txt文档，我把之前所有的书名写入一个txt文档，每个书名空一格，保证其能识别为一个整体。<br/>
![9SWVh9.png](https://s1.ax1x.com/2018/01/29/9SWVh9.png)
