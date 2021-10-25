import requests
from bs4 import BeautifulSoup
url = "https://news.ycombinator.com/news"
response = requests.get(url)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)


aritcle_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(aritcle_upvotes)

