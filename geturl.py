import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.cuponation.com.sg/allshop'
driver = webdriver.Chrome('C:\\Users\\XX\\Desktop\\scrapy\\chromedriver.exe')
driver.get(url)
links = driver.find_elements(By.CSS_SELECTOR, "div._1hd6wnh6 a")
links_href = [(link.get_attribute('href'), link.text) for link in links]
file_path = 'C:\\Users\\XX\\Desktop\\scrapy\\links.csv'
with open(file_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['URL', 'Shop Name'])
    for href, name in links_href:
        writer.writerow([href, name])
driver.quit()
