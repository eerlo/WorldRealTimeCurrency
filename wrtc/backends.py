#-*- coding: utf-8 -*-
import urllib2
from lxml import html
class BCBBackend(object):
    """
    Get currencies from the Brazilian Central Bank
    """
    _url = u'https://www3.bcb.gov.br/ptax_internet/consultarTodasAsMoedas.do?method=consultaTodasMoedas'
    
    def get_currencies(self):
        response = urllib2.urlopen(self._url)
        parsed_html = html.fromstring(response.read())
        currencies = {}
        for tr in parsed_html.cssselect('table tr'):
            tds = tr.cssselect(u'td')
            if not len(tds):#its the headers
                continue
            currency = tds[2].text_content()
            currencies[currency] = {}
            currencies[currency][u'import'] = tds[3].text_content()
            currencies[currency][u'export'] = tds[4].text_content()
        return currencies