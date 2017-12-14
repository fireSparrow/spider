
from grab import Grab
from proxy import get_proxy


class BaseParser:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def parse(self):
        return {}

    def _checkup(self, content):
        return True


class HtmlParser(BaseParser):

    def _grab_page(self):
        res = None
        while not self._checkup(res):
            proxy = get_proxy() if self.proxy else None
            g = Grab(proxy=proxy)
            g.go(self.url)
            res = g.doc.select('.')
        return res

    def _checkup(self, content):
        check = self.templates.get('check')
        if check and content:
            if content.select(check[0]):
                return bool(content.select(check))
            else:
                return False
        else:
            return bool(content)

    def _extract_blocks(self, page):
        tc = self.templates.get('container')
        tb = self.templates.get('block')
        return page.select(tc).select(tb)

    def _extract_item(self, block):
        ti = self.templates.get('item', {})
        return {k: block.select(t).text() for k, t in ti.items()}

    def parse(self):
        page = self._grab_page()
        blocks = self._extract_blocks(page)
        print(len(blocks))
        return [self._extract_item(block) for block in blocks]





if __name__ == '__main__':
    parser = HtmlParser(url='kinozal.tv', proxy=True, check=('*/title', 'Торрент трекер Кинозал.ТВ'))
    print(parser.parse())