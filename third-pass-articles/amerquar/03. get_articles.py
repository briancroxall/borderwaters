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

driver.get("https://muse.jhu.edu/journal/13")

output_dir = "articles/"
with open("articles.txt") as f:
	articles = f.read()
articles = articles.split("\n")
random.shuffle(articles)

for url in tqdm(articles):
	cols = url.split("\t")
	issue = cols[0].split("/")[-1]
	url = cols[1]
	filename = url.split("/")[-1]
	filename = output_dir + issue + "-" + filename + ".html"
	print(url, "-->", filename)
	if os.path.isfile(filename) == False:
		driver.get(url)
		html = driver.page_source
		with open(filename, 'w') as f:
			f.write(html)
		time.sleep(random.uniform(30,60))