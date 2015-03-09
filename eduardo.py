import re, requests

class Ed(object):

    def __init__(self, name='Eduardo', port='8085',
                server='0.0.0.0', url='http://www.ed.conpet.gov.br/mod_perl/bot_gateway.cgi'):
        self.name = name
        self.port = port
        self.server = server
        self.url = url

    def name(self):
        return self.name

    def say(self, text):
        svr = self.server + ':' + self.port
        params = dict(server=svr,charset_post='utf-8',
        charset='utf-8',pure=1,js=0,tst=1, msg=text)

        r = requests.get(self.url, params=params)
        return self.name + ': ' + re.sub(r'\n+$','', r.text)
