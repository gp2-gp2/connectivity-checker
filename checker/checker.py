from http.client import HTTPConnection
from urllib.parse import urlparse


def site_is_online(url, timeout=2):
    """
    Return true if the site is online.
    Raise an exception otherwise.
    """
    error = Exception("unknown error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
