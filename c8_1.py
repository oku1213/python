import urllib.request

url='http://blog.python.org/'
req=urllib.request.Request(url)

with urllib.request.urlopen(req) as res:
    body=str(res.read())

if 'security' in body or 'vulnerability' in body:
    print('セキュリティに関する記述があります')
    print('http://blog.python.org/を確認してください')
else:
    print('調査対象のセキュリティ用語はありませんでした')
