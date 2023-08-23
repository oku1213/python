import urllib.request

url='http://news.yahoo.co.jp/'
req=urllib.request.Request(url)

with urllib.request.urlopen(req) as res:
    body=str(res.read())

if 'プリゴジン' in body or 'アルツハイマー' in body:
    print('キーワードに関する記述があります')
    print('http://news.yahoo.co.jp/を確認してください')
else:
    print('調査対象のセキュリティ用語はありませんでした')
