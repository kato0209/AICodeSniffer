import requests
from bs4 import BeautifulSoup

# スクレイピングするウェブページのURL
url = 'http://example.com'

# ページの内容を取得
response = requests.get(url)

# HTMLのパース
soup = BeautifulSoup(response.content, 'html.parser')

# <extra_id_0> soup.find('title').text

print(f"ページのタイトル: {title}")
