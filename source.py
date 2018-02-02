
from parser import HtmlParser


class BaseEngine:

    _parser = None
    _params = {'proxy': False}
    _templates = {}

    def _get_parser(self, params):
        return self._parser(**params, templates=self._templates)

    def get_items(self):
        parser = self._get_parser(self._params)
        return parser.parse()


class KinozalSearch(BaseEngine):

    _parser = HtmlParser
    _base_url = 'http://kinozal.tv/browse.php?s='
    _templates = {
        'container': '*//table[contains(@class, "t_peer")]',
        'block': 'tr[contains(@class, "bg")]',
        'check': '*/title[text()="Раздачи :: Кинозал.ТВ"]',
        'item': {
            'title': 'td[@class="nam"]',
            'url': 'td[@class="nam"]/a/@href',
            'size': 'td[@class="s"][2]'
        }
    }
    _params = {'proxy': 'True'}

    def __init__(self, search):
        params = self._params.copy()
        params['url'] = self._base_url + search
        self._params = params


if __name__ == '__main__':
    k = KinozalSearch(search='simpsons')
    print(k.get_items())