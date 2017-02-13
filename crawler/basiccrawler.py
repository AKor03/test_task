import ssl
import time
import urllib.error
import urllib.request
from abc import ABC

from exception.crawlerexception import FetchFailedException
from settings import CrawlerConfig


class Crawler(ABC):
    # Logger if necessary

    def http_request(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }
        request = urllib.request.Request(url, headers=headers)
        context = ssl._create_unverified_context()

        request_number = 0
        while request_number < CrawlerConfig.REQUEST_RETRIES:
            request_number += 1
            state_message = 'Success'

            try:
                response = urllib.request.urlopen(request, timeout=CrawlerConfig.REQUEST_TIMEOUT, context=context)
                return response.read()

            except urllib.error.HTTPError as http_error:
                if http_error.code in [404]:
                    # 404 error logging logic
                    return None

                if http_error.code in [410]:
                    # 410 error logging logic
                    return None

                state_message = str(http_error)

            except Exception as common_error:
                state_message = str(common_error)
                pass

            if request_number > CrawlerConfig.REQUEST_RETRIES:
                # Other error logging logic
                raise FetchFailedException(state_message)

            time.sleep(CrawlerConfig.REQUEST_DELAY)
