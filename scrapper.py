import requests
from bs4 import BeautifulSoup
import csv

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
# print(r)
soup = BeautifulSoup(r.text,"lxml")
boxes = soup.find_all("div",class_="col-md-4 col-xl-4 col-lg-4")

names = soup.find_all("a",class_="title")
prices = soup.find_all("h4",class_="price")

for n,p in zip(names,prices):
    print(n.text.strip(),"=",p.text.strip())

with open("products.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Price"])
    for n,p in zip(names,prices):
        writer.writerow([n.text.strip(), p.text.strip()])
