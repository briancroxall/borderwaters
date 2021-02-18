from selenium import webdriver
import selenium
import time
import os

chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)

driver.get("https://muse.jhu.edu/journal/13")

with open("indexes.txt") as f:
	indexes = f.read()
indexes = indexes.split("\n")
for index in indexes:
	print(index)
	index = index.split("\t")
	issue = index[0]
	url = index[1]
	output_filename = issue + ".html"
	output_filename = "indexes/" + output_filename
	print(output_filename)
	if os.path.isfile(output_filename) == False:
		driver.get(url)
		html = driver.page_source
		with open(output_filename, 'w') as f:
			f.write(html)
		time.sleep(3)