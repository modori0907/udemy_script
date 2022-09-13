import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]  # リスト内包処理を使う

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)  # 最も大きい数字のインデックス番号を取得する

print(article_links[largest_index]) # 最も大きい数字のインデックス番号を取得した数字を記載


#
# print(largest_number)
# print(article_texts)
# print(article_links)
# print(article_upvotes)


"""
print(article_upvotes[0])
print(int(article_upvotes[0].split()[0]))
分割させるためにsplitを利用した
99 points
['99', 'points']
"""