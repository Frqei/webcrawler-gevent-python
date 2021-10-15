from urllib import parse  # for domain extraction
import re  # for regular expression


def clean(url):
    """
    Clean up url by
        - always start with "http://" or "https://"
        - remove element jumping
        - remove last '/'
    """
    # Deal with "http(s)://"
    if url[0:4] != "http":
        url = "http://" + url

    # Deal with "#"
    idx = url.find('#')
    if idx != -1:
        url = url[:idx]

    # Deal with last "/"
    l = len(url)
    if url[l - 1] == '/':
        url = url[:l - 1]

    return url


def get_domain(url):
    """
    Get the domain of a given url
    """
    parsed_url = parse.urlparse(url)
    return "{url.netloc}".format(url=parsed_url)


def valid(url, domain):
    """
    Check if the given url is valid
    """
    if re.match(r'^https?://([\w-]*\.)?' + domain + r'.*$', url, re.M | re.I):
        return True
    else:
        return False


def contain_static(val):
    '''
    Check if a given val (relative path or url) contains static files
    @input:
        val         :   relative path or url
    @output:
        contain?    :   if the val contains a static file
    '''
    if re.match(r'^.*\.(jpg|jpeg|gif|pdf|png|css|js|ico|xml|rss|txt).*$', val, re.M | re.I):
        return True
    else:
        return False

