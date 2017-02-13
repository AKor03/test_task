from crawler.googlecrawler import GoogleSearchCrawler


def main():
    search_request = 'Python & R'

    crawler = GoogleSearchCrawler()
    links = crawler.fetch_links(search_request)

    for title, href in links.items():
        print(title + '\t' + href)

if __name__ == "__main__":
    main()
