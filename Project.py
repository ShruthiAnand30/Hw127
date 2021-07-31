from selenium import webdriver 
from bs4 import BeautifulSoup
import time
import csv
start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
import pandas as pd 
import requests

page = requests.get(start_url)
soup = BeautifulSoup(page.text, "html.parser")
star_table = soup.find("table")
temp_list = []
table_rows = star_table.find_all("tr")

for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip()for i in td]
    temp_list.append(row)

name = []
distance - []
mass = []
raduis = []
lum = []

for i in range(1,len(temp_list)):
    names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    raduis.append(temp_list[i][6])
    lum.append(temp_list[i][7])

df2.pd.DataFrame(list(zip(names, distance, mass, radius, lum)), columns = ["star_name", "star_distance", "star_mass", "star_radius", "star_luminicy"])
df2.to_csv("bright_star.csv")
