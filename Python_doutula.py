"""
Project: A simple crawler project.

File:   Pythonbizhi.py

Author: qingheyueshilui

Time:   2020/11/15

"""
# 0.导入模块
import requests
import re

# 1.确定网址（url）
url = 'https://www.fabiaoqing.com/search/bqb/keyword/%E6%96%97%E5%9B%BE%E5%95%A6/type/bq.html'

# 1.2 UA
ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

# 2.请求数据(ruquest) 图片 音频 视频（content） 文本text
html_str = requests.get(url,headers=ua).text


# 3.删选数据(正则表达式)
image_urls = re.findall('data-original="(.*?)"',html_str)


for image_url in image_urls:
    # print(image_url)
    # http://wx1.sinaimg.cn/bmiddle/005TGG6vly1fem11owix8j30j60gy0tt.jpg

    image_names = image_url.split('/')[-1]
    print(image_names)

    image = requests.get(image_url, headers=ua).content

    # 4.保存数据
    with open('./imagefile%s'%image_names,'wb') as file:
        file.write(image)