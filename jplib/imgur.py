#!/usr/bin/env python3

"""
Upload an image to imgur anonymously.

# from jplib import imgur
"""

import pycurl
import untangle
from six import StringIO
from unipath import Path

from jplib import config as cfg
from jplib.scraper import bsoup as bs
from jplib.web import get_page


def upload_from_computer(fpath):
    """
    Upload an image from the local machine.
    The return value is an XML string.

    Beware! fpath must be normal string, not unicode!
    With unicode it'll drop an error.
    """
    response = StringIO()
    c = pycurl.Curl()

    values = [("key", cfg.IMGUR_KEY),
              ("image", (c.FORM_FILE, fpath))]

    c.setopt(c.URL, "http://api.imgur.com/2/upload.xml")
    c.setopt(c.HTTPPOST, values)
    c.setopt(c.WRITEFUNCTION, response.write)
    c.perform()
    c.close()

    return response.getvalue()


def upload_from_web(url):
    """
    Upload an image from the web.
    The return value is an XML string.
    """
    response = StringIO()
    c = pycurl.Curl()

    values = [("key", cfg.IMGUR_KEY),
              ("image", url)]

    c.setopt(c.URL, "http://api.imgur.com/2/upload.xml")
    c.setopt(c.HTTPPOST, values)
    c.setopt(c.WRITEFUNCTION, response.write)
    c.perform()
    c.close()

    return response.getvalue()


def process(xml, silent=True):
    """
    Process the returned XML string.
    """
    o = untangle.parse(xml)
    url = o.upload.links.original.cdata
    delete_page = o.upload.links.delete_page.cdata

    if not silent:
        print('# url:        ', url)
        print('# delete page:', delete_page)
    #
    return (url, delete_page)

##########################
## some simple wrappers ##
##########################

def upload_local_img(fpath):
    """
    Upload a local image.
    The return value is a tuple: (imgur_url, imgur_delete_url)
    """
    xml = upload_from_computer(fpath)
    o = untangle.parse(xml)
    url = o.upload.links.original.cdata
    delete_page = o.upload.links.delete_page.cdata
    return (url, delete_page)


def upload_web_img(url):
    """
    Upload a web image.
    The return value is a tuple: (imgur_url, imgur_delete_url)
    """
    xml = upload_from_web(url)
    o = untangle.parse(xml)
    url = o.upload.links.original.cdata
    delete_page = o.upload.links.delete_page.cdata
    return (url, delete_page)

#############
## gallery ##
#############

def get_gallery_images(url):
    html = get_page(url)
    soup = bs.to_soup(html)

    li = []
    for link in bs.get_images(soup):
        if 'imgur.com' in link and link.endswith(('.jpg', '.gif', '.png')):
            if link.startswith('//'):
                link = 'http:' + link
            li.append(link)

    return li

#############################################################################

if __name__ == "__main__":
#     img = Path(cfg.TEST_ASSETS_DIR, 'manjaro.png')
# #    xml = upload_from_computer(img)
# #    print(process(xml, silent=False))
#     #
#     url = 'http://i.imgur.com/sfjH2Hu.png'
# #    xml = upload_from_web(url)
# #    print(xml)
# #    print(process(xml))
#     #
# #    print(upload_local_img(img))
#     #
#     print(upload_web_img(url))

    url = "http://imgur.com/a/O4lle"
    print(get_gallery_images(url))
