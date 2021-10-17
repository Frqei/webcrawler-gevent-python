# webcrawler-gevent-python
python3 project

Your task is to build a website crawler in Python, using gevent for asynchronous operations. You may use other libraries as well.

Your solution should accept one page URL as input, and should crawl all links within the associated domain that are reachable either directly or indirectly from the original page URL.

Your solution should not crawl pages outside of the domain associated with the original URL.

For instance, if your solution crawls https://bbc.co.uk, it should catalogue all news pages, comments, profiles etc within the domain bbc.co.uk; but it should not crawl linked articles outside of bbc.co.uk.

You may return results via any mechanism, as long as you include the origin and destination of each link. For instance, if page A links to B and C you could return something like: A -> B

A -> C

Suppose B had a further link to page D you'd also emit:

B -> D

Use this opportunity to showcase your approach to engineering; this is at least as important as producing a working algorithm. For instance:

- Consider how you would structure your solution to be readable, maintainable, and to enable a team to work alongside you on your solution;
- How will you test your solution - unit tests, etc;
- Think about how your solution could be reused - how it is invoked, how it is configured, and how it returns its results;
- Manage expensive resources and make best use of them - for instance, how will you create/maintain/feed gevent workers, manage how many are active at any one time, etc. 

# Assumptions and tackling the problem

- I assume that the website I have to crawl contains a href tags.
- I don't render Js sites.
- I don't manage Auth yet.
- Nothing is stored in db yet, might use redis or another dbms like postgres.

# TODO

- Args parse to run it
- db management
- better management of gevent pool (at the momment I create batches of 50 worker when I try to parse link I found in one page)
- use json file as input or at least a list of websites
- dockerfile + docker-compose for convenience
- so much more 


# How to run 

Works with python 3.9, you want to create a virtual-env using conda and the .yml provided or casually using the requirements.txt
At the moment you have to modify the code of main.py


