# 新浪博客转电子书

## 目的
通过爬取新浪博客文章制作电子书。
目前爬取的是“缠中说禅”的某几个分类。

## 用法
修改`spiders/sinablog.py`的变量`start_urls`为某一博客列表后，执行`scrapy crawl sinablog`，在output目录下会生成一组html文件和一个toc文件。

打开calibre的ebook编辑器，新建书籍（选择epub格式）后选择“导入文件到书籍”，选择所有html文件导入。

文本编辑器打开名为toc的文件，复制所有内容，在ebook编辑器里打开toc.ncx，将复制的内容粘贴到navMap节点下，电子书即初步完成，已经可读。可根据自己需要继续调整或直接使用阅读器读书。

要用kindle的需要再用calibre转一下mobi格式。

## 其他
python和scrapy新手，仅仅为了实现自己的目的而写了这个小程序。欢迎给出改进意见。

目前没有爬取图片功能，以后加上。

## 命令记录备忘
```bash
# 创建新项目
scrapy startproject SinaBlogCrawler
# 创建一个spider
scrapy genspider sinablog blog.sina.com.cn

# 执行爬取
scrapy crawl sinablog
```
