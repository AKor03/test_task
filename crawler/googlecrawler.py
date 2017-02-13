from crawler.basiccrawler import Crawler
from exception.crawlerexception import FetchFailedException
from parser.googleparser import GoogleSearchParser


class GoogleSearchCrawler(Crawler):

    def __init__(self):
        self.parser = GoogleSearchParser()
        self.search_url_template = 'https://www.google.com/search?q={find}'

    def fetch_links(self, search_request):
        url = self.search_url_template.format(find=search_request.replace(" ", "+"))

        try:
            html_page = self.http_request(url)
        except FetchFailedException as fetch_error:
            raise fetch_error

        if html_page:
            links = self.parser.parse_page_links(html_page)
            return links

        return None
