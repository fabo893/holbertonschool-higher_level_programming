#!/usr/bin/python3
"""
    What's my status?
"""


from urllib import request


if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as rep:
        html = rep.read()
        print("Body response:\n\
                \t- type: {}\n\
                \t- content: {}\n\
                \t- utf8 content: {}".format(type(html), html,
                                             html.decode('utf-8')))
