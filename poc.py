""" Note for future me: Idea is really unique, shut the f up!!! """
""" The perfect streaming application!!! """

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

""" POC class for now, will make it better later """
class POC:
	def __init__(self, file_name):
		self.file_name = file_name

	""" Method to hit the stream websites """
	def hit_urls(self, urls):
		for url in urls:
			# Hit the Streaming website URL
			req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
			page = urlopen(req)
			html = page.read()
			soup = BeautifulSoup(html, 'lxml')

			# Choose what kind of DOM data to send to the learner
			# Need to find a way to parallelize this as well, too slow at the moment

			# Send data to learner
			# Learn the DOM data
			# Evaluate on different classifiers, check performance

			# Receive necessary information

	""" Method to retrieve urls from a file, more data to be added to the file later """
	def retrieve_urls(self):
		with open(self.file_name) as url_file:
			lines = url_file.read().splitlines()

		urls = []
		for line in lines:
			urls.append(line.split(',')[0])

		self.hit_urls(urls)

poc = POC("./urls.txt")
poc.retrieve_urls()