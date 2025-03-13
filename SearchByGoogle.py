import sys
import webbrowser
import urllib.parse

# ファイル名を取得
if len(sys.argv) < 2:
    print("エラー：ファイル名が指定されていません")
    sys.exit(1)

file_name = sys.argv[1]
query = urllib.parse.quote(file_name)  # URLエンコード

# Google 検索 URL を生成
search_url = f"https://www.google.com/search?q={query}"

print(search_url)
input()
# デフォルトのブラウザで開く
# webbrowser.open(search_url)