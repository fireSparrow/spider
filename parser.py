
from grab import Grab
from proxy import get_proxy


class BaseParser:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def parse(self):
        return {}

    def examine(self, content):
        return True


class HtmlParser(BaseParser):

    def _grab_page(self):
        res = None
        while not self.checkup(res):
            print("Попытка...")
            proxy = get_proxy() if self.proxy else None
            g = Grab(proxy=proxy)
            g.go(self.url)
            res = g.doc.select('.')
        return res

    def checkup(self, content):
        check = getattr(self, 'check', None)
        if check and content:
            if content.select(check[0]):
                return content.select(check[0]).text() == check[1]
            else:
                return False
        else:
            return bool(content)

    def _extract(self, page):
        return page.html()

    def parse(self):
        return self._extract(self._grab_page())





if __name__ == '__main__':
    parser = HtmlParser(url='kinozal.tv', proxy=True, check=('*/title', 'Торрент трекер Кинозал.ТВ'))
    print(parser.parse())