import time

from spider import Spider

if __name__ == "__main__":
    spider = Spider()
    start = time.time()
    spider.crawl("https://bbc.co.uk/", max_depth=2)
    end = time.time()
    print(f"Crawled {len(spider.visited)} pages in {end - start} seconds")