import pytest
from utils.spider import Spider


def test_create_spider():
    spider = Spider()
    assert isinstance(spider, Spider)


def test_display_connections(capsys):
    spider = Spider()
    spider.links_connections.append(("Page A", "Page B"))
    spider.display_connections()
    captured = capsys.readouterr()
    assert captured.out == "Page A -> Page B\n"

