from gevent import monkey

monkey.patch_all()
from html.parser import HTMLParser
import requests
from bs4 import BeautifulSoup
from utils.urlstools import get_domain, valid, contain_static


class PageParser(HTMLParser):
    """
    HTML parser to fetch urls
    """

    def error(self, message):
        super().error(message=message)

    def run(self, url, max_depth, current_depth):
        """
        Run the parser and return links in this page
        """
        url
        urls = []
        try:
            if current_depth < max_depth:
                response = requests.get(url)
                domain = get_domain(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                links = []
                for link in soup.findAll('a'):
                    l = link.get('href')
                    if l is not None:
                        links.append(l)
                filtered = [i for i in links if (valid(i, domain) and not contain_static(i))]
                filtered = list(set(filtered))
                urls = filtered
            else:
                return []
        except KeyboardInterrupt:  # deal with Ctrl-C
            exit()
        except Exception as e:
            print(e.message)
            print("Unexpected failure happens and the spider escapes.")
        return urls
