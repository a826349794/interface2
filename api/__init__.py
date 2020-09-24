# 以下为公共变量
# host域名/ip
from tools.read_yaml import read_yaml

HOST = "http://ttapi.research.itcast.cn"
# 请求信息头:
headers = {"Content-Type":"application/json"}

# 文章id
article_id = None
data =read_yaml("mp_article.yaml")
print(data)
# 文章标题
title = data[0][0]
# 文章内容
content = data[0][1]
# 频道
channel =data[0][2]
# 频道id
channel_id =data[0][3]
print(title,content,channel,channel_id)