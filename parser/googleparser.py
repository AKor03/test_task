from bs4 import BeautifulSoup


class GoogleSearchParser:

    def parse_page_links(self, page):
        soup = BeautifulSoup(page, "html.parser")
        items = soup.find_all('h3', attrs={'class': 'r'})

        if items:
            links = map(lambda item: (item.a.get_text(), item.a['href'][7:]), items)
            return dict(links)

        return None
