from selenium import webdriver
import selenium
import time
import os

chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)

base_url = "https://www.lds.org/mls/mbr/orgs/callings-by-organization"
driver.get("https://academic.oup.com/jah")

with open("indexes.txt") as f:
	indexes = f.read()
indexes = indexes.split("\n")
for index in indexes:
    stop = False
    page = 1
    while stop == False:
        driver.get(index + "?page=" + str(page))		
        try:
            next_ = driver.find_element_by_class_name("PagedList-skipToNext")
        except selenium.common.exceptions.NoSuchElementException:
            stop = True
            print("No next page")
        html = driver.page_source
        output_filename = index.split("/")
        output_filename = output_filename[-2:]
        output_filename = "-".join(output_filename)
        output_filename = output_filename + "_" + str(page) + ".html"
        output_filename = "indexes/" + output_filename
        print(output_filename)
        if os.path.isfile(output_filename) == False:
            with open(output_filename, 'w') as f:
                f.write(html)
                time.sleep(3)
        page += 1
        if stop == False:
            next_.click()