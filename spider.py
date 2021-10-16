import gevent
from gevent import monkey

monkey.patch_all()
import time
from utils.parser import PageParser
from utils.urlstools import clean, get_domain, valid, contain_static


class Spider(object):
    def __init__(self):
        self.to_visit = []
        self.visited = set([])
        self.parser = PageParser()
        self.links_connections = list()

    def display_connections(self):
        """
        Display links between pages, from page A we find a link to page B : A -> B
        """
        for con in self.links_connections:
            print(f"{con[0]} -> {con[1]}")

    def crawl(self, target_url, max_depth=2):
        """
        Spawn greenlet objects and make them visit pages from the list
        """
        target_url = clean(target_url)  # clean target_url
        print(f"Start crawling @ {target_url}")
        current_depth = 0
        self.to_visit.append((target_url, current_depth))  # put target_url to to_visit list
        jobs = list()
        cpt_d = 0
        while current_depth < max_depth:
            js = 0
            while len(self.to_visit) > 0:
                (url, current_depth) = self.to_visit.pop(0)  # get next url
                if url not in self.visited:
                    jobs.append(gevent.spawn(self.visit, url, max_depth, current_depth))
                    js += 1
                    if js == 50:
                        gevent.joinall(jobs)
                        jobs = list()
                        js = 0
            if len(jobs) > 0:
                gevent.joinall(jobs)
        self.display_connections()
        print("The spider has finished crawling the web at {url}".format(url=target_url))

    def visit(self, url, max_depth, current_depth):
        """
        Run the parser and returns links found in this page
        """
        urls = self.parser.run(url, max_depth, current_depth)  # parse the url
        if len(urls) > 0:
            l = [(url, u) for u in urls if u is not None]
            self.links_connections = self.links_connections + l
        self.visited.add(url)  # add this visted url to visted list

        # Add urls from the praser to to_visit lits
        # When they are not visited or already in the to_vist list
        if len(urls) > 0:
            for url in urls:
                if url not in self.visited and url not in [a_tuple[0] for a_tuple in self.to_visit]:
                    self.to_visit.append((url, current_depth + 1))



