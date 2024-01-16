import requests
from bs4 import BeautifulSoup
# import lxml


# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # soup = BeautifulSoup(data, "lxml")
#
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.a)
# # print(soup.p)
# anchor_tags = soup.find_all(name="a")
# # print(soup.find_all(name="a"))
#
# for tag in anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#     pass

# heading = soup.find(name="h1", id="name")
# print(heading.getText())
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))
#
# print(soup.select_one(selector="#name"))
# print(soup.select(selector=".heading"))

# print(soup.find("input").get("maxlength"))

response = requests.get("https://news.ycombinator.com/news")
yc_web = response.text

# soup = BeautifulSoup(yc_web, "html.parser")
# article = soup.find(name="span", class_="titleline")
# article_text = article.getText()
# print(article_text)
# article_link = article.select_one("a").get("href")
# print(article_link)
# article_upvote = soup.find(name="span", class_="score").getText()
# print(article_upvote)

soup = BeautifulSoup(yc_web, "html.parser")
article = soup.find_all(name="span", class_="titleline")
text_list = []
link_list = []
for tag in article:
    article_text = tag.getText()
    text_list.append(article_text)
    article_link = tag.select_one("a").get("href")
    link_list.append(article_link)

all_score = soup.find_all(name="td", class_="subtext")
score_list = []
for score in all_score:
    scores = score.find(name="span", class_="score")
    if scores is None:
        score_list.append(0)
    else:
        score_list.append(int(scores.getText().split()[0]))

max_value = max(score_list)
max_index = int(score_list.index((max_value)))
