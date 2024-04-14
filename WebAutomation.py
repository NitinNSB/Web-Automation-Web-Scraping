from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

website = "https://www.thesun.co.uk/sport/"
path = "./chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
containers = driver.find_elements(By.XPATH, value='//div[@class="teaser__copy-container"]')
titles = []
subtitles = []
links = []
for container in containers:
    try:
        title = container.find_element(By.XPATH, value='./a/h3').text
        titles.append(title)
    except NoSuchElementException:
        titles.append("N/A")
    try:
        subtitle = container.find_element(By.XPATH, value='./a/p').text
        subtitles.append(subtitle)
    except NoSuchElementException:
        subtitles.append("N/A")
    try:
        link = container.find_element(By.XPATH, value='./a').get_attribute("href")
        links.append(link)
    except NoSuchElementException:
        links.append("N/A")
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv("fileName.csv")
driver.quit()
