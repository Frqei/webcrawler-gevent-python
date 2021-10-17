from unittest import mock
from pytest_mock import mocker
import pytest
import utils.parser
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


def test_visit(mocker):
    mocker.patch('utils.parser.PageParser.run', return_value=["pageA", "pageB"])
    spider = Spider()
    spider.visit("http://adrien.fazio/", 1, 0)
    assert spider.to_visit == [('pageA', 1), ('pageB', 1)]


def test_crawl(capsys, mocker):
    mocker.patch('utils.parser.PageParser.run', return_value=["pageA", "pageB"])
    spider = Spider()
    spider.crawl("http://adrien.fazio/", max_depth=1)
    captured = capsys.readouterr()
    assert captured.out == "Start crawling @ http://adrien.fazio\nhttp://adrien.fazio -> pageA\nhttp://adrien.fazio -> pageB\npageA -> pageA\npageA -> pageB\npageB -> pageA\npageB -> pageB\nThe spider has finished crawling the web at http://adrien.fazio\n"
    assert isinstance(spider.visited, set)
    assert list(spider.visited).sort() == ["http://adrien.fazio", "pageA", "PageB"].sort()
    assert spider.links_connections == [('http://adrien.fazio', 'pageA'), ('http://adrien.fazio', 'pageB'),
                                        ('pageA', 'pageA'), ('pageA', 'pageB'), ('pageB', 'pageA'),
                                        ('pageB', 'pageB')]
