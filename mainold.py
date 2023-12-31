from bs4 import BeautifulSoup
#
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)
#
# # all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
# #
# # for tag in all_anchor_tags:
# #     print(tag.get("href"))
# #
# # heading = soup.find(name="h1", id="name")
# # print(heading)
#
# # section_heading = soup.find(name="h3", class_="heading")
# # # print(section_heading.getText())
# # company_url = soup.select_one(selector="#name")
# # print(company_url)
#
# print(soup.select(".heading"))

import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find(name="a", class_="storylink")
# article_tag = article_tag.getText()
# article_link = article_tag.get("href")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(article_tag)
    link = article_tag.get("href")
    article_links.append(link)

article_upvote = [score.getText() for score in soup.find_all(name="span", class_="score").getText()]


print(article_texts)
print(article_links)
print(article_upvote)
