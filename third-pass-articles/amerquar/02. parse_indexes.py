import os
from bs4 import BeautifulSoup as bs

base_url = "https://muse.jhu.edu/"
input_dir = "indexes/"
files = os.listdir(input_dir)
files = [input_dir + x for x in files if x.endswith(".html")]
urls = []
for file in files:
	issue = file.replace(".html", "")
	with open(file) as f:
		html = f.read()
	soup = bs(html, "html.parser")
	links = soup.find_all("li", {"class":"title"})
	for link in links:
		a_element = link.find_all("a")[0]
		url = base_url + a_element.attrs["href"]
		if "article" in url:
			urls.append(issue + "\t" + url)

with open("articles.txt", 'w') as f:
	f.write("\n".join(urls))