# coding:utf-8
import urllib
import re
def get_html(url):
    page = urllib.urlopen(url)
    html_code = page.read()
    return html_code

def get_image(html_code):
   reg = r'src="(.+?\.jpg)" width'
   reg_img = re.compile(reg)
   img_list = reg_img.findall(html_code)
   x = 0
  for img in img_list:
        urllib.urlretrieve(img, '%s.jpg' % x)
         x += 1

19 print u'-------网页图片抓取-------'
20 print u'请输入url:',
21 url = raw_input()
22 if url:
23     pass
24 else:
25     print u'---没有地址输入正在使用默认地址---'
26     url = 'http://tieba.baidu.com/p/1753935195'
27 print u'----------正在获取网页---------'
28 html_code = get_html(url)
29 print u'----------正在下载图片---------'
30 get_image(html_code)
31 print u'-----------下载成功-----------'
32 raw_input('Press Enter to exit')