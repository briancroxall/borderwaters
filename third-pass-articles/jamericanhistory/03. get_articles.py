from selenium import webdriver
import selenium
import time
import os
import random
from tqdm import tqdm

chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)

driver.get("https://academic.oup.com/jah")

output_dir = "articles/"
with open("articles.txt") as f:
	articles = f.read()
articles = articles.split("\n")
random.shuffle(articles)

for url in tqdm(articles):
	filename = url.split("/")
	filename = output_dir + "-".join(filename[-4:]) + ".html"
	if os.path.isfile(filename) == False:
		driver.get(url)
		html = driver.page_source
		with open(filename, 'w') as f:
			f.write(html)
		time.sleep(random.uniform(3,10))