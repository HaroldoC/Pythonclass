import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")
res2 = requests.get("https://news.ycombinator.com/news?p=2")
soup = BeautifulSoup(res.text, "html.parser")
soup2 = BeautifulSoup(res2.text, "html.parser")
links = soup.select(".titleline")
links2 = soup2.select(".titleline")
subtext = soup.select(".subtext")
subtext2 = soup2.select(".subtext")
# print(links[0].get("href"))
# print(votes[0].get("id"))
# print(votes[0].getText())

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k["votes"], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))


# def get_page(url):
#     response = requests.get(url)
#     if not response.ok:
#         print("Server responded:", response.status_code)
#     else:
#         soup = BeautifulSoup(response.text, "lxml")
#     return soup


# def get_detail_data(soup):
#     # title
#     try:
#         title = soup.find("h1", id="itemTitle").text.strip().replace("Details about", "")
#     except:
#         title = ""

#     # price
#     try:
#         price = soup.find("span", id="prcIsum").text.strip()
#     except:
#         price = ""

#     # sold
#     try:
#         sold = soup.find("span", class_="vi-qtyS-hot-red").find("a").text.strip().split(" ")[0]
#     except:
#         sold = ""

#     data = {
#         "title": title,
#         "price": price,
#         "total sold": sold,
#     }
#     return data
